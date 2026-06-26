import pandas as pd

df = pd.read_csv(
    "image_quality_report.csv"
)

worst = df.sort_values(
    by=[
        "grade",
        "blur_score",
        "contrast"
    ],
    ascending=[
        False,
        True,
        True
    ]
)

worst.head(100).to_csv(
    "top_100_worst_images.csv",
    index=False
)

print("Top 100 Worst Images Saved")