import pytest
from fvt import PyMySQLDBConnection

@pytest.fixture()
def setupDB():
    db = PyMySQLDBConnection()
    return db


class TestDatabase:
    """
    TestDatabase is responsible for testing database methods reading or writing data form/to the database
    """

    def test_allTablesAvailableInDB(self, setupDB):
        """
        testing if all 3 tables (namely 'présent', 'testtbl' and 'trackusersuccessfailure') exist inside the database.
        """
        table_names = setupDB.getTableNames()

        assert len(table_names) == 3 and \
            "présent" in table_names and \
            "testtbl" in table_names and \
            "trackusersuccessfailure" in table_names

    def test_getColumnNamesFromTable_trackusersuccessfailure(self, setupDB):
        """
        testing if all 6 columns (namely 'error_id', 'verbform', 'verb', 'erroneousUserInput', 'state' and 'date') are
        present inside the table 'trackusersuccessfailure'
        """
        column_names = setupDB.getColumnNamesFromTable_trackusersuccessfailure()

        assert len(column_names) == 6 and \
            "error_id" in column_names and \
            "verbform" in column_names and \
            "verb" in column_names and \
            "erroneousUserInput" in column_names and \
            "state" in column_names and \
            "date" in column_names

    def test_trackUserPerformance(self):
        pass
