from fastapi.responses import JSONResponse
from datetime import datetime
import pytz
from Dalag import Dalag
import json
from Nisaabyo import Sako
from Errors import Errors
local_time = pytz.timezone("Africa/Mogadishu")
date = datetime.now(local_time)
Date_format = f"{date.strftime("%A %d-%B-%Y")}"
Time_format = f"{date.strftime("%I:%M %p")}"
URL_DOC = "https://esakoapi.org/doc"

def test_valid_calc_crops_op_1():
    amount = "990"
    option = "1"
    requirements = [
            "Must be rain-fed crops.",
            "Must be harvested and storable (e.g., wheat, rice, or maize)."
    ]
    response = Dalag(amount, option)
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response":99,
        "requirements" :requirements,
        "Unit":"Kg",
        "date":Date_format,
        "time":Time_format
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))



def test_valid_calc_crops_op_2():
    amount = "990"
    option = "2"
    requirements = [
            "Must be irrigated crops cultivated with paid water.",
            "Must be harvested and storable (e.g., wheat, rice, or maize)."
    ]
    response = Dalag(amount, option)
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response":49.5,
        "requirements" :requirements,
        "Unit":"Kg",
        "date":Date_format,
        "time":Time_format
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))


def test_valid_calc_crops_op_3():
    amount = "990"
    option = "3"
    requirements = [
            "Must be crops grown with a combination of rain and paid irrigation.",
            "Must be harvested and storable (e.g., wheat, rice, or maize)."
        ]
    response = Dalag(amount, option)
    expected = JSONResponse(status_code=200, content={
        "code": 200,
        "response":74.25,
        "requirements" :requirements,
        "Unit":"Kg",
        "date":Date_format,
        "time":Time_format
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))




def test_invalid_amount_crops():
    amount = "invalid"
    option = "3"
    response = Dalag(amount, option)
    expected = JSONResponse(status_code=464, content={
        "code": 464,
        "message": f"Please use numbers only Read more details this URL: {URL_DOC} .",
        "ok": False
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))

def test_if_option_is_str():
    amount = "990"
    option = "invalid"
    response = Dalag(amount, option)
    expected = JSONResponse(status_code=464, content={
        "code": 464,
        "message": f"Please use numbers only Read more details this URL: {URL_DOC} .",
        "ok": False
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))


def test_if_option_int_but_is_valid():
    amount = "990"
    option = "22"
    response = Dalag(amount, option)
    expected = JSONResponse(status_code=468, content={
        "code": 468,
        "message": f"The calculation type you requested is invalid. Accepted types are 1, 2, or 3. Read more details here: {URL_DOC}",
        "ok": False
    })

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))

def test_crop_amount_less_then_crop_nisab_response():
    amount = "200"
    option = "1"
    response = Dalag(amount, option)
    expected = JSONResponse(status_code=327, content=Errors(327))

    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))
