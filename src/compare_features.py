import pickle
import cv2

# Load features
with open("outputs/orb_features_original.pkl", "rb") as f:
    original = pickle.load(f)

with open("outputs/orb_features_clahe.pkl", "rb") as f:
    clahe = pickle.load(f)

matcher = cv2.BFMatcher(
    cv2.NORM_HAMMING,
    crossCheck=True
)

# Example pair
img1 = "cow_1.jpg"
img2 = "cow_2.jpg"

des1 = original[img1]["descriptors"]
des2 = original[img2]["descriptors"]

matches = matcher.match(des1, des2)

print("Original Matches:", len(matches))

des1 = clahe[img1]["descriptors"]
des2 = clahe[img2]["descriptors"]

matches = matcher.match(des1, des2)

print("CLAHE Matches:", len(matches))