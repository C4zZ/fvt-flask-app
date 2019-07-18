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

    # Taken from the doc comment of Flask().test_client() method:
    # Note that if you are testing for assertions or exceptions in your
    # application code, you must set ``app.testing = True`` in order for the
    # exceptions to propagate to the test client.  Otherwise, the exception
    # will be handled by the application (not visible to the test client) and
    # the only indication of an AssertionError or other exception will be a
    # 500 status code response to the test client.  See the :attr:`testing`
    # attribute.  For example::

    #    app.testing = True
    #    client = app.test_client()
    app.testing = True

    # saving app.test_client() inside app so that unit tests are possible
    # e.g. that request methods like get() and post() are available
    test_client = app.test_client()

    return test_client


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
