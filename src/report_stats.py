import pandas as pd

df = pd.read_csv(
    "outputs/quality_report.csv"
)

print(
    df["quality_tier"]
    .value_counts()
)