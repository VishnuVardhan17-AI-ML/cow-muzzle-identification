import pandas as pd

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

counts = df["uniqueId"].value_counts()

eligible = counts[counts >= 3]

print("Eligible Animals:", len(eligible))

selected = eligible.sample(
    n=50,
    random_state=42
)

selected.to_csv(
    "selected_50_animals.csv"
)

print("Selected Animals:", len(selected))