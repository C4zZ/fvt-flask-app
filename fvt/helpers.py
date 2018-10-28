import random
import datetime
from . db import conn, db
import pymysql as MySQLdb
from . grammar import *
import json
from flask import jsonify

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

def newRandomVerb():

    person = [1, 2, 3]

    zahl = ["Singular", "Plural"]
    
    # the global variable zeit is not right in the scope of the function
    # newRandomVerb(). it only is a random letter. In the scope of the 
    # function checkVerb() it is a lits of french tenses.
    #zeit = global zeit
    # for the Impérativ only 1Sg, 1Pl and 2Pl is needed as perszahl(variable in checkVerb function)

    zeit = [
        #"Präsens",
        "Passé composé",
        #"Futur composé",
        #"Impératif"
    ]
    
    # choosing random person
    randint = random.randint(0, 2)
    person = str(person[randint])

    # choosing random zahl
    randint = random.randint(0, 1)
    zahl = zahl[randint]

    # choosing random zeit
    zeitlen = len(zeit)-1
    randint = random.randint(0, zeitlen)
    zeit = zeit[randint]

    # creating verblist
    db.execute("SELECT infinitiv FROM présent")
    llist = db.fetchall()

    # because of db = conn.cursor(MySQLdb.cursors.DictCursor)
    # llist (above) is a list of dictionaries with one key-value pair.
    # newRandomVerb only needs the values of each dict in this list-> llist
    # needs to get transformed with listOfDictsToList to a list of verbs.
    verbs = listOfDictsToList(llist)

    # choosing random verb
    verbslen = len(verbs)-1
    randint = random.randint(0, verbslen)
    verb = verbs[randint]


    verbViewForm = person + ". Person " + zahl + ", " + zeit + " von " + verb + "." 
    verbComponents = [verb, zeit, zahl, person]
    res = [verbViewForm, verbComponents]
    return jsonify(res)


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
    

    # personalpronomen doesnt get removed and thus evvery correct verb typed in by the user 
    # is renderd as wrong because the verbsolution doesnt contain a personalpronomen
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
    # 0 is false
    # 1 is true
    bitboolean = 0

    if toCheck == verbsolution:
        bitboolean = 1

    # tracks the successful and failed userinputs of a given verb
    # column names for table trackUserSuccessFailure
    # error_id - error_id
    # verbform - verbform
    # verb - verbsolution
    # erroneousUserInput - erroneousUserInput
    # state - bitboolean
    # date - date
    
    if bitboolean == 0:
        db.execute("INSERT INTO trackUserSuccessFailure \
        (verbform, verb, erroneousUserInput, state, date) VALUES (%s, %s, %s, %s, %s)", \
        (verbform, verbsolution, erroneousUserInput, bitboolean, date))
    
    else :
        db.execute("INSERT INTO trackUserSuccessFailure \
        (verbform, verb, erroneousUserInput, state, date) VALUES (%s, %s, '', %s, %s)", \
        (verbform, verbsolution, bitboolean, date))
    
    conn.commit()
    
    data = [bitboolean, verbform]
    # with jsonify data gets returned as a string
    # ensure_ascii is off to prevent characters with accents to get encoded 
    return json.dumps({'data': data}, ensure_ascii=False)


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

    