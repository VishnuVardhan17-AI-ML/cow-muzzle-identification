import pandas as pd

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

sample = df.sample(
    n=10000,
    random_state=42
)

sample.to_csv(
    "sample_10000_images.csv",
    index=False
)

print("Selected:", len(sample))