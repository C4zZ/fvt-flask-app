import pytest

from fvt.DBConfigReader import DBConfigReader


@pytest.fixture()
def DB_TestConfigReader():
    configReader = DBConfigReader("DBTestConfig.cfg")
    return configReader


class TestDBConfigReader:

    def test_DBConfigReader_read_test_host(self, DB_TestConfigReader):
        assert DB_TestConfigReader.getHost() == "host"

    def test_DBConfigReader_read_test_user(self, DB_TestConfigReader):
        assert DB_TestConfigReader.getUser() == "user"

    def test_DBConfigReader_read_test_password(self, DB_TestConfigReader):
        assert DB_TestConfigReader.getPassword() == "secretpassword"

    def test_DBConfigReader_read_test_db(self, DB_TestConfigReader):
        assert DB_TestConfigReader.getDB() == "database"

    def test_DBConfigReader_read_test_testing(self, DB_TestConfigReader):
        assert DB_TestConfigReader.isTestingDB() == True
