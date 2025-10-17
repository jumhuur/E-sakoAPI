import json
from Lacag import Lacag
from fastapi.responses import JSONResponse
from datetime import datetime
date = datetime.now()
Date_format = f"{date.strftime("%A %d-%B-%Y")}"
Time_format = f"{date.strftime("%I:%M %p")}"

def test_mone_valid_cal():
    amount = 12560
    response = Lacag(amount)
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response": 314,
        "requirements": [
        "The amount must be in US dollars 'USD'.",
        "You must have possessed it for one full year.",
        "The Zakat has been calculated based on the gold price of 136.3834 USD per gram."
        ],
        "Unit": "$",
        "date": Date_format,
        "time": Time_format
        }
    )

    res_result = json.loads(response.body.decode("utf-8"))
    exp_result = json.loads(expected.body.decode("utf-8"))
    assert response.status_code == expected.status_code
    assert res_result["response"] == exp_result["response"]


def test_invalid_amount():
    amount = "maxadasdas"
    response = Lacag(amount)
    expected = JSONResponse(status_code=464, content={
        "code": 464,
        "message": "Please use numbers only Read more details this URL: https://esakoapi.org/doc .",
        "ok": False
        }
    )

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))


def test_amount_lessthan_nisaab_gold_and_silver():
    amount = 100
    response = Lacag(amount)
    expected = JSONResponse(status_code=325, content={
        "code": 325,
        "message": "Please use numbers only Read more details this URL: https://esakoapi.org/doc .",
        "ok": False
        }
    )

    assert response.status_code == expected.status_code


def test_amount_less_than_gold_nisab_and_greater_than_silver_nisab():
    amount = 1000
    response = Lacag(amount)
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response": 25,
        "requirements": [
        "The amount must be in US dollars 'USD'.",
        "You must have possessed it for one full year.",
        "The Zakat has been calculated based on the gold price of 136.3834 USD per gram."
        ],
        "Unit": "$",
        "date": Date_format,
        "time": Time_format
        }
    )

    res_result = json.loads(response.body.decode("utf-8"))
    exp_result = json.loads(expected.body.decode("utf-8"))
    assert response.status_code == expected.status_code
    assert res_result["response"] == exp_result["response"]



