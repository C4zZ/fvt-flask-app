from ..verb import Verb
from ..tenses import Tenses
# Todo: implement db with good db design


class TestVerb:
    '''
    def test_verb_success(self):
        assert Verb(3, "Plural", Tenses.PRÉSENT.value, "être").constructVerbStringform() == "sont"

    '''

    def test_generate_random_verb(self):
        verb = Verb()

        assert verb.tense in verb.defaultTenses and \
               verb.baseVerb != "" and \
               verb.number in verb.defaultNumber and \
               verb.person in [1, 2, 3]
