class TestConfig:
    """
    tests for loading Flask.config form an .cfg file
    """

    def test_testConfigDebugIsEnabled(self, testingApp_config_client):
        assert testingApp_config_client.debug == True
    
    def test_testConfigTestingIsEnabled(self, testingApp_config_client):
        assert testingApp_config_client.testing == True

    def test_productionConfigDebugIsDisabled(self, productionApp_config_client):
        assert productionApp_config_client.debug == False

    def test_productionConfigTestingIsDisabled(self, productionApp_config_client):
        assert productionApp_config_client.testing == False
