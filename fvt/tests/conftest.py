import pytest
from fvt import create_app, PyMySQLDBConnection

""" conftest.py defines pytest fixtures which are useful for testing this application. 
"""
@pytest.fixture
def fixture_default_client():
    app = create_app()
    return app


@pytest.fixture
def test_client():
    app = create_app()

    # saving test_client() inside app so that unit tests are possible 
    # e.g. that request methods like get() and post() are available
    app = app.test_client()

    return app


@pytest.fixture
def testingApp_config_client():
    app = create_app("testingApp.cfg")
    return app


@pytest.fixture
def productionApp_config_client():
    app = create_app("productionApp.cfg")
    return app


@pytest.fixture()
def testDB():
    db = PyMySQLDBConnection(config_filename="testingDB.cfg")
    return db
