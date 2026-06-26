import pandas as pd
import requests
import ast
import os

os.makedirs(
    "dataset/production_test",
    exist_ok=True
)

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

selected = pd.read_csv(
    "selected_50_animals.csv"
)

animal_ids = selected["uniqueId"].tolist()

downloaded = 0

for animal_id in animal_ids:

    animal_rows = df[
        df["uniqueId"] == animal_id
    ].head(5)

    count = 1

    for _, row in animal_rows.iterrows():

        try:

            urls = ast.literal_eval(
                row["imageUrls"]
            )

            if "facePic" not in urls:
                continue

            image_url = urls["facePic"]

            response = requests.get(
                image_url,
                timeout=30
            )

            if response.status_code == 200:

                filename = (
                    f"{animal_id}_{count}.jpg"
                )

                filepath = os.path.join(
                    "dataset/production_test",
                    filename
                )

                with open(
                    filepath,
                    "wb"
                ) as f:

                    f.write(
                        response.content
                    )

                print(
                    f"Downloaded {filename}"
                )

                downloaded += 1
                count += 1

        except Exception as e:
            print(e)

print(
    f"\nTotal Downloaded: {downloaded}"
)