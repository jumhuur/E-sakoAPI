from fastapi.responses import JSONResponse
from datetime import datetime
from Geel import Geel
from Nisaabyo import Sako
import json
import pytest

date = datetime.now()
Date_format = f"{date.strftime("%A %d-%B-%Y")}"
Time_format = f"{date.strftime("%I:%M %p")}"


# @pytest.fixture
# def amount_cases():
#     invalida_amount = "amsadhsa"
#     valid_amount = 160
#     return {
#         "valid":valid_amount,
#         "invalid":invalida_amount
#     }

def test_valid_amount_and_nisab():
    amount = 55
    response = Geel(amount)
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response": 1,
        "requirements": [
        "The Payment Will Be A Camel",
        "It Must Have Entered Its Fourth Year",
        "It Must Be Female"
        ],
        "Unit": "heads",
        "date": Date_format,
        "time": Time_format
    })

    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))

def test_invalid_amount():
    amount = "maxamad"
    response = Geel(amount)
    expected = JSONResponse(status_code=464, content={
        "code": 464,
        "message": f"Please use numbers only Read more details this URL: https://esakoapi.org/doc .",
        "ok": False
    })

    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))


def test_if_nisab_greater_than_121_head():
    amount = 160
    response = Geel(amount)
    req = [f"4 camels must be two years old".title(), 
        "They must be female".title(), 
        ]
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response": 4,
        "requirements": req,
        "Unit": "heads",
        "date": Date_format,
        "time": Time_format
    })

    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))



def test_amount_less_then_nisaab():
    amount = 3
    response = Geel(amount)
    expected = JSONResponse(status_code=326, content={
        "code": 326,
        "message": f"The number of camels you entered has not reached the Zakat threshold. The Nisaab for camels is {Sako.Nisaab_Geel} heads.",
        "ok": False
    })

    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))
    

