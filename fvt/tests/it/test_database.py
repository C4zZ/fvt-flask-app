
verbform = "2. Person Singular, Futur composé von avoir"
verbsolution = "as eu"
erroneousUserInput = "tu as eu"
isVerbCorrect = "1"
date = "11-07-2019"


class TestDatabase:

    def test_trackUserPerformance(self, setupDB):
        setupDB.trackUserPerformance(verbform, verbsolution, erroneousUserInput, isVerbCorrect, date)

        cursor = setupDB.connection.cursor()
        cursor.execute("SELECT * FROM trackusersuccessfailure")

        res = cursor.fetchall()[0]
        assert verbform in res and \
                verbsolution in res and \
                erroneousUserInput in res and \
                int(isVerbCorrect) in res and \
                date in res