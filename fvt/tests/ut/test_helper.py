from fvt.helpers import remove_pronouns_from_user_input


class TestHelper():

    def test_remove_pronouns_from_user_input_correct_pronoun_removal1(self):
        assert remove_pronouns_from_user_input("j'irai") == "irai"

    def test_remove_pronouns_from_user_input_correct_pronoun_removal2(self):
        assert remove_pronouns_from_user_input("je vais") == "vais"
    
    def test_remove_pronouns_from_user_input_correct_pronoun_removal3(self):
        assert remove_pronouns_from_user_input("tu vas") == "vas"

    def test_remove_pronouns_from_user_input_correct_pronoun_removal4(self):
        assert remove_pronouns_from_user_input("il va") == "va"

    def test_remove_pronouns_from_user_input_correct_pronoun_removal5(self):
        assert remove_pronouns_from_user_input("elle va") == "va"

    def test_remove_pronouns_from_user_input_correct_pronoun_removal6(self):
        assert remove_pronouns_from_user_input("on va") == "va"

    def test_remove_pronouns_from_user_input_correct_pronoun_removal7(self):
        assert remove_pronouns_from_user_input("nous allons") == "allons"

    def test_remove_pronouns_from_user_input_correct_pronoun_removal8(self):
        assert remove_pronouns_from_user_input("vous allez") == "allez"

    def test_remove_pronouns_from_user_input_correct_pronoun_removal9(self):
        assert remove_pronouns_from_user_input("ils vont") == "vont"

    def test_remove_pronouns_from_user_input_correct_pronoun_removal10(self):
        assert remove_pronouns_from_user_input("elles vont") == "vont"
