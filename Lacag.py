from fastapi.responses import JSONResponse
from Nisaabyo import Sako , selfinfo
from Errors import Errors
from jawaabo import jawaab
import re
def Lacag(xadi:int):
    reg = r"^\d+$"
    if not re.match(reg, str(xadi)):
        return JSONResponse(status_code=464, content=Errors(464))
    if xadi < selfinfo.Nisaab_lacag_d and xadi < selfinfo.Nisaab_Lacag_f:
        return JSONResponse(status_code=325, content=Errors(325, True))
    if xadi >= selfinfo.Nisaab_lacag_d:
        jw = round(xadi / Sako.Dahab_40, 4)
        shuruud = ["waa inay tahay lacagtu dollar 'USD'".title(),
                    "waa inaad sanad haysay".title(), 
                    f"waxaa lagugu xisaabiyay sakadan qiimaha dahabka oo maraya {round(selfinfo.qiimaha_dahab_24, 4)}".title()
                ]
        return JSONResponse(status_code=200,content=jawaab(jw, shuruud, "$"))
    if xadi >= selfinfo.Nisaab_Lacag_f:
        jw = round(xadi / Sako.Dahab_40, 4)
        shuruud = ["waa inay tahay lacagtu dollar 'USD'".title(), 
                    "waa inaad sanad haysay".title(), 
                    f"waxaa lagugu xisaabiyay sakadan qiimaha fidada oo maraysa {round(selfinfo.Qiimah_fidada_1G, 4)}".title()
                ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruud, "$"))
        

