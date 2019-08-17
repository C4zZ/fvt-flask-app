from fvt.helpers import remove_pronouns_from_user_input


class TestHelper():

    def test_remove_pronouns_from_user_input_correct_pronoun_removal(self):
        user_input = "j'irai"
        result = remove_pronouns_from_user_input(user_input)
        assert result == "irai"

    def test_remove_pronouns_from_user_input_no_pronoun_removal(self):
        user_input = "je vais"
        result = remove_pronouns_from_user_input(user_input)
        assert result == user_input