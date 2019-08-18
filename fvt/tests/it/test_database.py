import pytest

verbform = ""
verbsolution = ""
erroneousUserInput = ""
isVerbCorrect = ""
date = ""


class TestDatabase:

    def test_trackUserPerformance_wrong_verb(self, testDB):
        erroneousUserInput = "WRONG_USER_INPUT"
        query = get_trackUserPerformance_results_for(testDB, verbform, verbsolution, erroneousUserInput, date)
        assert 0 in query
        assert 1 not in query[1:]

    def test_trackUserPerformance_correct_verb(self, testDB):
        query = get_trackUserPerformance_results_for(testDB, verbform, verbsolution, erroneousUserInput, date)
        assert 1 in query
        assert 0 not in query[1:]

    def test_buildprésent1(self, testDB):
        pass


def get_trackUserPerformance_results_for(db, verbform, verbsolution, erroneousUserInput, date):
    db.trackUserPerformance(verbform, verbsolution, erroneousUserInput, date)

    with db.connection.cursor() as cursor:
        cursor.execute("SELECT * FROM trackusersuccessfailure")
        query = cursor.fetchall()[0]

        return query