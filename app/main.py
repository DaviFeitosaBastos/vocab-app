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
    except FileNotFoundError as e:
        with open("progress.json", "w", encoding="utf-8") as file:
            json.dump({"seen": []}, file, indent=4)
        return {"seen": []}

def load_dictionary(relative_path):
    absolute_path = os.path.join(app_dir, relative_path)
    with open(absolute_path, "r", encoding="utf-8") as file:
        return json.load(file)

    
load_files = load_progress("progress.json")
load_dict = load_dictionary("../data/processed/dictionary.json")

unseen = [word for word in load_dict if word["Id"] not in load_files["seen"]]
sort_word = random.sample(unseen, 1)


if load_files:
    print(f"[green]Loaded progress.json[/] -> total length [{len(load_files)} words][green]✔[/]")
    print(f"[green]Loaded dictionary.json[/] -> total length [{len(load_dict)} words][green]✔[/]")
    print(f"[green]Loaded unseen[/] -> total length [{len(unseen)} words][green]✔[/]")
    print(f"{sort_word}")
else:
    print("Empty")