import pytest
from flask import url_for, request
from ..helpers import newRandomVerb


class TestApp:

    def test_index_200_response(self, client):
        res = client.get("/")
        assert res.status_code == 200
    
    def test_collect_GET_200_response(self, client):
        res = client.get("/collect")
        assert res.status_code == 200

    # right now this test is irrelevant
    '''
    def test_collect_POST_200_response(self, client):
        res = client.post("/collect")
        assert res.get == 200
    '''
    
    def test_newverb_GET_200_response(self, client):
        res = client.open("/newverb")
        assert res.status_code == 200
    
    def test_newverb_GET_nonempty_String(self, client):
        res = client.open("/newverb")
        assert res.data.decode("utf-8") != ""
        assert len(res.data) > 0 
    
    def test_validateverb_POST_200_response(self, client):
        dummydata = {
            "verbform": newRandomVerb(),
            "userverb": "userinput"
        }
        res = client.post("/validateverb", data=dummydata)
        assert res.status_code == 200

    def test_validateverb_POST_userinput_success(self, client):
        dummydata = {
            "verbform": "2. Person Singular, Passé composé von avoir.",
            "userverb": "tu as eu"
        }
        res = client.post("/validateverb", data=dummydata)
        
        assert res.get_data(as_text=True) == "True"
    
    def test_validateverb_POST_userinput_fail(self, client):
        dummydata = {
            "verbform": "2. Person Singular, Passé composé von avoir.",
            "userverb": "userinput"
        }
        res = client.post("/validateverb", data=dummydata)
        assert res.get_data(as_text=True) == "False"
    
