import cv2
import os
import numpy as np

folder = "dataset/cow1"

images = []

for file in sorted(os.listdir(folder)):
    img = cv2.imread(
        os.path.join(folder, file)
    )

    img = cv2.resize(
        img,
        (200,150)
    )

    images.append(img)

rows = []

for i in range(0, len(images), 4):
    row = np.hstack(
        images[i:i+4]
    )

    rows.append(row)

sheet = np.vstack(rows)

cv2.imwrite(
    "outputs/contact_sheet.jpg",
    sheet
)

print("Saved")