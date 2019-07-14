
class TestConfig:
    """
    tests for loading Flask.config form an .cfg file
    """

    def test_testConfigDebugIsEnabled(self, config_testing_client):
        assert config_testing_client.debug == True
    
    def test_testConfigTestingIsEnabled(self, config_testing_client):
        assert config_testing_client.testing == True
