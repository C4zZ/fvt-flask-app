import pytest
from flask import url_for, request


class TestApp:

    def test_index_200_response_ok(self, client):
        res = client.get("/")
        assert res.status_code == 200
    
