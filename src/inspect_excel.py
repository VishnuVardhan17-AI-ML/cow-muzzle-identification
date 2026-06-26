import pandas as pd
import ast

# ==========================
# CONFIG
# ==========================
EXCEL_FILE = "cattle_export.xlsx"

# ==========================
# READ EXCEL
# ==========================
df = pd.read_excel(EXCEL_FILE, engine="openpyxl")

print("\n========== DATASET SUMMARY ==========")
print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

print("\nAvailable Columns:")
for col in df.columns:
    print(f" - {col}")

# ==========================
# DETECT UNIQUE ID COLUMN
# ==========================
possible_id_cols = [
    col for col in df.columns
    if "unique" in col.lower()
    or col.lower() == "id"
    or "cattle" in col.lower()
]

print("\nPossible ID Columns:")
for col in possible_id_cols:
    print(f" - {col}")

# ==========================
# DETECT IMAGE URL COLUMNS
# ==========================
image_columns = []

for col in df.columns:

    sample = df[col].dropna().astype(str).head(10)

    for value in sample:

        if "http" in value or "image" in value.lower() or "facePic" in value:
            image_columns.append(col)
            break

print("\nPossible Image Columns:")
for col in image_columns:
    print(f" - {col}")

# ==========================
# SAMPLE IMAGE INFO
# ==========================
if image_columns:

    img_col = image_columns[0]

    print("\nSample Image Entries:")

    count = 0

    for value in df[img_col].dropna():

        try:
            parsed = ast.literal_eval(str(value))

            print(parsed)

            count += 1

            if count == 3:
                break

        except Exception:
            print(value)

            count += 1

            if count == 3:
                break

print("\n========== INSPECTION COMPLETE ==========")