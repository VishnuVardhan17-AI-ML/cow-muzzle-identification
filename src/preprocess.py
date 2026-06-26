import cv2
import os

input_folder = "dataset/cow1"
output_folder = "processed/cow1"

os.makedirs(output_folder, exist_ok=True)

clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8,8)
)

for file in os.listdir(input_folder):

    img_path = os.path.join(input_folder, file)

    img = cv2.imread(img_path)

    if img is None:
        continue

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    enhanced = clahe.apply(gray)

    save_path = os.path.join(
        output_folder,
        file
    )

    cv2.imwrite(
        save_path,
        enhanced
    )

print("Preprocessing Complete")