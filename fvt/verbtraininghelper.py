# 
# the verbtraininghelper.py module implements features like:
# - loading all verbforms of all verbs in a dictionary as follows: 
#           d = { "some verbform": 0, "another verbform": 2, ..., "yet another verbform": 1 }
#   every value of every key value pair is initially set to zero
#    
# - checking if user has typed a given verbform correctly three consecutive times. If not 
#   then the value in the dict above is set to zero. When value reaches 3 (the user has 
#   typed in the correct given verbform three consecutive times) the key value pair of that
#   verbform should be removed from the dictionary.
#

import os.path
from pathlib import Path

PATH_TO_FILE = "/home/deev/webapps/fvt/htdocs/fvt/verbtrainer.txt"

#
# testfunctions
#
def createFile():
    f_path = Path(PATH_TO_FILE)
    
    if not f_path.is_file():
        f = open(PATH_TO_FILE, "w+")
        f.close()

def writeToFile(text):
    createFile()

    f = open(PATH_TO_FILE, "a")
    f.write(text + '\n')

#
# loads every verbform of the verbs être prendre and aller in the tenses 
# présent and passé composé in a multidimensional dictionary
#
def loadVerbtrainerDictionary(tensesList, verbsList):
    verbtrainerDictionary = {}
    
    for verb in verbsList:
        verbtrainerDictionary[verb] = loadTensesIntoVerb(tensesList)

    return verbtrainerDictionary

def experiment():
    verbs = ["aller", "prendre", "être", "savoir", "avoir"]
    tenses = ["présent", "passé composé", "passé simple", "futur composé", "futur simple"]

    testString = str(loadVerbtrainerDictionary(tenses, verbs)["aller"]["passé composé"]["Pl"]["2"])

    writeToFile(testString)



#
# helper functions
#

def loadTensesIntoVerb(tensesList):
    d = {}
    for tense in tensesList:
        d[tense] = loadSingularAndPluralIntoTense()
    return d

def loadSingularAndPluralIntoTense():
    d = {
        "Sg": {1:0, 2:0, 3:0},
        "Pl": {1:0, 2:0, 3:0}
        }
    return d
