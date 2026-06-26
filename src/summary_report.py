import pandas as pd

df = pd.read_csv(
    "comparison_report.csv"
)

print("\nImages:", len(df))

print(
    "\nAverage Contrast Increase:",
    df["contrast_change"].mean()
)

print(
    "\nAverage Brightness Change:",
    df["brightness_change"].mean()
)

print(
    "\nImproved:"
)

print(
    (df["status"] == "Improved").sum()
)

print(
    "\nDegraded:"
)

print(
    (df["status"] == "Degraded").sum()
)