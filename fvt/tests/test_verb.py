import pytest
from ..verb import Verb 
from ..tenses import Tenses

class TestVerb:
    
    def test_verb_success(self):
        assert Verb(3, "Plural", Tenses.PRÉSENT.value, "être").constructVerb() == "sont"
        
    

