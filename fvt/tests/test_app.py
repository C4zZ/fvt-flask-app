import pytest
from flask import url_for, request


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
        assert res.data.decode("utf-8") != ""
    
    '''
    def test_validateverb_POST_200_response(self, client):
        res = client.post("/validateverb")
        assert res.status_code == 200
    '''
