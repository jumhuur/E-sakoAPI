from fastapi.responses import JSONResponse
from Errors import Errors
from Nisaabyo import Sako, selfinfo
from jawaabo import jawaab
import re

def Rikaas(amount: int):
    Sako.data_collection(amount)
    reg_exp = r"^\d+$"
    if not re.match(reg_exp, str(amount)):
        return JSONResponse(status_code=464, content=Errors(464))

    if int(amount) < Sako.Nisaab_Rikaas:
        return JSONResponse(status_code=323, content=Errors(323, True))

    # Zakat calculation
    jw = round(amount / 5, 4)
    money = round(jw * selfinfo.qiimaha_dahab_24, 4)

    requirements = [
        "Must be pure Rikaas.",
        "Must be inherited or passed down and show its original markings.",
        f"If paying in cash, the amount is {money}$."
    ]

    return JSONResponse(status_code=200,content=jawaab(jw, requirements, "Grams"))
