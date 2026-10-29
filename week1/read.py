from pathlib import Path
path = Path("data/practice.txt")
with path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)