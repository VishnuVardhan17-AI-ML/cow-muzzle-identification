from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
import requests
import ast
import logging
import time
from tqdm import tqdm
from threading import Lock

# ============================================================
# CONFIGURATION
# ============================================================

EXCEL_FILE = "cattle_export.xlsx"

DATASET_DIR = Path("dataset")

LOG_DIR = Path("logs")

REPORT_FILE = "download_report.csv"

MAX_WORKERS = 16

TIMEOUT = 30

MAX_RETRIES = 3

# ============================================================
# CREATE REQUIRED DIRECTORIES
# ============================================================

DATASET_DIR.mkdir(exist_ok=True)

LOG_DIR.mkdir(exist_ok=True)

# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    filename=LOG_DIR / "download.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

# ============================================================
# HTTP SESSION
# ============================================================

session = requests.Session()

session.headers.update({
    "User-Agent": "Cow-Muzzle-Dataset-Builder/1.0"
})

# ============================================================
# GLOBALS
# ============================================================

download_report = []

downloaded_urls = set()

url_lock = Lock()

report_lock = Lock()

stats = {
    "total_urls":0,
    "downloaded":0,
    "failed":0,
    "missing":0,
    "duplicate":0,
    "already_exists":0
}

# ============================================================
# HELPERS
# ============================================================

def safe_filename(name):

    invalid='<>:"/\\|?*'

    for c in invalid:
        name=name.replace(c,"_")

    return name


def parse_image_dict(value):

    if pd.isna(value):
        return {}

    try:
        data=ast.literal_eval(str(value))

        if isinstance(data,dict):
            return data

    except Exception:
        pass

    return {}


def create_image_name(key,index):

    if key:

        return f"{safe_filename(key)}.jpg"

    return f"image_{index:02d}.jpg"


def append_report(
    cattle_id,
    image_url,
    local_path,
    image_name,
    status,
    error=""
):

    with report_lock:

        download_report.append({

            "cattle_id":cattle_id,

            "image_url":image_url,

            "local_file_path":str(local_path),

            "image_name":image_name,

            "download_status":status,

            "error_message":error

        })

# ============================================================
# CREATE DOWNLOAD TASKS
# ============================================================

def build_tasks(df):

    tasks=[]

    for _,row in df.iterrows():

        cattle_id=str(row["uniqueId"])

        folder=DATASET_DIR/cattle_id
        
        folder.mkdir(parents=True, exist_ok=True)

        images=parse_image_dict(row["imageUrls"])

        index=1

        for key,url in images.items():

            image_name=create_image_name(key,index)

            image_path=folder/image_name

            tasks.append({

                "cattle_id":cattle_id,

                "url":url,

                "image_name":image_name,

                "image_path":image_path

            })

            index+=1

    return tasks

# ============================================================
# DOWNLOAD ENGINE
# ============================================================

def download_image(task):

    cattle_id = task["cattle_id"]
    url = task["url"]
    image_name = task["image_name"]
    image_path = task["image_path"]

    # -------------------------------
    # Missing URL
    # -------------------------------
    if not url or str(url).strip() == "":

        stats["missing"] += 1

        append_report(
            cattle_id,
            url,
            image_path,
            image_name,
            "Missing URL",
            "Empty URL"
        )

        return

    # -------------------------------
    # Duplicate URL
    # -------------------------------
    with url_lock:

        if url in downloaded_urls:

            stats["duplicate"] += 1

            append_report(
                cattle_id,
                url,
                image_path,
                image_name,
                "Duplicate",
                "Duplicate URL"
            )

            return

        downloaded_urls.add(url)

    # -------------------------------
    # Already Exists
    # -------------------------------
    if image_path.exists():

        stats["already_exists"] += 1

        append_report(
            cattle_id,
            url,
            image_path,
            image_name,
            "Already Exists",
            ""
        )

        return

    # -------------------------------
    # Download with Retry
    # -------------------------------
    for attempt in range(MAX_RETRIES):

        try:

            response = session.get(
                url,
                timeout=TIMEOUT,
                stream=True
            )

            response.raise_for_status()

            with open(image_path, "wb") as f:

                for chunk in response.iter_content(8192):

                    if chunk:
                        f.write(chunk)

            stats["downloaded"] += 1

            append_report(
                cattle_id,
                url,
                image_path,
                image_name,
                "Downloaded",
                ""
            )

            logger.info(f"Downloaded {image_path}")

            return

        except Exception as e:

            error = str(e)

            logger.warning(
                f"Retry {attempt+1}: {image_name} -> {error}"
            )

    # -------------------------------
    # Failed
    # -------------------------------
    stats["failed"] += 1

    append_report(
        cattle_id,
        url,
        image_path,
        image_name,
        "Failed",
        error
    )

    logger.error(f"Failed {image_name}")


# ============================================================
# PARALLEL DOWNLOADER
# ============================================================

def run_downloader(tasks):

    print(f"\nTotal Images : {len(tasks)}\n")

    stats["total_urls"] = len(tasks)

    with ThreadPoolExecutor(
        max_workers=MAX_WORKERS
    ) as executor:

        futures = [

            executor.submit(
                download_image,
                task
            )

            for task in tasks

        ]

        for _ in tqdm(
            as_completed(futures),
            total=len(futures),
            desc="Downloading Images"
        ):

            pass
        
        # ============================================================
# SAVE DOWNLOAD REPORT
# ============================================================

def save_report():

    report_df = pd.DataFrame(download_report)

    report_df.to_csv(
        REPORT_FILE,
        index=False
    )

    print(f"\nDownload report saved : {REPORT_FILE}")


# ============================================================
# PRINT FINAL SUMMARY
# ============================================================

def print_summary(start_time):

    elapsed = time.time() - start_time

    print("\n" + "=" * 50)

    print("DOWNLOAD SUMMARY")

    print("=" * 50)

    print(f"Total URLs        : {stats['total_urls']}")
    print(f"Downloaded        : {stats['downloaded']}")
    print(f"Already Exists    : {stats['already_exists']}")
    print(f"Duplicate URLs    : {stats['duplicate']}")
    print(f"Missing URLs      : {stats['missing']}")
    print(f"Failed Downloads  : {stats['failed']}")
    print(f"Execution Time    : {elapsed:.2f} seconds")

    print("=" * 50)


# ============================================================
# MAIN
# ============================================================

def main():

    start_time = time.time()

    print("Reading Excel...")

    df = pd.read_excel(
        EXCEL_FILE,
        engine="openpyxl"
    )

    # Remove rows without uniqueId
    df = df.dropna(subset=["uniqueId"])

    # Replace missing imageUrls with empty string
    df["imageUrls"] = df["imageUrls"].fillna("")

    print(f"Records Loaded : {len(df)}")

    print("Building download tasks...")

    tasks = build_tasks(df)

    print(f"Tasks Created : {len(tasks)}")

    run_downloader(tasks)

    save_report()

    print_summary(start_time)

    logger.info("Download completed successfully")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()