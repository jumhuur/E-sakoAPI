from fastapi.responses import JSONResponse
from Errors import Errors
from Nisaabyo import Sako, selfinfo
from jawaabo import jawaab
import re
def Fido(xadi:int):
    reg_exp = r"^\d+$"
    if not re.match(reg_exp, str(xadi)):
        return JSONResponse(status_code=464, content= Errors(464))
    if type(xadi) != int:
        return JSONResponse(status_code=465, content=Errors(465))
    if xadi < Sako.Nisaab_Fidada:
        return JSONResponse(status_code=321, content=Errors(321, True))
    # Xisaabin 
    jw = round(xadi / Sako.Dahab_40,4)
    lacag = round(jw * selfinfo.Qiimah_fidada_1G, 4)
    shuruudo = ["waa inay tahay Fido Saafi ah 100%".title(), 
                "waa inaad sanad haysay".title(), 
                f"Lacag Hadaad ku bixinayso waxay noqonaysaa {lacag}$"]
    return JSONResponse(status_code=200, content=jawaab(jw, shuruudo, "Giraam"))

        
        


