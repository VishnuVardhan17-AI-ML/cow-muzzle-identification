import pandas as pd
import requests
import ast
import os

os.makedirs("dataset/random500", exist_ok=True)

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

# Random 500 rows
df = df.sample(
    n=500,
    random_state=42
)

count = 0

for _, row in df.iterrows():

    try:
        urls = ast.literal_eval(
            row["imageUrls"]
        )

        if "facePic" not in urls:
            continue

        response = requests.get(
            urls["facePic"],
            timeout=30
        )

        if response.status_code == 200:

            filename = (
                f"img_{count+1}.jpg"
            )

            with open(
                os.path.join(
                    "dataset/random500",
                    filename
                ),
                "wb"
            ) as f:

                f.write(
                    response.content
                )

            count += 1

            print(
                f"Downloaded {filename}"
            )

    except:
        pass

print(
    f"\nTotal Downloaded: {count}"
)