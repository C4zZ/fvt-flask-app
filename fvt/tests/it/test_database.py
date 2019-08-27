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
        assert testDB.build_passé_composé("être", "1", "Sg") == "ai été"
        assert testDB.build_passé_composé("être", "2", "Sg") == "as été"
        assert testDB.build_passé_composé("être", "3", "Sg") == "a été"
        assert testDB.build_passé_composé("être", "1", "Pl") == "avons été"
        assert testDB.build_passé_composé("être", "2", "Pl") == "avez été"
        assert testDB.build_passé_composé("être", "3", "Pl") == "ont été"
        
    # tests for irregular verb aller
    def test_buildpresent_aller(self, testDB):
        assert testDB.build_présent("aller", "1", "Sg") == "vais"
        assert testDB.build_présent("aller", "2", "Sg") == "vas"
        assert testDB.build_présent("aller", "3", "Sg") == "va"
        assert testDB.build_présent("aller", "1", "Pl") == "allons"
        assert testDB.build_présent("aller", "2", "Pl") == "allez"
        assert testDB.build_présent("aller", "3", "Pl") == "vont"

    def test_build_passe_compose_aller(self, testDB):
        assert testDB.build_passé_composé("aller", "1", "Sg") == "suis allé"
        assert testDB.build_passé_composé("aller", "2", "Sg") == "es allé"
        assert testDB.build_passé_composé("aller", "3", "Sg") == "est allé"
        assert testDB.build_passé_composé("aller", "1", "Pl") == "sommes allés"
        assert testDB.build_passé_composé("aller", "2", "Pl") == "êtes allés"
        assert testDB.build_passé_composé("aller", "3", "Pl") == "sont allés"

    # tests for irregular verb avoir
    def test_buildpresent_avoir(self, testDB):
        assert testDB.build_présent("avoir", "1", "Sg") == "ai"
        assert testDB.build_présent("avoir", "2", "Sg") == "as"
        assert testDB.build_présent("avoir", "3", "Sg") == "a"
        assert testDB.build_présent("avoir", "1", "Pl") == "avons"
        assert testDB.build_présent("avoir", "2", "Pl") == "avez"
        assert testDB.build_présent("avoir", "3", "Pl") == "ont"

    def test_build_passe_compose_avoir(self, testDB):
        assert testDB.build_passé_composé("avoir", "1", "Sg") == "ai eu"
        assert testDB.build_passé_composé("avoir", "2", "Sg") == "as eu"
        assert testDB.build_passé_composé("avoir", "3", "Sg") == "a eu"
        assert testDB.build_passé_composé("avoir", "1", "Pl") == "avons eu"
        assert testDB.build_passé_composé("avoir", "2", "Pl") == "avez eu"
        assert testDB.build_passé_composé("avoir", "3", "Pl") == "ont eu"
        
    # tests for irregular verb faire
    def test_buildpresent_faire(self, testDB):
        assert testDB.build_présent("faire", "1", "Sg") == "fais"
        assert testDB.build_présent("faire", "2", "Sg") == "fais"
        assert testDB.build_présent("faire", "3", "Sg") == "fait"
        assert testDB.build_présent("faire", "1", "Pl") == "faisons"
        assert testDB.build_présent("faire", "2", "Pl") == "faites"
        assert testDB.build_présent("faire", "3", "Pl") == "font"
    
    def test_build_passe_compose_faire(self, testDB):
        assert testDB.build_passé_composé("faire", "1", "Sg") == "ai fait"
        assert testDB.build_passé_composé("faire", "2", "Sg") == "as fait"
        assert testDB.build_passé_composé("faire", "3", "Sg") == "a fait"
        assert testDB.build_passé_composé("faire", "1", "Pl") == "avons fait"
        assert testDB.build_passé_composé("faire", "2", "Pl") == "avez fait"
        assert testDB.build_passé_composé("faire", "3", "Pl") == "ont fait"

    # tests for irregular verb prendre
    def test_buildpresent_prendre(self, testDB):
        assert testDB.build_présent("prendre", "1", "Sg") == "prends"
        assert testDB.build_présent("prendre", "2", "Sg") == "prends"
        assert testDB.build_présent("prendre", "3", "Sg") == "prend"
        assert testDB.build_présent("prendre", "1", "Pl") == "prenons"
        assert testDB.build_présent("prendre", "2", "Pl") == "prenez"
        assert testDB.build_présent("prendre", "3", "Pl") == "prennent"

    def test_build_passe_compose_prendre(self, testDB):
        assert testDB.build_passé_composé("prendre", "1", "Sg") == "ai pris"
        assert testDB.build_passé_composé("prendre", "2", "Sg") == "as pris"
        assert testDB.build_passé_composé("prendre", "3", "Sg") == "a pris"
        assert testDB.build_passé_composé("prendre", "1", "Pl") == "avons pris"
        assert testDB.build_passé_composé("prendre", "2", "Pl") == "avez pris"
        assert testDB.build_passé_composé("prendre", "3", "Pl") == "ont pris"

def get_trackUserPerformance_results_for(db, verbform, verbsolution, erroneousUserInput, date):
    db.trackUserPerformance(verbform, verbsolution, erroneousUserInput, date)

    with db.connection.cursor() as cursor:
        cursor.execute("SELECT * FROM trackusersuccessfailure")
        query = cursor.fetchall()[0]

        return query