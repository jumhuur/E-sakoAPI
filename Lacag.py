from fastapi.responses import JSONResponse
from Nisaabyo import Sako, selfinfo
from Errors import Errors
from jawaabo import jawaab
import re

def Lacag(amount: int):
    Sako.data_collection(amount)
    reg = r"^\d+$"
    if not re.match(reg, str(amount)):
        return JSONResponse(status_code=464, content=Errors(464))
    
    # Check if amount meets either of the Zakat thresholds (gold or silver)
    if amount < selfinfo.Nisaab_lacag_d and amount < selfinfo.Nisaab_Lacag_f:
        return JSONResponse(status_code=325, content=Errors(325, True))
    
    # If amount meets gold threshold
    if amount >= selfinfo.Nisaab_lacag_d:
        jw = round(amount / Sako.Dahab_40, 4)
        requirements = [
            "The amount must be in US dollars 'USD'.",
            "You must have possessed it for one full year.",
            f"The Zakat has been calculated based on the gold price of {round(selfinfo.qiimaha_dahab_24, 4)} USD per gram."
        ]
        return JSONResponse(status_code=200, content=jawaab(jw, requirements, "$"))
    
    # If amount meets silver threshold
    if amount >= selfinfo.Nisaab_Lacag_f:
        jw = round(amount / Sako.Dahab_40, 4)
        requirements = [
            "The amount must be in US dollars 'USD'.",
            "You must have possessed it for one full year.",
            f"The Zakat has been calculated based on the silver price of {round(selfinfo.Qiimah_fidada_1G, 4)} USD per gram."
        ]
        return JSONResponse(status_code=200, content=jawaab(jw, requirements, "$"))
