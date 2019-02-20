class Verb:

    def __init__(self, person, number, tense, baseVerb):
        """ __init__ creates a Verb instance.
        
        Arguments:
            person {int} -- person refers to whether the subject is first person (“je” or “nous”), second person (“tu” or “vous”) or third person (“il”/“elle”/“on” or “ils”/“elles”).
            number {string} -- number refers to whether the subject of the verb is singular or plural.
            tense {string} -- tense denotes the place in time of the action (condition, state of being, etc.) represented by the verb.
            baseVerb {string} -- baseVerb refers to the actual infinitive form of the verb which should be represented by this instance
        """
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
