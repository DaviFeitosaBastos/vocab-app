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
            json.dump({"Seen": []}, file, indent=4)
        return {"Seen": []}

def load_dictionary(relative_path):
    absolute_path = os.path.join(app_dir, relative_path)
    with open(absolute_path, "r", encoding="utf-8") as file:
        return json.load(file)

load_files = load_progress("progress.json")
load_dict = load_dictionary("../data/processed/dictionary.json")

ids_seen = {item["Id"] for item in load_files["Seen"]}
unseen = [word for word in load_dict if word["Id"] not in ids_seen]

if unseen:
    sort_word = random.sample(unseen, 1)
else:
    sort_word = []

def mark_as_seen(sorted_word):
    already_read = []
    already_read.append(sort_word[0]["Id"])
    already_read.append(sort_word[0]["Word"])
    already_read.append(sort_word[0]["Meanings"])
    return already_read

def save_progress(already_seen: list, relative_path: str):
    absolute_path = os.path.join(app_dir, relative_path)
    data = {
        "Id": already_seen[0],
        "Word": already_seen[1],
        "Meaning": already_seen[2],
    }
    
    load_files["Seen"].append(data)

    with open(absolute_path, "w", encoding="utf-8") as f:
        json.dump(load_files, f, indent=4)
    return data



if __name__=="__main__":   
    if load_files:
        print(f"[green]Loaded progress.json[/] -> total length [{len(load_files)} words][green]✔[/]")
        print(f"[green]Loaded dictionary.json[/] -> total length [{len(load_dict)} words][green]✔[/]")       
    else:
        print("Empty")