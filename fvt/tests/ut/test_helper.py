from fvt.helpers import remove_pronouns_from_user_input


class TestHelper():

    def test_remove_pronouns_from_user_input_correct_pronoun_removal1(self):
        user_input = "j'irai"
        result = remove_pronouns_from_user_input(user_input)
        assert result == "irai"

    def test_remove_pronouns_from_user_input_correct_pronoun_removal2(self):
        user_input = "je vais"
        result = remove_pronouns_from_user_input(user_input)
        assert result == "vais"
    
    def test_remove_pronouns_from_user_input_correct_pronoun_removal3(self):
        pass

    def test_remove_pronouns_from_user_input_correct_pronoun_removal4(self):
        pass

    def test_remove_pronouns_from_user_input_correct_pronoun_removal5(self):
        pass

    def test_remove_pronouns_from_user_input_correct_pronoun_removal6(self):
        pass

    def test_remove_pronouns_from_user_input_correct_pronoun_removal7(self):
        pass

    def test_remove_pronouns_from_user_input_correct_pronoun_removal8(self):
        pass

    def test_remove_pronouns_from_user_input_correct_pronoun_removal9(self):
        pass

    def test_remove_pronouns_from_user_input_correct_pronoun_removal10(self):
        pass
