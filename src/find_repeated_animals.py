import pandas as pd

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

counts = df["uniqueId"].value_counts()

repeated = counts[counts >= 2]

print("Animals with 2+ images:", len(repeated))

print(repeated.head(20))