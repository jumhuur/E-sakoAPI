from fastapi.responses import JSONResponse
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
    if not re.match(reg_exp, str(xadi)):
        return JSONResponse(status_code=464, content=Errors(464))
    if xadi < Sako.Nisaab_Geel:
        return JSONResponse(status_code=326, content=Errors(326))
    if xadi > Sako.Nisaab_Geel and xadi < nisaab[1]:
        jw = 1
        shuruudo = ["The payment will be livestock (sheep)".title(), 
                    "Sheep must be at least one year old".title(),
                    "Goats must be at least two years old".title(), 
                    "Male and female animals are treated equally".title()
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads" ))
    if xadi >=  nisaab[1] and xadi < nisaab[2]:
        jw = 2
        shuruudo = ["The payment will be livestock (sheep)".title(), 
                    "Sheep must be at least one year old".title(),
                    "Goats must be at least two years old".title(), 
                    "Male and female animals are treated equally".title()
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads"))
    if xadi >=  nisaab[2] and xadi < nisaab[3]:
        jw = 3
        shuruudo = ["The payment will be livestock (sheep)".title(), 
                    "Sheep must be at least one year old".title(),
                    "Goats must be at least two years old".title(), 
                    "Male and female animals are treated equally".title()
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads"))
    elif xadi >=  nisaab[3] and xadi < nisaab[4]:
        jw = 4
        shuruudo = ["The payment will be livestock (sheep)".title(), 
                    "Sheep must be at least one year old".title(),
                    "Goats must be at least two years old".title(), 
                    "Male and female animals are treated equally".title()
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads" ))
    if xadi >=  nisaab[4] and xadi < nisaab[5]:
        jw = 1
        shuruudo = ["The payment will be a camel".title(), 
                    "It must have entered its second year".title(),
                    "It must be female".title(), 
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads" ))
    if xadi >=  nisaab[5] and xadi < nisaab[6]:
        jw = 1
        shuruudo = ["The payment will be a camel".title(), 
                    "It must have entered its third year".title(),
                    "It must be female".title(), 
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads" ))
    if xadi >=  nisaab[6] and xadi < nisaab[7]:
        jw = 1
        shuruudo = ["The payment will be a camel".title(), 
                    "It must have entered its fourth year".title(),
                    "It must be female".title(), 
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads" ))
    if xadi >=  nisaab[6] and xadi < nisaab[7]:
        jw = 2
        shuruudo = ["They must be camels".title(), 
                    "They must have entered their second year".title(),
                    "They must be female".title(), 
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads" ))
    if xadi >=  nisaab[7] and xadi < nisaab[8]:
        jw = 2
        shuruudo = ["They must be camels".title(), 
                    "They must have entered their fourth year".title(),
                    "They must be female".title(), 
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads" ))
    if xadi >=  nisaab[8] and xadi < nisaab[9]:
        jw = 3
        shuruudo = ["They must be camels".title(), 
                    "They must have entered their fifth year".title(),
                    "They must be female".title(), 
                    ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo,"heads" ))
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
                shuruudo = [f"{ugu_fiican["xiqa"]} camels must be three years old".title(), 
                f"{ugu_fiican['labuun']} camels must be two years old".title(),
                "They must be female".title(), 
                ]
                return jawaab(jw, shuruudo, "heads") 
            elif ugu_fiican["xiqa"] > 0 and ugu_fiican["labuun"] < 1:
                jw = ugu_fiican["Sako"]
                shuruudo = [f"{ugu_fiican["xiqa"]} camels must be three years old".title(), 
                "They must be female".title(), 
                ]
                return jawaab(jw, shuruudo, "heads")
            elif ugu_fiican["xiqa"] < 1 and ugu_fiican["labuun"] > 0:
                jw = ugu_fiican["Sako"]
                shuruudo = [f"{ugu_fiican["labuun"]} camels must be two years old".title(), 
                "They must be female".title(), 
                ]
                return jawaab(jw, shuruudo, "heads")