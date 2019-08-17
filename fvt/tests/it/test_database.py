import pytest

verbform = ""
verbsolution = ""
erroneousUserInput = ""
isVerbCorrect = ""
date = ""


class TestDatabase:

    def test_trackUserPerformance_wrong_verb(self, testDB):

        verbform = "verbform"
        verbsolution = "verbsolution"
        erroneousUserInput = "WRONG_USER_INPUT"
        date = "11-07-2019"

        query = get_query_results_for(testDB, verbform, verbsolution, erroneousUserInput, date)

        assert verbform in query
        assert verbsolution in query
        assert erroneousUserInput in query
        assert 0 in query
        assert date in query

    def test_trackUserPerformance_right_verb(self, testDB):
        pass


def get_query_results_for(db, verbform, verbsolution, erroneousUserInput, date):
    db.trackUserPerformance(verbform, verbsolution, erroneousUserInput, date)

    with db.connection.cursor() as cursor:
        cursor.execute("SELECT * FROM trackusersuccessfailure")
        query = cursor.fetchall()[0]

        return query