import cv2
import os

input_folder = "dataset/repeated"
output_folder = "processed/repeated"

os.makedirs(output_folder, exist_ok=True)

clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8,8)
)

for file in os.listdir(input_folder):

    path = os.path.join(input_folder, file)

    img = cv2.imread(path)

    if img is None:
        continue

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    enhanced = clahe.apply(gray)

    cv2.imwrite(
        os.path.join(output_folder, file),
        enhanced
    )

print("CLAHE Complete")