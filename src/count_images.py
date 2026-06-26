import pandas as pd
import ast

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

count = 0

for _, row in df.iterrows():

    try:
        urls = ast.literal_eval(
            row["imageUrls"]
        )

        if "facePic" in urls:
            count += 1

    except:
        pass

print("Total Images:", count)