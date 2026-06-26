import ast
import os
import shutil
import pandas as pd
import requests

# Create necessary directories
os.makedirs("benchmark/gallery", exist_ok=True)
os.makedirs("benchmark/query", exist_ok=True)

# Load datasets
df = pd.read_excel("cattle_export.xlsx", engine="openpyxl")
selected = pd.read_csv("selected_50_animals.csv")

# Filter main dataframe based on selected IDs
filtered = df[df["uniqueId"].isin(selected["uniqueId"])]

manifest = []
gallery_count = 0
query_count = 0

# Process each animal group
for animal_id, group in filtered.groupby("uniqueId"):
    group = group.reset_index(drop=True)
    total = len(group)

    # Determine image splitting rules
    if total >= 4:
        gallery_n = 3
    else:
        gallery_n = 2

    for idx, (_, row) in enumerate(group.iterrows()):
        try:
            urls = ast.literal_eval(row["imageUrls"])
            if "facePic" not in urls:
                continue

            image_url = urls["facePic"]

            # Split into gallery or query
            if idx < gallery_n:
                split = "gallery"
                gallery_count += 1
            else:
                split = "query"
                query_count += 1

            # Build paths and download image
            animal_folder = os.path.join("benchmark", split, animal_id)
            os.makedirs(animal_folder, exist_ok=True)

            filename = f"{animal_id}_{idx+1}.jpg"
            save_path = os.path.join(animal_folder, filename)

            r = requests.get(image_url, timeout=20)
            if r.status_code == 200:
                with open(save_path, "wb") as f:
                    f.write(r.content)
                manifest.append([animal_id, filename, split])
        except Exception:
            pass

# Save manifest and statistics
manifest_df = pd.DataFrame(
    manifest, columns=["uniqueId", "image_name", "split"]
)
manifest_df.to_csv("benchmark_manifest.csv", index=False)

stats = filtered.groupby("uniqueId").size().reset_index(name="image_count")
stats.to_csv("cattle_statistics.csv", index=False)

# Print execution report
print("\n===== REPORT =====")
print("Total Cattle:", filtered["uniqueId"].nunique())
print("Gallery Images:", gallery_count)
print("Query Images:", query_count)
print(
    "Average Images/Cattle:",
    round(len(filtered) / filtered["uniqueId"].nunique(), 2),
)
