import pytest

from fvt.AppConfigReader import AppConfigReader


@pytest.fixture()
def App_TestConfigReader():
    configReader = AppConfigReader("AppTestConfig.cfg")
    return configReader

class TestAppConfigReader:

    def test_AppConfigReader_read_test_isTesting(self):
        pass

    def test_AppConfigReader_read_test_isDebug(self):
        pass
