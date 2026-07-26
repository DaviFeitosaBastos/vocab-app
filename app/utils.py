import json
from rich import print
import random
import os

app_dir = os.path.dirname(os.path.abspath(__file__))


def load_progress(relative_path):
    try:
        absolute_path = os.path.join(app_dir, relative_path)
        with open(absolute_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(absolute_path, "w", encoding="utf-8") as file:
            json.dump({"Seen": []}, file, indent=4)
        return {"Seen": []}


def load_dictionary(relative_path):
    absolute_path = os.path.join(app_dir, relative_path)
    with open(absolute_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_unseen(load_dict, load_files):
    ids_seen = set(load_files["Seen"])
    return [word for word in load_dict if word["Id"] not in ids_seen]


def save_progress(load_files, relative_path):
    absolute_path = os.path.join(app_dir, relative_path)
    with open(absolute_path, "w", encoding="utf-8") as f:
        json.dump(load_files, f, indent=4)
