import pandas as pd
import requests
import ast
import os

# Folder create
os.makedirs("dataset/repeated", exist_ok=True)

# Read excel
df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

# Animals with 2+ records
counts = df["uniqueId"].value_counts()
repeated_ids = counts[counts >= 2].index.tolist()

# First 20 animals
selected_ids = repeated_ids[:20]

count = 0

for uid in selected_ids:

    animal_rows = df[df["uniqueId"] == uid]

    animal_count = 0

    for _, row in animal_rows.iterrows():

        try:
            urls = ast.literal_eval(row["imageUrls"])

            if "facePic" not in urls:
                continue

            image_url = urls["facePic"]

            response = requests.get(
                image_url,
                timeout=30
            )

            if response.status_code == 200:

                filename = (
                    f"{uid}_{animal_count+1}.jpg"
                )

                filepath = os.path.join(
                    "dataset/repeated",
                    filename
                )

                with open(filepath, "wb") as f:
                    f.write(response.content)

                animal_count += 1
                count += 1

                print(
                    f"Downloaded {filename}"
                )

            # Only 2 images per animal
            if animal_count >= 2:
                break

        except Exception as e:
            print("Error:", e)

print(
    f"\nTotal Downloaded: {count}"
)