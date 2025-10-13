from fastapi.responses import JSONResponse
from Errors import Errors
from Nisaabyo import Sako, selfinfo
from jawaabo import jawaab
import re
def Rikaas(xadi:int):
    reg_exp = r"^\d+$"
    if not re.match(reg_exp, str(xadi)):
        return JSONResponse(status_code=464, content=Errors(464))
    if xadi < Sako.Nisaab_Rikaas:
        return JSONResponse(status_code=323, content=Errors(323, True))
    # Xisaabin 
    jw = round(xadi / 5,4)
    lacag = round(jw * selfinfo.qiimaha_dahab_24, 4)
    shuruud = ["waa inay tahay Rikaas".title(), 
                "Waa Inuu Yahaya Wax Dadkii Inaga Horeeyay Aaseen Ayna Ka Muuqayto Calaamadahodii".title(), 
                f"Lacag Hadaad ku bixinayso waxay noqonaysaa {lacag}$"
            ]
    return jawaab(jw, shuruud, "Giraam")
        
        