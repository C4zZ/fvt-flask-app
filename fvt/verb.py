from random import randint
from fvt.persistence.database import database

class Verb:
    defaultNumber = ["Singular", "Plural"]

    # for the Impérativ only 1Sg, 1Pl and 2Pl is needed as perszahl(variable in isUserInputCorrect function)
    # for the Impérativ
    # only 1Sg, 1Pl and 2Pl is needed as perszahl(variable in isUserInputCorrect function)
    defaultTenses = [
        "Präsens",
        "Passé composé",
        # "Passé simple",
        # "Imparfait",
        # "Plus-que-parfait",
        "Futur composé",
        # "Futur simple",
        # "Futur antérieur"
    ]

    def __init__(self, person=None, number=None, tense=None, baseVerb=None):
        """ __init__ creates a Verb instance. When any of the parameters person, number or tense is not given,
        __init__ generates them. The parameter baseVerb needs to be fetched from the database. Since a database call
        is involved when generating a random baseVerb it must be created outside the __init__ method.

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

        self.person = person
        self.number = number
        self.tense = tense
        self.baseVerb = baseVerb
    
    def constructVerbStringform(self):
        """ constructVerbStringform() creates a String instance of the verb based on the current instances
            person, number, tense and baseVerb.

            example:    a Verb instance instantiated as follows Verb(3, "Plural", Tenses.PRÉSENT.value, "être")
                        should build the String 'sont'.

        """

        # database should be accessed here...
        result = "" + str(self.person) + " " + self.number + " " + self.tense + " " + self.baseVerb

        return result

    def generateRandomPerson(self):
        return randint(1, 3)

    def generateRandomNumber(self):
        return self.defaultNumber[randint(0, 1)]

    def generateRandomTense(self):
        return self.defaultTenses[randint(0, len(self.defaultTenses) - 1)]
