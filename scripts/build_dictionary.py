import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def load_json(relative_path: str):
    absolute_path = os.path.join(script_dir, relative_path)
    with open(absolute_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_json(relative_path: str, result: list):
    absolute_path = os.path.join(script_dir, relative_path)
    with open(absolute_path, "w", encoding="utf-8") as file:
        return json.dump(result, file, indent=4)

merged = load_json("../data/raw/formated_words.json")
wordfreq = load_json("../data/raw/word_frequency.json")

def build_dictionary(merged: list, wordfreq: list) -> list:
    """ 
    Receive parameters merged and wordfreq and return the dictionary
    """
    dictionary = []
    counting = 0 
    index = 1
    for value in wordfreq:
        if value[0].upper() in merged:
            data = merged[value[0].upper()]

            if not data["MEANINGS"] == []:
                grammar_class = data["MEANINGS"][0][0]
                definitions = data["MEANINGS"][0][1]
                dictionary.append({
                    "Id": index,
                    "Word": value[0].lower(),
                    "Meanings": [grammar_class, definitions],
                    "Synonyms": data["SYNONYMS"],
                })
                index += 1
        else:
            counting += 1

    return dictionary

result = build_dictionary(merged, wordfreq)
save_json("../data/processed/dictionary.json", result)

if __name__ == "__main__":
    print(f"Merged loaded: {len(merged)} words")
    print(f"Wordfreq loaded: {len(wordfreq)} words")
    print(f"Dictionary saved: {len(result)} words")