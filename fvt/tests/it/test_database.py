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
    
    # tests for irregular verb être
    def test_buildpresent_etre1(self, testDB):
        assert testDB.build_présent("être", "1", "Sg") == "suis"

    def test_buildpresent_etre2(self, testDB):
        assert testDB.build_présent("être", "2", "Sg") == "es"

    def test_buildpresent_etre3(self, testDB):
        assert testDB.build_présent("être", "3", "Sg") == "est"

    def test_buildpresent_etre4(self, testDB):
        assert testDB.build_présent("être", "1", "Pl") == "sommes"

    def test_buildpresent_etre5(self, testDB):
        assert testDB.build_présent("être", "2", "Pl") == "êtes"

    def test_buildpresent_etre6(self, testDB):
        assert testDB.build_présent("être", "3", "Pl") == "sont"
        
    # tests for irregular verb aller
    def test_buildpresent_aller1(self, testDB):
        assert testDB.build_présent("aller", "1", "Sg") == "vais"

    def test_buildpresent_aller2(self, testDB):
        assert testDB.build_présent("aller", "2", "Sg") == "vas"

    def test_buildpresent_aller3(self, testDB):
        assert testDB.build_présent("aller", "3", "Sg") == "va"

    def test_buildpresent_aller4(self, testDB):
        assert testDB.build_présent("aller", "1", "Pl") == "allons"

    def test_buildpresent_aller5(self, testDB):
        assert testDB.build_présent("aller", "2", "Pl") == "allez"

    def test_buildpresent_aller6(self, testDB):
        assert testDB.build_présent("aller", "3", "Pl") == "vont"

    # tests for irregular verb avoir
    def test_buildpresent_avoir1(self, testDB):
        assert testDB.build_présent("avoir", "1", "Sg") == "ai"

    def test_buildpresent_avoir2(self, testDB):
        assert testDB.build_présent("avoir", "2", "Sg") == "as"

    def test_buildpresent_avoir3(self, testDB):
        assert testDB.build_présent("avoir", "3", "Sg") == "a"

    def test_buildpresent_avoir4(self, testDB):
        assert testDB.build_présent("avoir", "1", "Pl") == "avons"

    def test_buildpresent_avoir5(self, testDB):
        assert testDB.build_présent("avoir", "2", "Pl") == "avez"

    def test_buildpresent_avoir6(self, testDB):
        assert testDB.build_présent("avoir", "3", "Pl") == "ont"

def get_trackUserPerformance_results_for(db, verbform, verbsolution, erroneousUserInput, date):
    db.trackUserPerformance(verbform, verbsolution, erroneousUserInput, date)

    with db.connection.cursor() as cursor:
        cursor.execute("SELECT * FROM trackusersuccessfailure")
        query = cursor.fetchall()[0]

        return query