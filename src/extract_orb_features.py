import cv2
import os
import pickle

# ORB detector
orb = cv2.ORB_create(nfeatures=1000)

input_folder = "processed/cow1"

input_folder = "dataset/cow1"

features = {}

for file in os.listdir(input_folder):

    path = os.path.join(input_folder, file)

    img = cv2.imread(
        path,
        cv2.IMREAD_GRAYSCALE
    )

    if img is None:
        continue

    keypoints, descriptors = orb.detectAndCompute(
        img,
        None
    )

    features[file] = {
        "keypoints": len(keypoints),
        "descriptors": descriptors
    }

    print(
        f"{file}: {len(keypoints)} keypoints"
    )

# Save features
with open(
    "outputs/orb_features_original.pkl",
    "wb"
) as f:

    pickle.dump(features, f)

print("\nORB Feature Extraction Complete")