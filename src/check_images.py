import cv2
import os

folder = "dataset/cow1"

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    img = cv2.imread(path)

    print(
        file,
        img.shape
    )