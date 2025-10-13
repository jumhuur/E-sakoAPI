import re
from Errors import Errors
from fastapi.responses import JSONResponse
from Nisaabyo import Sako , selfinfo
from jawaabo import jawaab

def Dalag(xadi: int, nooc: int):
    qaab = {1: 1/10, 2: 1/20, 3: 3/40}  # 10%, 5%, 7.5%
    options = {1,2,3}
    reg_exp = r"^\d+$"
    if not re.match(reg_exp, str(xadi)):
        return JSONResponse(status_code=464, content=Errors(464))

    if int(nooc) not in options:
        return JSONResponse(status_code=468, content=Errors(468))

    if int(xadi) < Sako.Nisaab_Midhaha:
        return JSONResponse(status_code=327, content=Errors(327))

    jw = int(xadi) * qaab[int(nooc)]
    if int(nooc) == 1:
        shuruudo = [
            "Dalag roob ku baxay".title(),
            "Waa in la goostay dalag kaydsan sida hadhuudh, bariis, ama galley".title(),
        ]
    elif int(nooc) == 2:
        shuruudo = [
            "Dalag lagu waraabiyay biyo lacag lagu bixiyay".title(),
            "Waa in la goostay dalag kaydsan sida hadhuudh, bariis, ama galley".title(),
        ]
    else:
        shuruudo = [
            "Dalag ku baxay biyo roob iyo biyo lacag lagu bixiyay oo isku jira".title(),
            "Waa in la goostay dalag kaydsan sida hadhuudh, bariis, ama galley".title(),
        ]

    return JSONResponse(status_code=200, content=jawaab(jw, shuruudo, "Kg"))


# qaabab = {1,2.3}
# if 6 not in qaabab:
#     print("ok")
# else:
#     print("no")