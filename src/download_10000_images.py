import pandas as pd
import requests
import ast
import os

os.makedirs(
    "dataset/quality_audit",
    exist_ok=True
)

df = pd.read_csv(
    "sample_10000_images.csv"
)

existing = len(
    os.listdir(
        "dataset/quality_audit"
    )
)

count = existing

print(
    f"Already Downloaded: {count}"
)

for idx, row in df.iloc[count:].iterrows():

    try:

        urls = ast.literal_eval(
            row["imageUrls"]
        )

        if "facePic" not in urls:
            continue

        image_url = urls["facePic"]

        response = requests.get(
            image_url,
            timeout=20
        )

        if response.status_code == 200:

            filename = (
                f"img_{count+1}.jpg"
            )

            with open(
                os.path.join(
                    "dataset/quality_audit",
                    filename
                ),
                "wb"
            ) as f:

                f.write(
                    response.content
                )

            count += 1

            if count % 100 == 0:
                print(
                    f"Downloaded {count}"
                )

    except:
        pass

print(
    f"\nTotal Downloaded: {count}"
)