import pandas as pd

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

count = 0
animals = []

for _, row in df.iterrows():

    try:
        if pd.isna(row["imageUrls"]):
            continue

        animals.append(
            row["uniqueId"]
        )

        count += 1

        if count >= 100:
            break

    except:
        pass

print("Images:", len(animals))
print(
    "Unique Animals:",
    len(set(animals))
)