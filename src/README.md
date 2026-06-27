# 🐄 Cow Muzzle Identification Dataset Builder

## Overview

This project automates the creation of a large-scale cattle image dataset for **Cow Muzzle Identification** and **Cattle Re-Identification** research.

Instead of manually organizing thousands of images, the system automatically reads cattle information from an Excel file, detects cattle IDs, downloads all available images, organizes them into folders, and generates detailed reports.

The project is designed to handle **100,000+ cattle records** efficiently using parallel downloading and robust error handling.


## 🏗️ System Architecture

```text
Excel Dataset
      │
      ▼
Inspect Dataset
      │
      ▼
Detect Cattle IDs
      │
      ▼
Extract Image URLs
      │
      ▼
Create Dataset Folders
      │
      ▼
Parallel Image Downloader
      │
      ▼
Generate Reports
      │
      ▼
Benchmark Dataset
```

---

## Features

* Automatic Excel inspection
* Automatic cattle ID detection
* Automatic image URL extraction
* Automatic folder creation for every cattle
* Parallel image downloading using ThreadPoolExecutor
* Resume support (skip already downloaded images)
* Duplicate URL detection
* Missing URL handling
* Download logging
* Automatic download report generation
* Production-quality modular Python implementation

---

## Project Structure

```
Cow_Muzzle_Identification/

src/
│
├── inspect_excel.py
├── create_dataset_folders.py
├── parse_image_urls.py
└── downloader.py

dataset/
logs/

download_report.csv
requirements.txt
README.md
```

---

## Technologies Used

* Python 3.11
* Pandas
* Requests
* OpenPyXL
* ThreadPoolExecutor
* tqdm
* Logging

---

## Workflow

1. Read the Excel dataset.
2. Detect unique cattle IDs.
3. Detect image URL columns automatically.
4. Create one folder for each cattle.
5. Parse image URLs.
6. Download images in parallel.
7. Skip existing images.
8. Detect duplicate URLs.
9. Generate download report.
10. Print execution summary.

---

## Output

The downloader automatically creates:

* Organized cattle image dataset
* download_report.csv
* download.log

Example dataset structure:

```
dataset/

├── cattle_001/
│   ├── facePic.jpg
│   ├── leftSide.jpg
│   └── rightSide.jpg
│
├── cattle_002/
│   ├── facePic.jpg
│   ├── muzzle.jpg
│   └── leftSide.jpg
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python src/downloader.py
```

---

## Sample Results

* Records Processed: 76,456
* Download Tasks: 229,366
* Images Downloaded: 106,245
* Already Existing Images: 120,784
* Duplicate URLs Detected: 2,337
* Failed Downloads: 0

---

## Future Improvements

* Automatic benchmark dataset generation
* Image quality assessment
* CLAHE preprocessing pipeline
* Model training integration
* Retrieval evaluation pipeline

---

## Author

**G. Vishnu Vardhan**

AI & Machine Learning
