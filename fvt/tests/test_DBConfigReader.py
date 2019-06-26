import pytest

from fvt.DBConfigReader import DBConfigReader


@pytest.fixture()
def TestConfigReader():
    configReader = DBConfigReader("DBTestConfig.cfg")
    return configReader

class TestDBConfigReader:

    def test_DBConfigReader_read_test_host(self):
        pass

    def test_DBConfigReader_read_test_user(self):
        pass

    def test_DBConfigReader_read_test_password(self):
        pass

    def test_DBConfigReader_read_test_db(self):
        pass
