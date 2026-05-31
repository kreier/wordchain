import csv
import json
from pathlib import Path

csv_path = Path("../vocabulary/vietnamese.csv")
json_path = Path("../vocabulary/vietnamese.json")

entries = []
with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        entries.append({
            "vietnamese": row["word"].strip(),
            "english": row["english"].strip()
        })

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"Written {len(entries)} entries to {json_path}")
