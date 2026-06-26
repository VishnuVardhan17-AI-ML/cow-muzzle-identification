import pandas as pd
import shutil
import os

df = pd.read_csv("comparison_report.csv")

os.makedirs(
    "before_after_examples",
    exist_ok=True
)

# Top 10 improvements
best = df.sort_values(
    "contrast_change",
    ascending=False
).head(10)

# Top 10 degradations
worst = df.sort_values(
    "contrast_change",
    ascending=True
).head(10)

# Save best examples
for i, row in enumerate(best.itertuples(), start=1):

    image = row.image_name

    shutil.copy(
        f"outputs/original/{image}",
        f"before_after_examples/best_{i}_before.jpg"
    )

    shutil.copy(
        f"outputs/clahe/{image}",
        f"before_after_examples/best_{i}_after.jpg"
    )

# Save worst examples
for i, row in enumerate(worst.itertuples(), start=1):

    image = row.image_name

    shutil.copy(
        f"outputs/original/{image}",
        f"before_after_examples/worst_{i}_before.jpg"
    )

    shutil.copy(
        f"outputs/clahe/{image}",
        f"before_after_examples/worst_{i}_after.jpg"
    )

print("Examples Saved")