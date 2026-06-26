import pandas as pd

df = pd.read_csv("outputs/image_mapping.csv")

print(
    df["uniqueId"]
    .value_counts()
    .head(20)
)