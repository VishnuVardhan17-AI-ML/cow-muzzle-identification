import pandas as pd
import ast

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

count = 0
rows = []

for _, row in df.iterrows():

    try:
        urls = ast.literal_eval(row["imageUrls"])

        if "facePic" not in urls:
            continue

        count += 1

        rows.append({
            "image_name": f"cow_{count}.jpg",
            "uniqueId": row["uniqueId"]
        })

        if count >= 100:
            break

    except:
        pass

mapping = pd.DataFrame(rows)

mapping.to_csv(
    "outputs/image_mapping.csv",
    index=False
)

print(mapping.head())
print("\nCSV Saved")