from random import randint
from .database import db
from .helpers import listOfDictsToList

class Verb:
    number = ["Singular", "Plural"]
    tense = [
        "Präsens",
        "Passé composé",
        "Futur composé"
        # "Impérativ"
    ]

    def __init__(self, person=None, number=None, tense=None, baseVerb=None):
        """ __init__ creates a Verb instance.
        Arguments:
            person {int} -- person refers to whether the subject is first person (“je” or “nous”), second person (“tu” or “vous”) or third person (“il”/“elle”/“on” or “ils”/“elles”).
            number {string} -- number refers to whether the subject of the verb is singular or plural.
            tense {string} -- tense denotes the place in time of the action (condition, state of being, etc.) represented by the verb.
            baseVerb {string} -- baseVerb refers to the actual infinitive form of the verb which should be represented by this instance
        """
        if person is None:
            person = self.generateRandomPerson()

        if number is None:
            number = self.generateRandomNumber()

        if tense is None:
            tense = self.generateRandomTense()

        if baseVerb is None:
            baseVerb = self.generateRandomBaseVerb()


        self.person = person
        self.number = number
        self.tense = tense
        self.baseVerb = baseVerb
    
    def constructVerb(self):
        """ constructVerb() creates a String instance of the verb based on the current instances
            person, number, tense and baseVerb.

            example:    a Verb instance instantiated as follows Verb(3, "Plural", Tenses.PRÉSENT.value, "être")
                        should build the String 'sont'.

        """

        return "" + str(self.person) + " " + self.number + " " + self.tense + " " + self.baseVerb

    def generateRandomPerson(self):
        return randint(1, 3)

    def generateRandomNumber(self):
        return self.number[randint(0, 1)]

    def generateRandomTense(self):
        return self.tense[randint(0, len(self.tense) - 1)]

    def generateRandomBaseVerb(self):

        linkedVerbsList = db\
            .execute("SELECT infinitiv FROM présent")\
            .fetchall()

        # because of db = conn.cursor(MySQLdb.cursors.DictCursor)
        # linkedVerbsList (above) is a list of dictionaries with one key-value pair.
        # newRandomVerb only needs the values of each dict in this list-> llist
        # needs to get transformed with listOfDictsToList to a list of verbs.
        verbsList = listOfDictsToList(linkedVerbsList)

        verb = verbsList[randint(0, len(verbsList) - 1)]

        return verb
