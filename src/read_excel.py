import pandas as pd

df = pd.read_excel("cattle_export.xlsx")

print(df.columns)

print(df["imageUrls"].head())