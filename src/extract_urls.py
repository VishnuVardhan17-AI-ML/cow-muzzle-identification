import pandas as pd
import ast

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

sample = ast.literal_eval(
    df["imageUrls"][0]
)

print(sample)