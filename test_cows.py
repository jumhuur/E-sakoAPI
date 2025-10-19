from fastapi.responses import JSONResponse
from datetime import datetime
from Errors import Errors
from Loa import Loa
from Nisaabyo import Sako
import json
import pytz

local_time = pytz.timezone("Africa/Mogadishu")
date = datetime.now(local_time)
Date_format = f"{date.strftime("%A %d-%B-%Y")}"
Time_format = f"{date.strftime("%I:%M %p")}"
URL_DOC = "https://esakoapi.org/doc"


def test_vali_amount_less_then_60():
    amount = 40
    response = Loa(amount)
    requirements = [
            "It must have entered its third year (Musina or similar)".title(),
            "Female is preferred, but male is also acceptable".title(),
            "It must be a cow".title()
        ]
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response":1,
        "requirements": requirements,
        "Unit": "heads",
        "date": Date_format,
        "time": Time_format
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))


def test_vali_amount_greater_then_60():
    amount = 160   
    # waxaa jita cilada xaga tirada qaar sida 180 waxaa la doonayay in jawaabta noqoto 6 Tabiic
    # laakiin waxa uu ku jawaabayaa 3 tabiic + 2 misino oo isku noqonaya 5
    response = Loa(amount)
    requirements = [
                f"4 cows must be at least two years old".title(),
                "They must be cows, male or female both are acceptable".title()
            ]
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response":4,
        "requirements": requirements,
        "Unit": "heads",
        "date": Date_format,
        "time": Time_format

    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))


def test_invalid_amount():
    amount = "invalid"
    response = Loa(amount)
    expected = JSONResponse(status_code=464, content=Errors(464))

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))



def test_if_amount_less_then_nisab():
    amount = 4
    response = Loa(amount)
    expected = JSONResponse(status_code=324, content={
        "code":324, 
        "message": f"The number of cows you entered has not reached the Zakat threshold. The Nisaab for cows is {Sako.Nisaab_lo} heads.",
        "ok": False
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))


