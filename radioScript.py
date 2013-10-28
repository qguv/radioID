#!/usr/bin/env python3
# WCWM Helper
# Helps to come up with varying id calls, witty statements, and PSAs

import json
from random import choice
from textwrap import wrap

# Loading data from file into dict `data`
with open('data.json', 'r') as f:
    data = json.load(f)
    ids = data['ids']
    chuckles = data['chuckles']
    psas = data['psas']

# Defining some convenient functions
def cls():
    for null in range(150):
        print()

def pprint(inString):
    lines = wrap(inString, 80)
    for line in lines:
        print(line)

def yesNo(prompt, default):
    if default:
        options = " [Y/n] "
    else:
        options = " [y/N] "
    out = None
    while out == None:
        ynChoice = input(prompt + options).strip().lower()
        if ynChoice == 'y':
            out = True
        elif ynChoice == 'n':
            out = False
        elif ynChoice == '':
            out = default
        else:
            print("Huh?", end=' ')
    return out

# Functions to scrape datafile
def buildCategories(dictionary):
    return list(dictionary.keys())

def askCategories(collection):
    allCategories = buildCategories(collection)
    pprint(', '.join(sorted(allCategories)))
    prompt = "Type categories separated by commas or type 'all': "
    categories = input(prompt).strip()
    if categories == 'all':
        return allCategories
    else:
        if ', ' in categories:
            return categories.split(', ')
        else:
            return categories.split(',')

def getEntriesOfCategories(categories, collection):
    entries = list()
    for category in categories:
        entries.extend(collection[category])
    return entries

cls()

# Choosing parameters
doPsaChoice = yesNo("Do you want a PSA?", False)
doChooseCategory = yesNo("Do you want to choose categories?", False)
if doChooseCategory:
    print()
    chuckleCategoryChoices = getEntriesOfCategories(askCategories(chuckles), chuckles)
else:
    chuckleCategoryChoices = getEntriesOfCategories(buildCategories(chuckles), chuckles)
if doPsaChoice and doChooseCategory:
    print()
    psaCategoryChoices = getEntriesOfCategories(askCategories(psas), psas)
elif doPsaChoice and not doChooseCategory:
    psaCategoryChoices = getEntriesOfCategories(buildCategories(psas), psas)


# Meat & Potatoes
runLoop = True
while runLoop:
    cls()
    pprint(choice(ids))
    print()
    pprint(choice(chuckleCategoryChoices))
    print()
    if doPsaChoice:
        print()
        pprint(choice(psaCategoryChoices))
        print()
    if input("<Enter> to continue, <Q> to quit. ").lower() == 'q':
        runLoop = False

