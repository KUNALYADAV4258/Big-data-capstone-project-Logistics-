
import csv
from pathlib import Path

# Locate the datasets folder
project_folder = Path(__file__).resolve().parent.parent
dataset_folder = project_folder / "datasets"

# Find all CSV files
csv_files = list(dataset_folder.glob("*.csv"))

if not csv_files:
    print("No CSV files found!")
else:
    print("DATA EXTRACTION STARTED")
    print("-" * 40)

    for file in csv_files:
        print("\nDataset:", file.name)

        with open(file, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f)

            headers = next(reader, [])
            row_count = sum(1 for row in reader)

        print("Columns:", len(headers))
        print("Column names:", headers)
        print("Total records:", row_count)
        print("File size:", round(file.stat().st_size / 1024, 2), "KB")
        print("Status: Successfully accessed")

    print("\nDATA EXTRACTION CHECK COMPLETED")
