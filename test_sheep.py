from fastapi.responses import JSONResponse
from datetime import datetime
from Adhi import Adhi
from Nisaabyo import Sako
import json
import re
import pytz


local_time = pytz.timezone("Africa/Mogadishu")
date = datetime.now(local_time)
Date_format = f"{date.strftime("%A %d-%B-%Y")}"
Time_format = f"{date.strftime("%I:%M %p")}"
URL_DOC = "https://esakoapi.org/doc"

def test_valid_amount_response():
    amount = "56"
    response = Adhi(amount)
    requirements = [
    "If they are sheep, they must be one year old.",
    "If they are Goats, they must be at least 2 years old."
    ]
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response": 1,
        "requirements":requirements,
        "date":Date_format,
        "time":Time_format ,
        "Unit": "heads"
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))




def test_invalid_amount_response():
    amount = "invalid"
    response = Adhi(amount)
    expected = JSONResponse(status_code=464, content={
        "code": 464,
        "message": f"Please use numbers only Read more details this URL: {URL_DOC} .",
        "ok": False
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))



def test_if_amount_greater_then_400_heead():
    amount = "440"
    response = Adhi(amount)
    requirements = [
            "If they are sheep, they must be one year old.",
            "If they are Goats, they must be at least 2 years old."
    ]
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response": 4,
        "requirements":requirements,
        "date":Date_format,
        "time":Time_format ,
        "Unit": "heads"
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))


def test_if_amount_less_then_nisab():
    amount = "20"
    response = Adhi(amount)
    expected = JSONResponse(status_code=322, content={
        "code": 322,
        "message": f"The number of sheep you entered has not reached the Zakat threshold. The Nisaab for sheep is {Sako.Nisaab_adhi} heads.",
        "ok": False
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))
