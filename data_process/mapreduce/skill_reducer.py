import sys
from collections import defaultdict


skill_count = defaultdict(int)

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        skill, count = line.split("\t", 1)
        skill_count[skill] += int(count)

    except Exception:
        continue


for skill, count in sorted(
    skill_count.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{skill}\t{count}")