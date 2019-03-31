import pytest
from .. import create_app

""" conftest.py defines pytest fixtures which are useful for testing this application. 
"""
@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    app.testing = True
    return app

@pytest.fixture
def testClient(app):
    return app.test_client()