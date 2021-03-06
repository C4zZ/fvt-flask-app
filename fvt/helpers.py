import datetime

from fvt.persistence.database import callTrackUserPerformance, callGetRandomBaseVerb, call_build_présent, \
    call_build_passé_composé
from .verb import Verb


zeit = [
        "Präsens",
        "Passé composé",
        "Futur composé"
        #"Impérativ"
    ]

personalpronomen = [
        "elles",
        "ils",
        "je",
        "tu",
        "il",
        "elle",
        "on",
        "nous",
        "vous"
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

    # removing potentially written personal pronouns from the beginning of the user_input string
    user_input = remove_pronouns_from_user_input(user_input)

    # getting the important elements from the check String (person, number, tense, verb)
    person = get_person_from_verbform(verbform)
    number = get_number_from_verbform(verbform)
    tense = get_tense_from_verbform(verbform)
    infinitive = get_infinitive_from_verbform(verbform)

    # getting the actual correct solution for the given verbform for comparing against the input of the user
    verbsolution = get_verb_solution(tense, infinitive, person, number)

    # determine whether the user input is correct or not
    if user_input == verbsolution:
        isVerbCorrect = True
        erroneousUserInput = ""
    else:
        isVerbCorrect = False
        erroneousUserInput = user_input

    # tracking users performance with the help of given data
    callTrackUserPerformance(verbform, verbsolution, erroneousUserInput, date)

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
    """
    get_verb_solution determines which tense to use for building the verbsolution, calls a respective function for
    building the verbsolution for the needed tense and returns the newly built verbsolution.

    :param tense: tense denotes the place in time of the action (condition, state of being, etc.) represented by the
    verb.
    :param infinitive: the base form of a verb.
    :param person: person refers to whether the subject is first person (“je” or “nous”), second person (“tu” or “vous”)
    or third person (“il”/“elle”/“on” or “ils”/“elles”).
    :param number: number refers to whether the subject of the verb is singular or plural.
    :return:
    """
    if tense == "Präsens":
        verbsolution = call_build_présent(infinitive, person, number)


    elif tense == "Passé composé":
        verbsolution = call_build_passé_composé(infinitive, person, number)

    # checking a verb in a different tense
    else:
        verbsolution = "OTHER VERBTENSE"

    return verbsolution


def remove_pronouns_from_user_input(user_input):
    """
    remove_pronouns_from_user_input removes the substrings 'je', 'j'', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils',
    'elles' and their capitalized forms, if they are present, from the beginning of the user_input.

    :param user_input: the string from which the above substring should be removed.
    :return: A string without the above mentioned substrings.
    """

    if user_input.startswith("j'") or user_input.startswith("J'"):
        user_input = user_input.split("'", 1)[1]

    for i in range(len(personalpronomen)):
        personal_pronoun = personalpronomen[i]

        if user_input.startswith(personal_pronoun) or user_input.startswith(personal_pronoun.capitalize()):
            user_input = user_input[len(personal_pronoun):]

        if user_input[0] == " ":
            user_input = user_input[1:]

    return user_input


def get_person_from_verbform(verbform):
    person = verbform.split(". Person ", 1)[0]
    if len(person) > 1:
        person = ""
    return person

def get_number_from_verbform(verbform):
    number = verbform.split(", ", 1)[0].split(" ")[2]
    if number == "Singular":
        return "Sg"
    elif number == "Plural":
        return "Pl"
    else:
        return ""


def get_infinitive_from_verbform(verbform):
    infinitive = verbform.split(" von ")[1]
    infinitive = infinitive.replace(".", "")
    return infinitive


def get_tense_from_verbform(verbform):
    for tense in zeit:
        if tense in verbform:
            return tense
    return ""