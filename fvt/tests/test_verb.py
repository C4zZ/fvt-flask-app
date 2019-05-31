import pytest
from ..verb import Verb 
from ..tenses import Tenses
# commented out because can not implement this business logic yet. Need a reliable webserver like nginx first
# Todo: implement db with good db design


class TestVerb:
    '''
    def test_verb_success(self):
        assert Verb(3, "Plural", Tenses.PRÉSENT.value, "être").constructVerb() == "sont"

    '''

    def test_generateRandomBaseVerb(self):
        assert Verb().generateRandomBaseVerb() == "test"
