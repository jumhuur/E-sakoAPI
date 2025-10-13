from Errors import Errors
from Nisaabyo import Sako ,selfinfo
from jawaabo import jawaab
from fastapi.responses import JSONResponse

import re

def Adhi(xadi):
    nisaab = {
    1:120,
    2:200,
    3:300,
    4:400
    }
    reg_exp = r"^\d+$"
    if not re.match(reg_exp, str(xadi)):
        return JSONResponse(
            status_code=200,
            content=Errors(464)
        )
    if int(xadi) < Sako.Nisaab_adhi:
        return JSONResponse(
            status_code=322,
            content=Errors(322)
        )
    if int(xadi) >= Sako.Nisaab_adhi and int(xadi) <= nisaab[1]:
        jw = 1
        shuruudo = [
            "Haduu yahay Ido waa in sanad u buuxsamay".title(),
            "Haduu Yahay Riyo waa in uu gaadhay 2 sano ".title(),
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, shuruudo, "neef")
        )
  
    if int(xadi) > nisaab[1] and int(xadi) <= nisaab[2]:
        jw = 2
        shuruudo = [
            "Haday Ido yihiin waa in sanad u buuxsamay".title(),
            "Haday Riyo Yihiin waa in ay gaadheen 2 sano".title(),
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, shuruudo, "neef")
        )
    if int(xadi) > nisaab[2] and int(xadi) <= nisaab[3]:
        jw = 3
        shuruudo = [
            "Haday Ido yihiin waa in sanad u buuxsamay".title(),
            "Haday Riyo Yihiin waa in ay gaadheen 2 sano".title(),
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, shuruudo, "neef")
        )
    if int(xadi) > nisaab[3] and int(xadi) < nisaab[4]:
        jw = 4
        shuruudo = [
            "Haday Ido yihiin waa in sanad u buuxsamay".title(),
            "Haday Riyo Yihiin waa in ay gaadheen 2 sano".title(),
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, shuruudo, "neef")
        )
    if int(xadi) >= nisaab[4]:
        jw = int(xadi) // 100
        shuruudo = [
            "Haday Ido yihiin waa in sanad u buuxsamay".title(),
            "Haday Riyo Yihiin waa in ay gaadheen 2 sano".title(),
        ]
        return JSONResponse(
            status_code=200,
            content=jawaab(jw, shuruudo, "neef")
        )

