
verbform = "2. Person Singular, Futur composé von avoir"
verbsolution = "as eu"
erroneousUserInput = "tu as eu"
isVerbCorrect = "1"
date = "11-07-2019"


class TestDatabase:

    def test_trackUserPerformance(self, setupDB):
        setupDB.trackUserPerformance(verbform, verbsolution, erroneousUserInput, isVerbCorrect, date)

        cursor = setupDB.connection.cursor()
        cursor.execute("SELECT * FROM `trackusersuccessfailure`;")

        res = cursor.fetchall()

        cursor.close()
        df = 34


        # now test data needs to be rollbacked somehow?