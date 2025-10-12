from Nisaabyo import Sako , selfinfo
from Errors import Errors
from jawaabo import jawaab
import re
def Lacag(Nooc:str,xadi:int):
    reg = r"^\d+$"
    route_regx = r"^(lacag)$"
    if re.match(route_regx, Nooc):
        if re.match(reg, str(xadi)):
            if xadi >= selfinfo.Nisaab_lacag_d or xadi >= selfinfo.Nisaab_Lacag_f:
                if xadi >= selfinfo.Nisaab_lacag_d:
                    jw = round(xadi / Sako.Dahab_40, 4)
                    return jawaab(jw, ["waa inay tahay lacagtu dollar 'USD'".title(), "waa inaad sanad haysay".title(), f"waxaa lagugu xisaabiyay sakadan qiimaha dahabka oo maraya {round(selfinfo.qiimaha_dahab_24, 4)}"], "$")
                if xadi >= selfinfo.Nisaab_Lacag_f:
                    jw = round(xadi / Sako.Dahab_40, 4)
                    return jawaab(jw, ["waa inay tahay lacagtu dollar 'USD'".title(), "waa inaad sanad haysay".title(), f"waxaa lagugu xisaabiyay sakadan qiimaha fidada oo maraysa {round(selfinfo.Qiimah_fidada_1G, 4)}"], "$")
            else:
                return Errors(325, True)
        else:
            return Errors(464)
    else:
        return Errors(467)