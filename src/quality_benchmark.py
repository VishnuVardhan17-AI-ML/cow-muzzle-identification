import cv2
import os
import pandas as pd

input_folder = "dataset/random500"

original_folder = "outputs/original"
clahe_folder = "outputs/clahe"

os.makedirs(original_folder, exist_ok=True)
os.makedirs(clahe_folder, exist_ok=True)

clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8,8)
)

results = []

for file in os.listdir(input_folder):

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

    enhanced = clahe.apply(gray)

    cv2.imwrite(
        os.path.join(
            original_folder,
            file
        ),
        gray
    )

    cv2.imwrite(
        os.path.join(
            clahe_folder,
            file
        ),
        enhanced
    )

    blur_score = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()

    contrast_before = gray.std()

    contrast_after = enhanced.std()

    if contrast_after > contrast_before:

        quality = "Improved"

    elif contrast_after < contrast_before:

        quality = "Degraded"

    else:

        quality = "Unchanged"

    results.append([
        file,
        round(blur_score,2),
        round(contrast_before,2),
        round(contrast_after,2),
        quality
    ])

df = pd.DataFrame(
    results,
    columns=[
        "image_name",
        "blur_score",
        "contrast_before",
        "contrast_after",
        "quality_tier"
    ]
)

df.to_csv(
    "outputs/quality_report.csv",
    index=False
)

print(df.head())

print(
    "\nCSV Saved"
)