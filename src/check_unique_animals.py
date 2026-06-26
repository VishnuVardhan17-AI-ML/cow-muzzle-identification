import pandas as pd

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

print("Total Records:",
      len(df))

print("Unique Animals:",
      df["uniqueId"].nunique())