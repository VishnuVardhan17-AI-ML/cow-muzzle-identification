import cv2
import pickle
import os

folder = "dataset/repeated"

orb = cv2.ORB_create(1000)

features = {}

for file in os.listdir(folder):

    img = cv2.imread(
        os.path.join(folder, file),
        0
    )

    kp, des = orb.detectAndCompute(
        img,
        None
    )

    features[file] = des

with open(
    "outputs/repeated_original.pkl",
    "wb"
) as f:
    pickle.dump(features, f)

print("Original Features Saved")