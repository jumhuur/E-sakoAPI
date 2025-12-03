from fastapi.responses import JSONResponse
from Nisaabyo import Sako
import re
from Errors import Errors
from jawaabo import jawaab
from  Gold_silver_price import Price_24_1g
def saafi(nooc: int,xadiga: int) -> int: 
    """
    istikhlaas ayaa loo yaqaanaa hawsha function waxana ay ka dhigantahay 
    in la soo saaro noocyada kala duwan ee dahabka mid walba inta uu ka yahay saafi 
    Tusaale nooca 24 waa safi 100% laakiin 22,21,20,18,16 dhamaantood noocyadan maaha saafi 
    sidaas darteed si loo xisaabiyo sakada ka baxaysa waa in la ogaado xadiga la xisaabinya ee ka tirsan
    tusaale ahaan nooca 22-ka ah inta uu saafi ka yahay sidan hoose oo kale 
    145-giraam oo dahab ah nooca 22-ka intee dahab saafi ah 145-kaas marka la eego 
    shaqadaas ayaa halkan lagu qabanaya
    """
    result = (xadiga * nooc) / Sako.Noocyo["24"]
    return result


def xisaab_Dahab(xadiga:int, nooc: int):
    g_24, _, _,_, = Price_24_1g().values()
    Sako.data_collection(xadiga, nooc, sako="Dahab")
    reg = r"^\d{2}$"
    reg_exp = r"^\d+$"
    if not re.match(reg_exp, str(xadiga)):
        return JSONResponse(status_code=461, content=Errors(461))
    if not re.match(reg, str(nooc)):
        return JSONResponse(status_code=465, content=Errors(465))
    grams = []
    for n_key, n_value in Sako.Noocyo.items():
        grams.append(n_value)

    if nooc not in grams:
        return JSONResponse(status_code=463, content=Errors(463))

    # if type(xadiga) != int:
    #     return JSONResponse(status_code=461, content=Errors(461))
    if int(xadiga) < Sako.Nisaab_dahab:
        return JSONResponse(status_code=320, content=Errors(320, True))
        # The actual calculation starts here
    if nooc == Sako.Noocyo["24"]:
        jw = round(int(xadiga) / Sako.Dahab_40, 4)
        usd_price = round(jw * g_24, 4)
        conditions = [
                    "It must be 100% pure gold.",
                    "You must have possessed it for one full year.",
                    f"If you are paying in cash, the amount is {usd_price}$."
                ]
        return JSONResponse(
            status_code=200,
            content=jawaab(
                jw,
                conditions
                ,
                "Grams"
            )
        )

    if nooc == Sako.Noocyo["22"]:
        d_saafi = saafi(nooc, int(xadiga))
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * g_24, 4)
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
        d_saafi = saafi(nooc, int(xadiga))
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * g_24, 4)
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
        d_saafi = saafi(nooc, int(xadiga))
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * g_24, 4)
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
        d_saafi = saafi(nooc, int(xadiga))
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * g_24, 4)
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
        d_saafi = saafi(nooc, int(xadiga))
        if d_saafi >= Sako.Nisaab_dahab:
            jw = round(d_saafi / Sako.Dahab_40, 4)
            usd_price = round(jw * g_24, 4)
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
