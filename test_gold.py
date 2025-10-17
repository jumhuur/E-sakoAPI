import json
from fastapi.responses import JSONResponse
from Dahab import xisaab_Dahab
from datetime import datetime


date = datetime.now()
Date_format = f"{date.strftime("%A %d-%B-%Y")}"
Time_format = f"{date.strftime("%I:%M %p")}"

def test_check_if_gold_calc():
    amount = 124
    Type = 24
    result = xisaab_Dahab(amount,Type)
    expected  = JSONResponse(status_code=200, content={
        "code": 200,
         "response": 3.1,
        "requirements": [
            "It must be 100% pure gold.", 
            "You must have possessed it for one full year.", 
            "If you are paying in cash, the amount is 433.0741$."
             ], 
        "Unit": "Grams", 
        "date": Date_format, 
        "time": Time_format
    })

    coming_data = json.loads(result.body.decode("utf-8"))
    expected_data = json.loads(expected.body.decode("utf-8"))

    assert result.status_code == expected.status_code
    assert coming_data["response"] == expected_data["response"]
    assert coming_data["Unit"] == expected_data["Unit"]
    assert coming_data["date"] == expected_data["date"]
    assert coming_data["time"] == expected_data["time"]
    # assert coming_data["requirements"] == expected_data["requirements"]


def test_check_invalid_amount():
    amount = "asdsa"
    Type = 24
    Expected =JSONResponse(status_code=200, content={
        "code": 461,
        "message": "Please enter a valid numeric amount Read more details this URL: https://esakoapi.org/doc.",
        "ok": False}
    )
    result = xisaab_Dahab(amount,Type)
    assert json.loads(result.body.decode("utf-8")) == json.loads(Expected.body.decode("utf-8"))


def test_check_invalid_Type():
    amount = 100
    Types = {24,22,21,20,18,16}
    Type = 66
    Expected = JSONResponse(status_code=463, content={
        "code": 463,
        "message": "The selected type is not among the recognized gold types Read more details this URL: https://esakoapi.org/doc.",
        "ok": False
    })
    result = xisaab_Dahab(amount,Type)

    assert  Type not in Types
    assert  json.loads(result.body.decode("utf-8")) == json.loads(Expected.body.decode("utf-8"))


