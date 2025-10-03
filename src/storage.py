from pathlib import Path
import json

DATA_PATH = Path("Alarms.json")


def save(alarms):
    with open(DATA_PATH, "w") as file:
        json.dump(alarms, file, indent=4)


def load():
    if not DATA_PATH.exists():
        return {"CPU": [], "Memory": [], "Disk": []}
    with open(DATA_PATH, "r") as file:
        return json.load(file)

