import pytest
from fvt import PyMySQLDBConnection
from ..persistence.database import getColumnNamesFromTable_trackusersuccessfailure, getTableNames


@pytest.fixture()
def setupDB():
    db = PyMySQLDBConnection()
    return db

class TestDatabase:
    """
    TestDatabase is responsible for testing database methods reading or writing data form/to the database
    """

    def test_allTablesAvailableInDB(self):
        """

        """
        table_names = getTableNames()

        assert len(table_names) == 3

    def test_getColumnNamesFromTable_trackusersuccessfailure(self):
        """
        testing if all 6 columns (namely 'error_id', 'verbform', 'verb', 'erroneousUserInput', 'state' and 'date') are
        present inside the table 'trackusersuccessfailure'
        """
        column_names = getColumnNamesFromTable_trackusersuccessfailure()

        assert len(column_names) == 6
