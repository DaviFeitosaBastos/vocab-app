from utils import load_dictionary, load_progress, get_unseen, save_progress
import random


class Api:
    def __init__(self) -> None:
        self.dictionary = load_dictionary("../data/processed/dictionary.json")
        self.progress = load_progress("progress.json")
        self.unseen = get_unseen(self.dictionary, self.progress)

    def search_word(self, term):
        for word in self.dictionary:
            if word["Word"] == term:
                return word
            elif word['Id'] == term:
                return word
        return None

    def get_daily_word(self):
        if self.unseen:
            word = random.sample(self.unseen, 1)[0]
            self.mark_as_seen(word["Id"])
            return word
        return None

    def mark_as_seen(self, word_id):
        self.progress["Seen"].append(word_id)
        save_progress(self.progress, "progress.json")
        self.unseen = [w for w in self.unseen if w["Id"] != word_id]

    def get_progress(self):
        seen_count = len(self.progress["Seen"])
        total = len(self.dictionary)
        remaining = len(self.unseen)
        percent = round((seen_count / total) * 100, 1)

        return {
            "seen_count": seen_count,
            "total": total,
            "remaining": remaining,
            "percent": percent,
            "seen_words": [
                w for w in self.dictionary if w["Id"] in self.progress["Seen"]
            ],
        }
