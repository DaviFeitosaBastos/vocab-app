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


def get_daily_word(unseen):
    if unseen:
        return random.sample(unseen, 1)
    return []


def mark_as_seen(sort_word):
    return [sort_word[0]["Id"]]


def save_progress(already_seen, load_files, relative_path):
    absolute_path = os.path.join(app_dir, relative_path)
    load_files["Seen"].append(already_seen[0])
    with open(absolute_path, "w", encoding="utf-8") as f:
        json.dump(load_files, f, indent=4)

def search_word(load_dict: dict, term: str):
    for index in load_dict:
        if index["Word"] == term:
            return index




if __name__ == "__main__":
    load_files = load_progress("progress.json")
    load_dict = load_dictionary("../data/processed/dictionary.json")

    print(f"[green]Loaded progress.json[/] -> [{len(load_files['Seen'])} seen][green]✔[/]")
    print(f"[green]Loaded dictionary.json[/] -> [{len(load_dict)} words][green]✔[/]")

    unseen = get_unseen(load_dict, load_files)
    sort_word = get_daily_word(unseen)

    if sort_word:
        print(f"\nWord: [bold]{sort_word[0]['Word']}[/]")
        print(f"Meaning: {sort_word[0]['Meanings'][1]}")
        save_progress(mark_as_seen(sort_word), load_files, "progress.json")
    else:
        print("[yellow]No more words to learn![/]")