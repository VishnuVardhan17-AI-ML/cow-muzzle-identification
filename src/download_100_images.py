import pandas as pd
import requests
import ast
import os

# Create folder
os.makedirs("dataset/cow1", exist_ok=True)

# Read excel
df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

count = 0

for i, row in df.iterrows():

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

            filename = f"cow_{count+1}.jpg"

            with open(
                os.path.join(
                    "dataset/cow1",
                    filename
                ),
                "wb"
            ) as f:

                f.write(response.content)

            print(
                f"Downloaded {filename}"
            )

            count += 1

        if count >= 100:
            break

    except Exception as e:
        print("Error:", e)

print(
    f"\nTotal Downloaded: {count}"
)