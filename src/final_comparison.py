import pickle
import cv2
import os
from itertools import combinations

# Load features
with open("outputs/repeated_original.pkl", "rb") as f:
    original = pickle.load(f)

with open("outputs/repeated_clahe.pkl", "rb") as f:
    clahe = pickle.load(f)

matcher = cv2.BFMatcher(
    cv2.NORM_HAMMING,
    crossCheck=True
)

same_original = []
same_clahe = []

different_original = []
different_clahe = []

files = list(original.keys())

# SAME ANIMAL PAIRS
animal_groups = {}

for file in files:

    animal_id = "_".join(
        file.split("_")[:-1]
    )

    animal_groups.setdefault(
        animal_id,
        []
    ).append(file)

for animal, imgs in animal_groups.items():

    if len(imgs) < 2:
        continue

    img1, img2 = imgs[0], imgs[1]

    des1 = original[img1]
    des2 = original[img2]

    matches = matcher.match(des1, des2)

    same_original.append(
        len(matches)
    )

    des1 = clahe[img1]
    des2 = clahe[img2]

    matches = matcher.match(des1, des2)

    same_clahe.append(
        len(matches)
    )

# DIFFERENT ANIMAL PAIRS
animals = list(
    animal_groups.keys()
)

for i in range(
    min(20, len(animals)-1)
):

    img1 = animal_groups[
        animals[i]
    ][0]

    img2 = animal_groups[
        animals[i+1]
    ][0]

    des1 = original[img1]
    des2 = original[img2]

    matches = matcher.match(
        des1,
        des2
    )

    different_original.append(
        len(matches)
    )

    des1 = clahe[img1]
    des2 = clahe[img2]

    matches = matcher.match(
        des1,
        des2
    )

    different_clahe.append(
        len(matches)
    )

print("\n===== RESULTS =====")

print(
    "Same Animal Original:",
    sum(same_original)/len(same_original)
)

print(
    "Same Animal CLAHE:",
    sum(same_clahe)/len(same_clahe)
)

print(
    "Different Animal Original:",
    sum(different_original)/len(different_original)
)

print(
    "Different Animal CLAHE:",
    sum(different_clahe)/len(different_clahe)
)

orig_gap = (
    sum(same_original)/len(same_original)
    -
    sum(different_original)/len(different_original)
)

clahe_gap = (
    sum(same_clahe)/len(same_clahe)
    -
    sum(different_clahe)/len(different_clahe)
)

print("\nOriginal Gap:", orig_gap)
print("CLAHE Gap:", clahe_gap)

if clahe_gap > orig_gap:
    print(
        "\nCLAHE IMPROVES SEPARABILITY"
    )
else:
    print(
        "\nCLAHE DOES NOT IMPROVE SEPARABILITY"
    )