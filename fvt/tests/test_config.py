class TestConfig:

    def test_testConfigIsEnabled(self, app):
        assert app.debug == True
