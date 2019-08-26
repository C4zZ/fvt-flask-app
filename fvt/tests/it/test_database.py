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
    def test_buildpresent_etre(self, testDB):
        assert testDB.build_présent("être", "1", "Sg") == "suis"
        assert testDB.build_présent("être", "2", "Sg") == "es"
        assert testDB.build_présent("être", "3", "Sg") == "est"
        assert testDB.build_présent("être", "1", "Pl") == "sommes"
        assert testDB.build_présent("être", "2", "Pl") == "êtes"
        assert testDB.build_présent("être", "3", "Pl") == "sont"

    def test_build_passe_compose_etre(self, testDB):
        pass
        
    # tests for irregular verb aller
    def test_buildpresent_aller(self, testDB):
        assert testDB.build_présent("aller", "1", "Sg") == "vais"
        assert testDB.build_présent("aller", "2", "Sg") == "vas"
        assert testDB.build_présent("aller", "3", "Sg") == "va"
        assert testDB.build_présent("aller", "1", "Pl") == "allons"
        assert testDB.build_présent("aller", "2", "Pl") == "allez"
        assert testDB.build_présent("aller", "3", "Pl") == "vont"

    # tests for irregular verb avoir
    def test_buildpresent_avoir(self, testDB):
        assert testDB.build_présent("avoir", "1", "Sg") == "ai"
        assert testDB.build_présent("avoir", "2", "Sg") == "as"
        assert testDB.build_présent("avoir", "3", "Sg") == "a"
        assert testDB.build_présent("avoir", "1", "Pl") == "avons"
        assert testDB.build_présent("avoir", "2", "Pl") == "avez"
        assert testDB.build_présent("avoir", "3", "Pl") == "ont"
    
    # tests for irregular verb faire
    def test_buildpresent_faire(self, testDB):
        assert testDB.build_présent("faire", "1", "Sg") == "fais"
        assert testDB.build_présent("faire", "2", "Sg") == "fais"
        assert testDB.build_présent("faire", "3", "Sg") == "fait"
        assert testDB.build_présent("faire", "1", "Pl") == "faisons"
        assert testDB.build_présent("faire", "2", "Pl") == "faites"
        assert testDB.build_présent("faire", "3", "Pl") == "font"

    # tests for irregular verb prendre
    def test_buildpresent_prendre(self, testDB):
        assert testDB.build_présent("prendre", "1", "Sg") == "prends"
        assert testDB.build_présent("prendre", "2", "Sg") == "prends"
        assert testDB.build_présent("prendre", "3", "Sg") == "prend"
        assert testDB.build_présent("prendre", "1", "Pl") == "prenons"
        assert testDB.build_présent("prendre", "2", "Pl") == "prenez"
        assert testDB.build_présent("prendre", "3", "Pl") == "prennent"

def get_trackUserPerformance_results_for(db, verbform, verbsolution, erroneousUserInput, date):
    db.trackUserPerformance(verbform, verbsolution, erroneousUserInput, date)

    with db.connection.cursor() as cursor:
        cursor.execute("SELECT * FROM trackusersuccessfailure")
        query = cursor.fetchall()[0]

        return query