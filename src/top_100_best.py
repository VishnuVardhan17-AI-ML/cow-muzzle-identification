import pandas as pd

df = pd.read_csv(
    "image_quality_report.csv"
)

best = df.sort_values(
    by=[
        "grade",
        "blur_score",
        "contrast"
    ],
    ascending=[
        True,
        False,
        False
    ]
)

best.head(100).to_csv(
    "top_100_best_images.csv",
    index=False
)

print("Top 100 Best Images Saved")