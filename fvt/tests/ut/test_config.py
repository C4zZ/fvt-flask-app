
class TestConfig:
    """
    tests for loading Flask.config form an .cfg file
    """

    def test_testConfigDebugIsEnabled(self, testingApp_config_client):
        assert testingApp_config_client.debug == True
    
    def test_testConfigTestingIsEnabled(self, testingApp_config_client):
        assert testingApp_config_client.testing == True
