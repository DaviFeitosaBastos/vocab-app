import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def load_json(relative_path):
    absolute_path = os.path.join(script_dir, relative_path)
    with open(absolute_path, "r", encoding="utf-8") as file:
        return json.load(file)

merged = load_json("../data/raw/formated_words.json")
wordfreq = load_json("../data/raw/word_frequency.json")

print(f"Merged loaded: {len(merged)} words")
print(f"Wordfreq loaded: {len(wordfreq)} words")



def build_dictionary(merged, wordfreq):
    dictionary = []
    counting = 0 

    for index, value in enumerate(wordfreq):
        if value[0].upper() in merged:
            print(index, value[0].upper())
        else:
            counting += 1

    return dictionary

print(build_dictionary(merged, wordfreq))