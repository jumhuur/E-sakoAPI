from Errors import Errors
from Nisaabyo import Sako, selfinfo
from jawaabo import jawaab
import re
def Fido(xadi:int):
    reg_exp = r"^\d+$"
    if re.match(reg_exp, str(xadi)):
        if type(xadi) == int:
            if xadi >= Sako.Nisaab_Fidada:
                # Xisaabin 
                jw = round(xadi / Sako.Dahab_40,4)
                lacag = round(jw * selfinfo.Qiimah_fidada_1G, 4)
                return jawaab(jw, ["waa inay tahay Fido Saafi ah 100%".title(), "waa inaad sanad haysay".title(), f"Lacag Hadaad ku bixinayso waxay noqonaysaa {lacag}$"], "Giraam")
            else:
                return Errors(321, True)
        else:
            return Errors(465)
    else:
            return(464)


