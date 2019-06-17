import datetime
from .verb import Verb

# with this import all tests are green because the db instance inside grammar has a dictCursor
from . grammar import *


zeit = [
        "Präsens",
        "Passé composé",
        "Futur composé"
        #"Impérativ"
    ]

def getNewVerb():

    verb = Verb()

    return str(verb.person) + ". Person " + verb.number + ", " + verb.tense + " von " + verb.baseVerb + "."


def checkVerb(userVerb, correctVerbfom):

    # getting current time in the form of yyyy-mm-dd
    date = datetime.datetime.now().strftime("%d" + "-" + "%m" + "-" + "%Y")
    #return date
    # saving the whole verbform for tracking inside the table trackUserSuccessFailure
    verbform = correctVerbfom
    # saving the whole verb typed in by the user for tracking inside the table trackUserSuccessFailure
    erroneousUserInput = userVerb

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
    
    if userVerb.startswith("j'") or userVerb.startswith("J'"):
        userVerb = userVerb.split("'", 1)[1]

    for i in range(len(personalpronomen)):
        p = personalpronomen[i]
        P = personalpronomen[i].capitalize()
       
        if userVerb.startswith(p) or userVerb.startswith(P):
            if userVerb[len(p)] == " ":
                userVerb = userVerb.split(" ", 1)[1]

    # getting the important elements from the check String (person, zahl, zeit, verb)

    # person (1/2/3)
    person = correctVerbfom.split(". Person ", 1)[0]
    remove = str(person) + ". Person "
    correctVerbfom = correctVerbfom.replace(remove, "", 1)

    # zahl (Singular/Plural)
    zahl = correctVerbfom.split(", ", 1)[0]
    remove = zahl + ", "
    correctVerbfom = correctVerbfom.replace(remove, "", 1)

    if zahl == "Singular":
        zahl = "Sg"
    else:
        zahl = "Pl"

    #variable for choosing the correct column
    perszahl = person + zahl

    # zeit and verb
    zeit, infinitiv = correctVerbfom.split(" von ", 1)[0], correctVerbfom.split(" von ", 1)[1]
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

    isVerbCorrect = True if userVerb == verbsolution else False
        

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

    