import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

scripts = [
    "inspect_excel.py",
    "create_dataset_folders.py",
    "parse_image_urls.py",
    "downloader.py",
    "report_generator.py",
]

print("=" * 60)
print("COW MUZZLE IDENTIFICATION DATASET BUILDER")
print("=" * 60)

for script in scripts:
    print(f"\nRunning: {script}")

    result = subprocess.run(
        [sys.executable, str(ROOT / script)]
    )

    if result.returncode != 0:
        print(f"\nError while executing {script}")
        sys.exit(result.returncode)

print("\n" + "=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)