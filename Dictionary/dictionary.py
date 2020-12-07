import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):

    w = w.lower()
    while True:
        if w in data:
            # return data[w]
            for words in data[w]:
                print(words)

        elif len(get_close_matches(w, data.keys())) > 0:
            yn = input("Did you mean % s? Enter Y for yes, N for no: " %
                       get_close_matches(w, data.keys())[0])

            if yn == "Y":
                return get_close_matches(w, data.keys())[0]

            else:
                return "Sorry. The word you entered doesn't exist in current dictionary. enter '.' to exit "
        else:
            return "Sorry. The word you entered doesn't exist in current dictionary. enter '.' to exit "


while True:
    meaning = input("Enter a word: ")
    word = translate(meaning)

    if word == ".":
        break
