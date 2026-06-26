import pandas as pd

df = pd.read_excel(
    "cattle_export.xlsx",
    engine="openpyxl"
)

print("Total Records:", len(df))

print("\nAnimal Types:")
print(df["animalType"].value_counts())

print("\nUnique Animals:")
print(df["uniqueId"].nunique())