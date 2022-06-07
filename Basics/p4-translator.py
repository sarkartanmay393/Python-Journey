# English Translator which holds millions of words, give it a try.

import json
from difflib import get_close_matches

# data contains the dictionary itself.
data = json.load(open("p4-related.json"))


# output formater function.
def output(DataPart):
    res, once = "", True
    for each in DataPart:
        if once:
            once = False
        else:
            res += "\n"
        res += each
    return res


# This is the translation function.
def translate(word):

    if word in data:
        return output(data[word])
    elif word.title() in data:
        return output(data[word.title()])

    word = word.lower()
    close_calls = get_close_matches(word, data.keys())

    if word in data:
        return output(data[close_calls[0]])
    elif len(close_calls) > 0:
        opt = input(
            "Did you mean {} ? (Y / N)) ".format(close_calls[0].title()))
        if opt == "Y" or opt == 'y':
            return output(data[close_calls[0]])
        elif opt == "N" or opt == 'n':
            print("Double check the spelling, then")
            w = input("Type word again : ")
            return translate(w)
        else:
            return "double check..."

    # If nothing works, return this.
    return "Word doesn't exists, check first."


WordToBeSearch = ""
HelperTracker = True

while True:
    if HelperTracker:
        HelperTracker = False
        print("To exit the programme type e/")

    # search for.
    WordToBeSearch = input("Enter a word : ")

    if WordToBeSearch == '/e' or WordToBeSearch == 'e/':
        print("Exiting the programme...")
        break

    # programme finalization.
    res = translate(WordToBeSearch)  # using func here.
    print(res)
