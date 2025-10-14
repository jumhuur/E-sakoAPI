from fastapi.responses import JSONResponse
from Nisaabyo import Sako, selfinfo
import re
from Errors import Errors
from jawaabo import jawaab


def saafi(nooc: int, xadiga: int) -> int:
    result = (xadiga * nooc) / Sako.Noocyo["24"]
    return result


def xisaab_Dahab(nooc: int, xadiga: float):
    reg = r"^\d{2}$"
    if not re.match(reg, str(nooc)):
        return JSONResponse(status_code=465, content=Errors(465))
    grams = []
    for n_key, n_value in Sako.Noocyo.items():
        grams.append(n_value)

    if nooc not in grams:
        return JSONResponse(status_code=463, content=Errors(463))

    if type(xadiga) != float:
        return JSONResponse(status_code=461, content=Errors(461))
    if xadiga < Sako.Nisaab_dahab:
        return JSONResponse(status_code=320, content=Errors(320, True))
        # The actual calculation starts here
    if nooc == Sako.Noocyo["24"]:
        jw = round(xadiga / Sako.Dahab_40, 4)
        usd_price = round(jw * selfinfo.qiimaha_dahab_24, 4)
        return JSONResponse(
            status_code=200,
            content=jawaab(
                jw,
                [
                    "It must be 100% pure gold.",
                    "You must have possessed it for one full year.",
                    f"If you are paying in cash, the amount is {usd_price}$."
                ],
                "Grams"
            )
        )

    if nooc == Sako.Noocyo["22"]:
        d_saafi = saafi(nooc, xadiga)
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * selfinfo.qiimaha_dahab_24, 4)
            return JSONResponse(
                status_code=200,
                content=jawaab(
                    jw,
                    [
                        f"It must be {nooc}-karat gold.",
                        "You must have possessed it for one full year.",
                        f"If you are paying in cash, the amount is {usd_price}$."
                    ],
                    "Grams"
                )
            )
        else:
            return Errors(466, True)

    if nooc == Sako.Noocyo["21"]:
        d_saafi = saafi(nooc, xadiga)
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * selfinfo.qiimaha_dahab_24, 4)
            return JSONResponse(
                status_code=200,
                content=jawaab(
                    jw,
                    [
                        f"It must be {nooc}-karat gold.",
                        "You must have possessed it for one full year.",
                        f"If you are paying in cash, the amount is {usd_price}$."
                    ],
                    "Grams"
                )
            )
        else:
            return Errors(466, True)

    if nooc == Sako.Noocyo["20"]:
        d_saafi = saafi(nooc, xadiga)
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * selfinfo.qiimaha_dahab_24, 4)
            return JSONResponse(
                status_code=200,
                content=jawaab(
                    jw,
                    [
                        f"It must be {nooc}-karat gold.",
                        "You must have possessed it for one full year.",
                        f"If you are paying in cash, the amount is {usd_price}$."
                    ],
                    "Grams"
                )
            )
        else:
            return Errors(466, True)

    if nooc == Sako.Noocyo["18"]:
        d_saafi = saafi(nooc, xadiga)
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * selfinfo.qiimaha_dahab_24, 4)
            return JSONResponse(
                status_code=200,
                content=jawaab(
                    jw,
                    [
                        f"It must be {nooc}-karat gold.",
                        "You must have possessed it for one full year.",
                        f"If you are paying in cash, the amount is {usd_price}$."
                    ],
                    "Grams"
                )
            )
        else:
            return Errors(466, True)

    if nooc == Sako.Noocyo["16"]:
        d_saafi = saafi(nooc, xadiga)
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * selfinfo.qiimaha_dahab_24, 4)
            return JSONResponse(
                status_code=200,
                content=jawaab(
                    jw,
                    [
                        f"It must be {nooc}-karat gold.",
                        "You must have possessed it for one full year.",
                        f"If you are paying in cash, the amount is {usd_price}$."
                    ],
                    "Grams"
                )
            )
        else:
            return Errors(466, True)
