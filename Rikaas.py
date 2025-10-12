from Errors import Errors
from Nisaabyo import Sako, selfinfo
from jawaabo import jawaab
import re
def Rikaas(xadi:int):
    reg_exp = r"^\d+$"
    if re.match(reg_exp, str(xadi)):
        if xadi >= Sako.Nisaab_Rikaas:
            # Xisaabin 
            jw = round(xadi / 5,4)
            lacag = round(jw * selfinfo.qiimaha_dahab_24, 4)
            return jawaab(jw, ["waa inay tahay Rikaas".title(), "Waa Inuu Yahaya Wax Dadkii Inaga Horeeyay Aaseen Ayna Ka Muuqayto Calaamadahodii".title(), f"Lacag Hadaad ku bixinayso waxay noqonaysaa {lacag}$"], "Giraam")
        else:
            return Errors(323, True)
    else:
        return(464)