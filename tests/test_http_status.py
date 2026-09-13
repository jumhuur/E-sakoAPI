"""Exercise actual HTTP responses through the ASGI app without a live server."""
import asyncio
import json
from unittest.mock import mock_open, patch

import pytest

from app.main import app


def get(path):
    async def request():
        route, _, query = path.partition("?")
        messages = []

        async def receive():
            return {"type": "http.request", "body": b"", "more_body": False}

        async def send(message):
            messages.append(message)

        await app({
            "type": "http", "asgi": {"version": "3.0"},
            "http_version": "1.1", "method": "GET", "scheme": "http",
            "path": route, "raw_path": route.encode(),
            "query_string": query.encode(), "root_path": "", "headers": [],
            "client": ("127.0.0.1", 1234), "server": ("test", 80),
        }, receive, send)
        status = next(m["status"] for m in messages if m["type"] == "http.response.start")
        body = b"".join(m.get("body", b"") for m in messages if m["type"] == "http.response.body")
        return status, json.loads(body)

    return asyncio.run(request())


CALCULATORS = [
    ("gold", 320, 100), ("silver", 321, 999),
    ("sheep", 322, 56), ("rikaas", 323, 155),
    ("cows", 324, 40), ("money", 325, 12560),
    ("camels", 326, 55), ("crops", 327, 1000),
]


@pytest.mark.parametrize("name,code,amount", CALCULATORS)
def test_success(name, code, amount):
    status, body = get(f"/api/{name}/{amount}")
    assert status == 200
    assert body["code"] == 200
    assert "response" in body


@pytest.mark.parametrize("name,code,amount", CALCULATORS)
def test_below_nisab(name, code, amount):
    status, body = get(f"/api/{name}/1")
    assert status == 200
    assert body["code"] == code
    assert body["ok"] is True
    assert body["message"]


@pytest.mark.parametrize("name,code,amount", CALCULATORS)
def test_invalid_amount(name, code, amount):
    status, body = get(f"/api/{name}/invalid")
    assert status == 422
    assert body["code"] == (461 if name == "gold" else 464)
    assert body["ok"] is False


@pytest.mark.parametrize("path,code", [
    ("/api/gold/100?Type=66", 463),
    ("/api/gold/100?Type=abc", 465),
    ("/api/crops/1000?Type=4", 468),
    ("/api/crops/1000?Type=abc", 464),
])
def test_invalid_type(path, code):
    status, body = get(path)
    assert status == 422
    assert body["code"] == code
    assert body["ok"] is False


def test_gold_purity_below_nisab():
    status, body = get("/api/gold/85?Type=22")
    assert status == 200
    assert body["code"] == 466
    assert body["ok"] is True


@pytest.mark.parametrize("path", ["/api/nonexistent", "/api/gold"])
def test_missing_url(path):
    status, body = get(path)
    assert status == 404
    assert body["code"] == 404
    assert body["ok"] is False


@pytest.mark.parametrize("error", [FileNotFoundError, PermissionError])
def test_info_file_failure(error):
    with patch("app.services.info.open", side_effect=error):
        status, body = get("/api/info")
    assert status == 500
    assert body["code"] == 500
    assert body["ok"] is False


def test_info_invalid_json():
    with patch("app.services.info.open", mock_open(read_data="invalid json")):
        status, body = get("/api/info")
    assert status == 500
    assert body["code"] == 500


def test_info_success():
    with patch("app.services.info.open", mock_open(read_data="[]")):
        status, body = get("/api/info")
    assert status == 200
    assert body["success"] is True
