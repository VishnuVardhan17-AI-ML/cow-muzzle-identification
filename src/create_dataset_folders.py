from pathlib import Path
import pandas as pd

EXCEL_FILE = "cattle_export.xlsx"
DATASET_DIR = Path("dataset")

DATASET_DIR.mkdir(exist_ok=True)

df = pd.read_excel(EXCEL_FILE, engine="openpyxl")

# Remove missing IDs
df = df.dropna(subset=["uniqueId"])

folder_count = 0

for cattle_id in df["uniqueId"].astype(str).unique():

    folder = DATASET_DIR / cattle_id

    if not folder.exists():
        folder.mkdir(parents=True)
        folder_count += 1

print("\n========== FOLDER CREATION ==========")
print("Unique Cattle :", df["uniqueId"].nunique())
print("Folders Created :", folder_count)
print("Dataset Folder :", DATASET_DIR.resolve())
print("=====================================")