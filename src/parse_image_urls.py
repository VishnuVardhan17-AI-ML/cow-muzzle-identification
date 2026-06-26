import ast
import pandas as pd

EXCEL_FILE = "cattle_export.xlsx"

df = pd.read_excel(EXCEL_FILE, engine="openpyxl")

df = df.dropna(subset=["uniqueId", "imageUrls"])

print("Total Records:", len(df))

for _, row in df.head(5).iterrows():

    print("\nCattle:", row["uniqueId"])

    try:

        images = ast.literal_eval(str(row["imageUrls"]))

        for image_type, image_url in images.items():

            print(f"{image_type} -> {image_url}")

    except Exception as e:

        print("Parse Error:", e)