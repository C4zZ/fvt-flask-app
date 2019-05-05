""" tests for loading Flask.config form an .cfg file
"""


class TestConfig:

    def test_testConfigDebugIsEnabled(self, config_testing_client):
        assert config_testing_client.debug == True
    
    def test_testConfigTestingIsEnabled(self, config_testing_client):
        assert config_testing_client.testing == True
    
