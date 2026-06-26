import cv2
import os
import pandas as pd

input_folder = "dataset/quality_audit"

results = []

files = os.listdir(input_folder)

for idx, file in enumerate(files, start=1):

    path = os.path.join(
        input_folder,
        file
    )

    img = cv2.imread(path)

    if img is None:
        continue

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    # Blur
    blur_score = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()

    # Brightness
    brightness = gray.mean()

    # Contrast
    contrast = gray.std()

    # Resolution
    height, width = gray.shape

    resolution = width * height

    # Grade
    if (
        blur_score > 1000 and
        contrast > 50 and
        resolution > 400000
    ):
        grade = "A"

    elif (
        blur_score > 500 and
        contrast > 40 and
        resolution > 250000
    ):
        grade = "B"

    elif (
        blur_score > 200 and
        contrast > 30
    ):
        grade = "C"

    else:
        grade = "D"

    results.append([
        file,
        round(blur_score, 2),
        round(brightness, 2),
        round(contrast, 2),
        width,
        height,
        resolution,
        grade
    ])

    if idx % 500 == 0:
        print(f"Processed {idx}")

df = pd.DataFrame(
    results,
    columns=[
        "image_name",
        "blur_score",
        "brightness",
        "contrast",
        "width",
        "height",
        "resolution",
        "grade"
    ]
)

df.to_csv(
    "image_quality_report.csv",
    index=False
)

print("\nSaved image_quality_report.csv")
print(df.head())