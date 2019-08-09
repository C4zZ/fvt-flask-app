import datetime

from fvt.persistence.database import callTrackUserPerformance, callGetRandomBaseVerb
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
    # because all babe verbs reside inside the database, getting a random base verb is a separate database call. This
    # database call can not happen inside the Verb class which is why it happens outside and just before the Verb() call.
    # baseVerb gets put into the Verb call as a parameter.
    baseVerb = callGetRandomBaseVerb()
    verb = Verb(baseVerb=baseVerb)

    return str(verb.person) + ". Person " + verb.number + ", " + verb.tense + " von " + verb.baseVerb + "."


def isUserInputCorrect(userVerb, correctVerbform):
    """
    isUserInputCorrect is responsible for checking the user input and tracking the performance of the user.
    :param userVerb: the user input.
    :param correctVerbform: the correct parts of the verb () in String form which needed to be inputted by the user and
                            against which the user input is compared.
    :return: True if user input is true; else returns false.
    """

    # getting current time in the form of yyyy-mm-dd
    date = datetime.datetime.now().strftime("%d" + "-" + "%m" + "-" + "%Y")

    # saving the whole verbform for tracking inside the table trackUserSuccessFailure
    verbform = correctVerbform
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

    if userVerb.startswith("j'") or userVerb.startswith("J'"):
        userVerb = userVerb.split("'", 1)[1]

    for i in range(len(personalpronomen)):
        personal_pronoun = personalpronomen[i]
        capitalized_personal_pronoun = personalpronomen[i].capitalize()
       
        if userVerb.startswith(personal_pronoun) or userVerb.startswith(capitalized_personal_pronoun):
            if userVerb[len(personal_pronoun)] == " ":
                userVerb = userVerb.split(" ", 1)[1]

    # getting the important elements from the check String (person, zahl, zeit, verb)

    # person (1/2/3)
    person = correctVerbform.split(". Person ", 1)[0]
    remove = str(person) + ". Person "
    correctVerbform = correctVerbform.replace(remove, "", 1)

    # number (Singular/Plural)
    number = correctVerbform.split(", ", 1)[0]
    remove = number + ", "
    correctVerbform = correctVerbform.replace(remove, "", 1)

    if number == "Singular":
        number = "Sg"
    else:
        number = "Pl"

    perszahl = person + number

    # zeit and verb
    tense, infinitive = correctVerbform.split(" von ", 1)[0], correctVerbform.split(" von ", 1)[1]
    infinitive = infinitive.replace(".", "")

    # checking a verb in Präsens (dbtablename for präsens 
    # was set to the french equivalent of présent) 
    # or in impératif or in passé composé or in futur composé   

    # turn SELECT output to a dictionary with the respective column names
    # of a table as key values

    if tense == "Präsens":

        verbsolution = buildprésent(infinitive, person, number)


    elif tense == "Passé composé":
        verbsolution = buildpc(infinitive, perszahl)

    elif tense == "Futur composé":
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
    
    if isVerbCorrect:
        callTrackUserPerformance(verbform, verbsolution, erroneousUserInput, isVerbCorrect, date)


    else:
        callTrackUserPerformance(verbform, verbsolution, "", isVerbCorrect, date)

    return str(isVerbCorrect)


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
    newList = iterateList(dictsList)
    return newList
