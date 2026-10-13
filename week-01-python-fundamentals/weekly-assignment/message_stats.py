import csv
import json

from pathlib import Path

csv_path = Path(__file__).parent / "messages.csv"

with open(csv_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)