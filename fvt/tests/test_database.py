import pytest
from fvt import FVT_DB



@pytest.fixture()
def setupDB():
    db = FVT_DB()
    return db

class TestDatabase:

    def test_defaultDatabaseConfig(self):
        pass





