import json
from fastapi.responses import JSONResponse
from Rikaas import Rikaas
from datetime import datetime
from jawaabo import jawaab
from Nisaabyo import Sako



def test_valid_rikas_calc():
    amount = "155"
    response = Rikaas(amount)
    requirements = [
        "Must be pure Rikaas.",
        "Must be inherited or passed down and show its original markings.",
    ]
    expected = JSONResponse(status_code=200, content=jawaab(31, requirements, "Grams"))
    assert json.loads(response.body.decode("utf-8"))["response"] == json.loads(expected.body.decode("utf-8"))["response"]
    assert response.status_code == expected.status_code


def test_invalid_rikaas_amount():
    URL_DOC = "https://esakoapi.org/doc"
    amount = "Testing"
    response = Rikaas(amount)
    expected = JSONResponse(status_code=464, content={
        "code":464,
        "message":f"Please use numbers only Read more details this URL: {URL_DOC} .",
        "ok":False
    })
    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))
    


def test_rikaas_amount_less_then_nisaab():
    amount = "2"
    response = Rikaas(amount)
    expected = JSONResponse(status_code=323, content={
        "code":323,
        "message":f"The amount of rikaas has not reached the Zakat threshold. The Nisaab for rikaas is {round(Sako.Nisaab_Rikaas, 4)} grams.",
        "ok":True
    })
    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))
