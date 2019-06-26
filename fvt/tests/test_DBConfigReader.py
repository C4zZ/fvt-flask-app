import pytest

from fvt.DBConfigReader import DBConfigReader


@pytest.fixture()
def TestConfigReader():
    configReader = DBConfigReader("DBTestConfig.cfg")
    return configReader

class TestDBConfigReader:

    def test_DBConfigReader_read_test_host(self, TestConfigReader):
        assert TestConfigReader.getHost() == "host"

    def test_DBConfigReader_read_test_user(self, TestConfigReader):
        assert TestConfigReader.getUser() == "user"

    def test_DBConfigReader_read_test_password(self, TestConfigReader):
        assert TestConfigReader.getPassword() == "secretpassword"

    def test_DBConfigReader_read_test_db(self, TestConfigReader):
        assert TestConfigReader.getDB() == "database"
