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

def getNewVerb():
    # because all babe verbs reside inside the database, getting a random base verb is a separate database call. This
    # database call can not happen inside the Verb class which is why it happens outside and just before the Verb() call.
    # baseVerb gets put into the Verb call as a parameter.
    baseVerb = callGetRandomBaseVerb()
    verb = Verb(baseVerb=baseVerb)

    return str(verb.person) + ". Person " + verb.number + ", " + verb.tense + " von " + verb.baseVerb + "."


def isUserInputCorrect(user_input, verbform):
    """
    isUserInputCorrect is responsible for checking the user input and tracking the performance of the user.
    :param user_input: the user input.
    :param verbform: the correct parts of the verb () in String form which needed to be inputted by the user and
                            against which the user input is compared.
    :return: True if user input is true; else returns false.
    """

    # getting current time in the form of yyyy-mm-dd
    date = datetime.datetime.now().strftime("%d" + "-" + "%m" + "-" + "%Y")

    # saving the whole verbform for tracking inside the table trackUserSuccessFailure
    verbform = verbform
    # saving the whole verb typed in by the user for tracking inside the table trackUserSuccessFailure
    erroneousUserInput = user_input

    # removing the personal pronouns from the userinput if they exist at the beginning

    if user_input.startswith("j'") or user_input.startswith("J'"):
        user_input = user_input.split("'", 1)[1]

    for i in range(len(personalpronomen)):
        personal_pronoun = personalpronomen[i]
        capitalized_personal_pronoun = personalpronomen[i].capitalize()
       
        if user_input.startswith(personal_pronoun) or user_input.startswith(capitalized_personal_pronoun):
            if user_input[len(personal_pronoun)] == " ":
                user_input = user_input.split(" ", 1)[1]

    # getting the important elements from the check String (person, zahl, zeit, verb)

    # person (1/2/3)
    person = verbform.split(". Person ", 1)[0]
    remove = str(person) + ". Person "
    verbform = verbform.replace(remove, "", 1)

    # number (Singular/Plural)
    number = verbform.split(", ", 1)[0]
    remove = number + ", "
    verbform = verbform.replace(remove, "", 1)

    number = "Sg" if number == "Singular" else "Pl"

    # zeit and verb
    tense, infinitive = verbform.split(" von ", 1)[0], verbform.split(" von ", 1)[1]
    infinitive = infinitive.replace(".", "")

    # getting the actual correct solution for the given verbform for comparing against the input of the user
    verbsolution = get_verb_solution(tense, infinitive, person, number)

    # determine whether the user input is correct or not
    isVerbCorrect = True if user_input == verbsolution else False

    # tracking users performance with the help of given data
    if isVerbCorrect:
        callTrackUserPerformance(verbform, verbsolution, erroneousUserInput, date)

    else:
        callTrackUserPerformance(verbform, verbsolution, "", date)

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


def get_verb_solution(tense, infinitive, person, number):
    if tense == "Präsens":
        verbsolution = buildprésent(infinitive, person, number)


    elif tense == "Passé composé":
        verbsolution = buildpc(infinitive, person, number)

    # checking a verb in a different tense
    else:
        verbsolution = "OTHER VERBTENSE"

    return verbsolution


def remove_pronouns_from_user_input(user_input):
    if user_input.startswith("j'") or user_input.startswith("J'"):
        user_input = user_input.split("'", 1)[1]

    return user_input
