import random
import datetime
from .verb import Verb

# with this import all tests are green because the db instance inside grammar has a dictCursor
from . grammar import *

'''
    zeit = [
        "Präsens",
        "Passé composé",
        "Passé simple",
        "Imparfait",
        "Plus-que-parfait",
        "Futur composé",
        "Futur simple",
        "Futur antérieur"
    ]
    '''
# change here when you'll implement more tenses
# for the Impérativ only 1Sg, 1Pl and 2Pl is needed as perszahl(variable in checkVerb function)

zeit = [
        "Präsens",
        "Passé composé",
        "Futur composé"
        #"Impérativ"
    ]

def getNewVerb():

    verb = Verb()

    return str(verb.person) + ". Person " + verb.number + ", " + verb.tense + " von " + verb.baseVerb + "."


def checkVerb(toCheck, check):
    # getting current time in the form of yyyy-mm-dd
    date = datetime.datetime.now().strftime("%d" + "-" + "%m" + "-" + "%Y")
    #return date
    # saving the whole verbform for tracking inside the table trackUserSuccessFailure
    verbform = check
    # saving the whole verb typed in by the user for tracking inside the table trackUserSuccessFailure
    erroneousUserInput = toCheck

    # removing the personal pronouns from the userinput if they exist at the beginning
    personalpronomen = [
        "je ", #??
        "tu",
        "il",
        "elle",
        "on",
        "nous",
        "vous",
        "ils",
        "elles"
        ]

    global zeit
    
    if toCheck.startswith("j'") or toCheck.startswith("J'"):
        toCheck = toCheck.split("'", 1)[1]

    for i in range(len(personalpronomen)):
        p = personalpronomen[i]
        P = personalpronomen[i].capitalize()
       
        if toCheck.startswith(p) or toCheck.startswith(P):
            if toCheck[len(p)] == " ":
                toCheck = toCheck.split(" ", 1)[1]

    # getting the important elements from the check String (person, zahl, zeit, verb)

    # person (1/2/3)
    person = check.split(". Person ", 1)[0]
    remove = str(person) + ". Person "
    check = check.replace(remove, "", 1)

    # zahl (Singular/Plural)
    zahl = check.split(", ", 1)[0]
    remove = zahl + ", "
    check = check.replace(remove, "", 1)

    if zahl == "Singular":
        zahl = "Sg"
    else:
        zahl = "Pl"

    #variable for choosing the correct column
    perszahl = person + zahl

    # zeit and verb
    zeit, infinitiv = check.split(" von ", 1)[0], check.split(" von ", 1)[1]
    infinitiv = infinitiv.replace(".", "")

    # checking a verb in Präsens (dbtablename for präsens 
    # was set to the french equivalent of présent) 
    # or in impératif or in passé composé or in futur composé   

    # turn SELECT output to a dictionary with the respective column names
    # of a table as key values
    #pymysql.cursors.DictCursor
    db = conn.cursor(MySQLdb.cursors.Cursor)
    verbsolution = ""

    if zeit == "Präsens":
        #try to import the whole grammar.py module so that you can write: grammar.buildprésent(infinitiv, perszahl)
        verbsolution = buildprésent(infinitiv, perszahl)


    elif zeit == "Passé composé":
        verbsolution = buildpc(infinitiv, perszahl)

    elif zeit == "Futur composé":
        verbsolution = ""

    #Problem with Impératif
    #if zeit == "Impératif":
        #verbsolution = ""

    # checking a verb in a different tense
    else:
        verbsolution = "OTHER VERBTENSE"

    # to parse a boolean to javascript
    # checking if the verb typed by the user matches the verbsolution

    isVerbCorrect = True if toCheck == verbsolution else False
        

    # tracks the successful and failed userinputs of a given verb
    # column names for table trackUserSuccessFailure
    # error_id - error_id
    # verbform - verbform
    # verb - verbsolution
    # erroneousUserInput - erroneousUserInput
    # state - bitboolean
    # date - date
    
    if isVerbCorrect == True:
        db.execute("INSERT INTO trackUserSuccessFailure \
        (verbform, verb, erroneousUserInput, state, date) VALUES (%s, %s, %s, %s, %s)", \
        (verbform, verbsolution, erroneousUserInput, isVerbCorrect, date))
    
    else :
        db.execute("INSERT INTO trackUserSuccessFailure \
        (verbform, verb, erroneousUserInput, state, date) VALUES (%s, %s, '', %s, %s)", \
        (verbform, verbsolution, isVerbCorrect, date))
    
    conn.commit()

    return str(isVerbCorrect)


# seperate helper functions
def getDictVal(dictionary):
    for key in dictionary:
        return dictionary[key] 


def iterateList(currentList):
    newList = []
    for element in currentList:
        listElement = getDictVal(element)
        newList.append(listElement)
    return newList

def listOfDictsToList(dictsList):
    newList = []
    newList = iterateList(dictsList)
    return newList

    