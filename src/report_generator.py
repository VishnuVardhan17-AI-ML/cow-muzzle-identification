from pathlib import Path
import pandas as pd

REPORT_CSV = Path("download_report.csv")
OUTPUT_FILE = Path("download_summary.txt")


def main():

    if not REPORT_CSV.exists():
        print("download_report.csv not found!")
        return

    df = pd.read_csv(REPORT_CSV)

    total_urls = len(df)

    total_cattle = df["cattle_id"].nunique()

    downloaded = (df["download_status"] == "Downloaded").sum()

    already_exists = (df["download_status"] == "Already Exists").sum()

    duplicate = (df["download_status"] == "Duplicate").sum()

    failed = (df["download_status"] == "Failed").sum()

    missing = (df["download_status"] == "Missing URL").sum()

    report = f"""
=========================================
        DATASET DOWNLOAD REPORT
=========================================

Total Cattle          : {total_cattle}
Total Image URLs      : {total_urls}

Downloaded Images     : {downloaded}
Already Exists        : {already_exists}
Duplicate URLs        : {duplicate}
Missing URLs          : {missing}
Failed Downloads      : {failed}

=========================================
"""

    print(report)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Summary saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()