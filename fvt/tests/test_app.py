import pytest
from flask import url_for, request


class TestApp:

    def test_ping(self, client):
        res = client.get("/")
        assert res.status_code == 200
        
