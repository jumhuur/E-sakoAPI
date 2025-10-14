from Errors import Errors
from Nisaabyo import Sako , selfinfo
from jawaabo import jawaab
import re


def Loa(xadi):
    nisaab = {
    1:40,
    2:60,
    }

    reg_exp = r"^\d+$"
    if re.match(reg_exp, str(xadi)):
        if int(xadi) > Sako.Nisaab_lo and int(xadi) < nisaab[1]:
            jw = 1
            shuruudo = [
                "waa inuu galay sanadkii 2aad (tabiic ama tabiica)".title(),
                "inuu dhedig noqdo ayaa fiican labna waad ku bixin kartaa".title(),
                "waa inuu yahay neef Lo'a ah "
            ]

            return jawaab(jw,shuruudo, "neef")
        elif int(xadi) > nisaab[1] and int(xadi) < nisaab[2]:
            jw = 1
            shuruudo = [
                "waa inuu galay sanadkii 3aad (musina ama )".title(),
                "inuu dhedig noqdo ayaa fiican labna waad ku bixin kartaa".title(),
                "waa inuu yahay neef Lo'a ah "
            ]
            return jawaab(jw,shuruudo, "neef")
        elif int(xadi) > nisaab[1] :
            fiican = None
            sodon = int(xadi) // 30
            afartan = int(xadi) // 40
            for Tabiic in range(sodon + 1):
                for musina in range(afartan + 1):
                    la_daboolay = 30*Tabiic + 40*musina
                    if la_daboolay > int(xadi):
                        continue
                    Hadhaa = int(xadi) - la_daboolay
                    stash = {
                        "Tabiic":Tabiic,
                        "Musina":musina,
                        "la_daboolay":la_daboolay,
                        "Hadhaa": Hadhaa,
                        "Sako":Tabiic + musina
                    }

                    if fiican == None:
                        fiican = stash
                    if stash["Hadhaa"] < fiican["Hadhaa"]:
                        fiican = stash
                    elif stash["Hadhaa"] == fiican["Hadhaa"]:
                        if stash["la_daboolay"] > fiican["la_daboolay"]:
                            fiican = stash
                        elif stash["la_daboolay"] == fiican["la_daboolay"] and stash["Sako"] < fiican["Sako"]:
                            fiican = stash
            if fiican["Tabiic"] > 0 and fiican["Musina"] > 0:
                jw = fiican["Tabiic"] + fiican["Musina"]
                shuruudo = [
                    f"waa in sanad u dhamaaday {fiican["Tabiic"]} neef".title(),
                    f"waa in laba sano u dhamaadeen {fiican["Musina"]} neef",
                    "Waa inay lo'a yihiin lab iyo dhadig labada waa lagu bixin karaa"
                ]
                return jawaab(jw,shuruudo, "neef")
            elif fiican["Tabiic"] > 0 and fiican["Musina"] < 1:
                jw = fiican["Tabiic"]
                shuruudo = [
                    f"waa in sanad u dhamaaday {fiican["Tabiic"]}da neef".title(),
                    "Waa inay Geel yihiin lab iyo dhadig labada waa lagu bixin karaa".title(),
                ]
                return jawaab(jw,shuruudo, "neef")
            elif fiican["Tabiic"] < 1 and fiican["Musina"] > 0:
                jw = fiican["Tabiic"]
                shuruudo = [
                    f"waa in Laba sanadood u dhamaadeen {fiican["Tabiic"]}da neef".title(),
                    "Waa inay Geel yihiin lab iyo dhadig labada waa lagu bixin karaa".title(),
                ]
                return jawaab(jw,shuruudo, "neef")
        else:
            return Errors(324)
    else:
        return Errors(464)