import pandas as pd

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

print(df["muzzleQuality"].value_counts(dropna=False))