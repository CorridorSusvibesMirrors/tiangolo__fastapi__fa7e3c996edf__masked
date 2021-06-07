import gzip
import json

import pytest
from fastapi import Request
from fastapi.testclient import TestClient

from docs_src.custom_request_and_route.tutorial001 import app


@app.get("/check-class")
async def check_gzip_request(request: Request):
    return {"request_class": type(request).__name__}


client = TestClient(app)




def test_request_class():
    response = client.get("/check-class")
    assert response.json() == {"request_class": "GzipRequest"}
