from Errors import Errors
from Nisaabyo import Sako
from jawaabo import jawaab
import re


def Geel(xadi:int):
    nisaab = {
        1:10,
        2:15,
        3:20,
        4:25,
        5:36,
        6:46,
        7:76,
        8:91,
        9:121
    }
    reg_exp = r"^\d+$"
    if re.match(reg_exp, str(xadi)):
        if xadi >= Sako.Nisaab_Geel:
            if xadi > Sako.Nisaab_Geel and xadi < nisaab[1]:
                jw = 1
                shuruudo = ["Waxa La bixinayaa waa Adhi".title(), 
                            "Ido waa in sanad u dhaamday".title(),
                            "riyo waa in laba sano u dhaamdeen".title(), 
                            "lab iyo dhedig waa isku mid".title()
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi >=  nisaab[1] and xadi < nisaab[2]:
                jw = 2
                shuruudo = ["Waxa La bixinayaa waa Adhi".title(), 
                            "Ido waa in sanad u dhaamday".title(),
                            "riyo waa in laba sano u dhaamdeen".title(), 
                            "lab iyo dhedig waa isku mid".title()
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi >=  nisaab[2] and xadi < nisaab[3]:
                jw = 3
                shuruudo = ["Waxa La bixinayaa waa Adhi".title(), 
                            "Ido waa in sanad u dhaamday".title(),
                            "riyo waa in laba sano u dhaamdeen".title(), 
                            "lab iyo dhedig waa isku mid".title()
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi >=  nisaab[3] and xadi < nisaab[4]:
                jw = 4
                shuruudo = ["Waxa La bixinayaa waa Adhi".title(), 
                            "Ido waa in sanad u dhaamday".title(),
                            "riyo waa in laba sano u dhaamdeen".title(), 
                            "lab iyo dhedig waa isku mid".title()
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi >=  nisaab[4] and xadi < nisaab[5]:
                jw = 1
                shuruudo = ["Waxa La bixinayaa waa Geel".title(), 
                            "Waa inuu Galay sanadkii 2aad".title(),
                            "waa inuu yahay dhedig".title(), 
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi >=  nisaab[5] and xadi < nisaab[6]:
                jw = 1
                shuruudo = ["Waxa La bixinayaa waa Geel".title(), 
                            "Waa inuu Galay sanadkii 3aad".title(),
                            "waa inuu yahay dhedig".title(), 
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi >=  nisaab[6] and xadi < nisaab[7]:
                jw = 1
                shuruudo = ["Waxa La bixinayaa waa Geel".title(), 
                            "Waa inuu Galay sanadkii 4aad".title(),
                            "waa inuu yahay dhedig".title(), 
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi >=  nisaab[6] and xadi < nisaab[7]:
                jw = 2
                shuruudo = ["Waa Inay Geel Yihiin".title(), 
                            "waa inay galeen sanadkii 2aad".title(),
                            "waa inay dhedig yihiin".title(), 
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi >=  nisaab[7] and xadi < nisaab[8]:
                jw = 2
                shuruudo = ["Waa Inay Geel Yihiin".title(), 
                            "waa inay galeen sanadkii 4aad".title(),
                            "waa inay dhedig yihiin".title(), 
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi >=  nisaab[8] and xadi < nisaab[9]:
                jw = 3
                shuruudo = ["Waa Inay Geel Yihiin".title(), 
                            "waa inay galeen sanadkii 5aad".title(),
                            "waa inay dhedig yihiin".title(), 
                            ]
                return jawaab(jw, shuruudo,"Neef" )
            elif xadi > nisaab[9]:
                ugu_fiican = None
                khamsiin = xadi // 50
                arbaciin = xadi // 40
                for xiqa in range(khamsiin + 1):
                    for labuun in range(arbaciin +1):
                        la_daboolay = 50*xiqa + 40*labuun
                        if la_daboolay > xadi:
                            continue
                        Hadhaa = xadi - la_daboolay
                        stash = {
                            "xiqa":xiqa,
                            "labuun":labuun,
                            "la_daboolay": la_daboolay,
                            "Hadhaa": Hadhaa,
                            "Sako": xiqa + labuun
                        }
                        if ugu_fiican == None:
                            ugu_fiican = stash
                        if stash["Hadhaa"] < ugu_fiican["Hadhaa"]:
                            ugu_fiican = stash
                        elif stash["Hadhaa"] == ugu_fiican["Hadhaa"]:
                            if stash["la_daboolay"] > ugu_fiican["la_daboolay"]:
                                ugu_fiican = stash
                            elif stash["la_daboolay"] == ugu_fiican["la_daboolay"] and stash["Sako"] < ugu_fiican["Sako"]:
                                ugu_fiican = stash
                if ugu_fiican["xiqa"] > 0 and  ugu_fiican["labuun"] > 0:
                    jw = ugu_fiican["Sako"]
                    shuruudo = [f"Waa in {ugu_fiican["xiqa"]} halaad ay 3 sano yihiin".title(), 
                    f"waa in {ugu_fiican['labuun']} Halaad laba jir yihiin".title(),
                    "waa inay dhedig yihiin".title(), 
                    ]
                    return jawaab(jw, shuruudo, "neef") 
                elif ugu_fiican["xiqa"] > 0 and ugu_fiican["labuun"] < 1:
                    jw = ugu_fiican["Sako"]
                    shuruudo = [f"Waa in {ugu_fiican["xiqa"]} halaad ay 3 sano yihiin".title(), 
                    "waa inay dhedig yihiin".title(), 
                    ]
                    return jawaab(jw, shuruudo, "neef")
                elif ugu_fiican["xiqa"] < 1 and ugu_fiican["labuun"] > 0:
                    jw = ugu_fiican["Sako"]
                    shuruudo = [f"Waa in {ugu_fiican["labuun"]} halaad ay 2 sano yihiin".title(), 
                    "waa inay dhedig yihiin".title(), 
                    ]
                    return jawaab(jw, shuruudo, "neef") 
        else:
            return Errors(326)
    else: 
        return Errors(464)