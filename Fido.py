from fastapi.responses import JSONResponse
from Errors import Errors
from Nisaabyo import Sako, selfinfo
from jawaabo import jawaab
import re

def Fido(amount: int):
    Sako.data_collection(amount)
    reg_exp = r"^\d+$"

    if not re.match(reg_exp, str(amount)):
        return JSONResponse(status_code=464, content=Errors(464))

    if type(amount) != int:
        return JSONResponse(status_code=465, content=Errors(465))

    if int(amount) < Sako.Nisaab_Fidada:
        return JSONResponse(status_code=321, content=Errors(321, True))

    # Zakat calculation
    jw = round(amount / Sako.Dahab_40, 4)
    money = round(jw * selfinfo.Qiimah_fidada_1G, 4)

    requirements = [
        "Must be 100% pure silver.",
        "You must have possessed it for one full year.",
        f"If paying in cash, the amount is {money}$."
    ]

    return JSONResponse(status_code=200, content=jawaab(jw, requirements, "Grams"))
