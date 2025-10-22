from fastapi.responses import JSONResponse
from Fido import Fido
from Nisaabyo import Sako
from jawaabo import jawaab
import json


def test_Silver_sakat_calc():
    amount = "999"
    requirements = [
        "Must be 100% pure silver.",
        "You must have possessed it for one full year.",
        # f"If paying in cash, the amount is {money}$."
    ]
    response = Fido(amount)
    expected = JSONResponse(status_code=200, content=jawaab(24.975,requirements, "Grams"))
    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8"))["response"] == json.loads(expected.body.decode("utf-8"))["response"]


def test_invalid_silver_amount():
    URL_DOC = "https://esakoapi.org/doc"
    amount = "invalidamount"
    response = Fido(amount)
    expected = JSONResponse(status_code=464, content={
        "code": 464,
        "message": f"Please use numbers only Read more details this URL: {URL_DOC} .",
        "ok" :False
    })
    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))


def test_silver_amount_less_then_nisaab():
    amount = "7"
    response = Fido(amount)
    expected = JSONResponse(status_code=321, content={
        "code": 321,
        "message": f"The amount of silver has not reached the Zakat threshold. The Nisaab for silver is {round(Sako.Nisaab_Fidada, 4)} grams.",
        "ok" :True
    })
    assert response.status_code == expected.status_code
    assert json.loads(response.body.decode("utf-8")) == json.loads(expected.body.decode("utf-8"))
