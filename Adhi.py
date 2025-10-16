from Errors import Errors
from Nisaabyo import Sako, selfinfo
from jawaabo import jawaab
from fastapi.responses import JSONResponse

import re

def Adhi(quantity):
    Sako.data_collection(quantity)
    # Zakat thresholds for sheep
    nisaab = {
        1: 120,
        2: 200,
        3: 300,
        4: 400
    }

    # Validate that the input is numeric
    reg_exp = r"^\d+$"
    if not re.match(reg_exp, str(quantity)):
        return JSONResponse(
            status_code=200,
            content=Errors(464)
        )

    # Check if the quantity meets the minimum Zakat threshold
    if int(quantity) < Sako.Nisaab_adhi:
        return JSONResponse(
            status_code=322,
            content=Errors(322)
        )

    # Determine Zakat due based on quantity ranges
    if int(quantity) >= Sako.Nisaab_adhi and int(quantity) <= nisaab[1]:
        jw = 1
        requirements = [
            "If they are sheep, they must be one year old.",
            "If they are Goats, they must be at least 2 years old."
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, requirements, "heads")
        )

    if int(quantity) > nisaab[1] and int(quantity) <= nisaab[2]:
        jw = 2
        requirements = [
            "If they are sheep, they must be one year old.",
            "If they are Goats, they must be at least 2 years old."
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, requirements, "heads")
        )

    if int(quantity) > nisaab[2] and int(quantity) <= nisaab[3]:
        jw = 3
        requirements = [
            "If they are sheep, they must be one year old.",
            "If they are Goats, they must be at least 2 years old."
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, requirements, "heads")
        )

    if int(quantity) > nisaab[3] and int(quantity) < nisaab[4]:
        jw = 4
        requirements = [
            "If they are sheep, they must be one year old.",
            "If they are Goats, they must be at least 2 years old."
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, requirements, "heads")
        )

    if int(quantity) >= nisaab[4]:
        jw = int(quantity) // 100
        requirements = [
            "If they are sheep, they must be one year old.",
            "If they are Goats, they must be at least 2 years old."
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, requirements, "heads")
        )


