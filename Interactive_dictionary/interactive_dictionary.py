# An interactive Dictionary

import json

from difflib import get_close_matches

data = json.load(open('076 data.json', 'r'))


def define(w):
    w = w.lower()

    if w in data:
        print(data[w])
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Did you mean %s instead?\nEnter Y if Yes or N if No: ' % get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return 'The word doesnt exist please double check it'
        else:
            return "We didn't understand your entry"
    else:
        print('This word is not in the database')


word = input('Enter word: ')

output = define(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
