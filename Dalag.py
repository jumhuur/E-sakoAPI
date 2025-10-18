import re
from Errors import Errors
from fastapi.responses import JSONResponse
from Nisaabyo import Sako, selfinfo
from jawaabo import jawaab


def Dalag(quantity: int, option: int):
    Sako.data_collection(quantity,option)
    rates = {1: 1/10, 2: 1/20, 3: 3/40}  # 10%, 5%, 7.5%
    valid_options = {1, 2, 3}
    reg_exp = r"^\d+$"

    if not re.match(reg_exp, str(quantity)):
        return JSONResponse(status_code=464, content=Errors(464))

    if not re.match(reg_exp, str(option)):
        return JSONResponse(status_code=464, content=Errors(464))

    if int(option) not in valid_options:
        return JSONResponse(status_code=468, content=Errors(468))


    if int(quantity) < Sako.Nisaab_Midhaha:
        return JSONResponse(status_code=327, content=Errors(327))

    # Calculate Zakat amount
    jw = int(quantity) * rates[int(option)]


    if int(option) == 1:
        requirements = [
            "Must be rain-fed crops.",
            "Must be harvested and storable (e.g., wheat, rice, or maize)."
        ]
    elif int(option) == 2:
        requirements = [
            "Must be irrigated crops cultivated with paid water.",
            "Must be harvested and storable (e.g., wheat, rice, or maize)."
        ]
    else:
        requirements = [
            "Must be crops grown with a combination of rain and paid irrigation.",
            "Must be harvested and storable (e.g., wheat, rice, or maize)."
        ]

    return JSONResponse(status_code=200, content=jawaab(jw, requirements, "Kg"))
