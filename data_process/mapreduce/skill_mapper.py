import sys
import csv


for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        reader = csv.reader([line])
        row = next(reader)

        if len(row) < 2:
            continue

        # skill_data.csv:
        # job_id, skill
        skill = row[1].strip()

        if skill:
            print(f"{skill}\t1")

    except Exception:
        continue