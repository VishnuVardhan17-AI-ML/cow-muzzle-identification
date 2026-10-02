\# 🐄 Cow Muzzle Identification



A computer vision research project for \*\*cattle identification and re-identification using muzzle images\*\*. The project builds a large-scale cattle image dataset, performs image preprocessing and quality analysis, extracts visual features using ORB, and compares original and CLAHE-enhanced images.



\## 📌 Overview



This project automates the preparation and analysis of cattle images for \*\*Cow Muzzle Identification\*\* and \*\*Cattle Re-Identification\*\* research.



The pipeline can:



\* Read cattle information from an Excel dataset

\* Identify cattle IDs

\* Extract image URLs

\* Create cattle-specific dataset folders

\* Download large numbers of images

\* Resume downloads without overwriting existing files

\* Detect duplicate image URLs

\* Select benchmark datasets

\* Preprocess images using CLAHE

\* Extract ORB features

\* Compare original and CLAHE-based features

\* Generate image-quality and comparison reports



The dataset preparation pipeline was designed to handle \*\*100,000+ cattle records\*\*.



\---



\## 🏗️ Project Architecture



```text

&#x20;                   Excel Dataset

&#x20;                        │

&#x20;                        ▼

&#x20;                 Inspect Dataset

&#x20;                        │

&#x20;                        ▼

&#x20;                 Detect Cattle IDs

&#x20;                        │

&#x20;                        ▼

&#x20;                Extract Image URLs

&#x20;                        │

&#x20;                        ▼

&#x20;              Create Dataset Folders

&#x20;                        │

&#x20;                        ▼

&#x20;                Download Images

&#x20;                        │

&#x20;                        ▼

&#x20;               Dataset Verification

&#x20;                        │

&#x20;                        ▼

&#x20;              Benchmark Selection

&#x20;                        │

&#x20;             ┌──────────┴──────────┐

&#x20;             ▼                     ▼

&#x20;       Original Images       CLAHE Images

&#x20;             │                     │

&#x20;             ▼                     ▼

&#x20;      ORB Feature Extraction \& Comparison

&#x20;                        │

&#x20;                        ▼

&#x20;                Quality Analysis

&#x20;                        │

&#x20;                        ▼

&#x20;                   Reports

```



\---



\## ✨ Main Features



\### Dataset Preparation



\* Excel dataset inspection

\* Automatic cattle ID processing

\* Image URL extraction

\* Automatic folder creation

\* Large-scale image downloading

\* Resume support

\* Duplicate URL detection

\* Download verification



\### Computer Vision Pipeline



\* Original image preprocessing

\* CLAHE preprocessing

\* ORB feature extraction

\* Repeated-animal image analysis

\* Feature comparison

\* Image-quality benchmarking



\### Reporting



\* Download reports

\* Image-quality reports

\* Feature comparison reports

\* Summary reports

\* Before/after image examples

\* Contact sheets



\---



\## 📂 Project Structure



```text

Cow\_Muzzle\_Identification/

│

├── src/

│   ├── inspect\_excel.py

│   ├── create\_dataset\_folders.py

│   ├── parse\_image\_urls.py

│   ├── downloader.py

│   ├── extract\_orb\_features.py

│   ├── extract\_repeated\_clahe.py

│   ├── extract\_repeated\_original.py

│   ├── compare\_features.py

│   ├── final\_comparison.py

│   ├── quality\_benchmark.py

│   ├── generate\_image\_quality\_report.py

│   ├── generate\_comparison\_report.py

│   ├── create\_benchmark\_dataset.py

│   ├── create\_summary\_pdf.py

│   └── main.py

│

├── dataset/

│

├── processed/

│

├── outputs/

│   ├── original/

│   ├── clahe/

│   ├── contact\_sheet.jpg

│   ├── image\_mapping.csv

│   ├── quality\_report.csv

│   ├── orb\_features\_original.pkl

│   ├── orb\_features\_clahe.pkl

│   ├── repeated\_original.pkl

│   └── repeated\_clahe.pkl

│

├── benchmark/

│

├── requirements.txt

├── project\_structure.txt

└── README.md

```



\---



\## 🛠️ Technologies



\* Python 3.11

\* Pandas

\* NumPy

\* OpenCV

\* OpenPyXL

\* Pillow

\* Matplotlib

\* Requests

\* ThreadPoolExecutor

\* tqdm



\---



\## 🚀 Installation



Create and activate a Python environment:



```bash

python -m venv venv

```



Activate it on Windows:



```bash

venv\\Scripts\\activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\---



\## ▶️ Dataset Preparation



The main dataset preparation stages include:



```bash

python src/inspect\_excel.py

```



```bash

python src/create\_dataset\_folders.py

```



```bash

python src/parse\_image\_urls.py

```



```bash

python src/downloader.py

```



The downloader supports existing files, duplicate URLs, missing URLs, and download reporting.



\---



\## 📊 Dataset Results



The completed download pipeline processed:



| Metric            |  Result |

| ----------------- | ------: |

| Cattle IDs        |  74,137 |

| Image URLs        | 229,366 |

| Images Downloaded | 106,245 |

| Already Existing  | 120,784 |

| Duplicate URLs    |   2,337 |

| Missing URLs      |       0 |

| Failed Downloads  |       0 |



\---



\## 🔬 CLAHE Quality Benchmark



A benchmark was performed to compare \*\*original images\*\* with \*\*CLAHE-enhanced images\*\*.



Results:



```text

Total Cattle IDs       : 50

Total Images Processed : 183



Improved Images        : 159

Degraded Images        : 24



Improvement Rate       : 86.89%

Degradation Rate       : 13.11%



Average Contrast Increase : +6.81

Average Brightness Change : +4.88

```



\### Observation



CLAHE improved image-quality measurements for most of the benchmark images.



However, the benchmark also showed that \*\*CLAHE did not improve ORB-based cattle identification performance\*\*.



Therefore, image-quality improvement and identification-performance improvement are treated as separate outcomes in this project.



\---



\## 🧠 ORB Feature Analysis



The project uses \*\*ORB (Oriented FAST and Rotated BRIEF)\*\* for local visual feature extraction.



The pipeline compares:



```text

Original Image

&#x20;     │

&#x20;     ▼

ORB Feature Extraction

&#x20;     │

&#x20;     ▼

Feature Representation

```



against:



```text

CLAHE Image

&#x20;     │

&#x20;     ▼

ORB Feature Extraction

&#x20;     │

&#x20;     ▼

Feature Representation

```



The resulting feature data is stored in the `outputs/` directory for comparison and analysis.



\---



\## 📈 Generated Outputs



The project generates outputs including:



\* `quality\_report.csv`

\* `image\_mapping.csv`

\* ORB feature files

\* Original image samples

\* CLAHE image samples

\* Contact sheets

\* Comparison reports

\* Summary reports



\---



\## ⚠️ Current Project Scope



The current completed pipeline focuses on:



1\. Large-scale dataset preparation

2\. Image downloading

3\. Image-quality analysis

4\. CLAHE preprocessing

5\. ORB feature extraction

6\. Original vs CLAHE comparison

7\. Research reporting



A trained YOLO model and YOLO annotation dataset are \*\*not included in the current verified pipeline\*\*.



\---



\## 🔮 Future Improvements



Possible future extensions include:



\* YOLO-based muzzle region detection

\* Creation of an annotated muzzle dataset

\* Deep-learning-based feature extraction

\* Siamese/Triplet Network for cattle re-identification

\* Embedding-based similarity search

\* Retrieval accuracy evaluation

\* Top-K identification evaluation

\* Model training and deployment



\---



\## 👨‍💻 Author



\*\*G. Vishnu Vardhan\*\*



AI \& Machine Learning



