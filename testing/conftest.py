#1/usr/bin/env python3

import pytest
import requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stuntted_get():
        raise RuntimeError("netwrok acess not allowed during testing")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())
