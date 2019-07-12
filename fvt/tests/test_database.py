import pytest
from fvt import FVT_DB
from ..persistence.database import getColumnNamesFromTable_trackusersuccessfailure



@pytest.fixture()
def setupDB():
    db = FVT_DB()
    return db

class TestDatabase:

    def test_getColumnNamesFromTable_trackusersuccessfailure(self):
        """
        testing if all 6 columns (namely 'error_id', 'verbform', 'verb', 'erroneousUserInput', 'state' and 'date') are
        present inside the table 'trackusersuccessfailure'
        """
        column_names = getColumnNamesFromTable_trackusersuccessfailure()

        assert len(column_names) == 6
