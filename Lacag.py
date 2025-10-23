from fastapi.responses import JSONResponse
from Nisaabyo import Sako, selfinfo
from Errors import Errors
from jawaabo import jawaab
from Gold_silver_price import  Price_24_1g
import re

def Lacag(amount: int):
    response = Price_24_1g()
    _, _, nisab_g , nisab_s = response.values()
    Sako.data_collection(amount)
    reg = r"^\d+$"
    if not re.match(reg, str(amount)):
        return JSONResponse(status_code=464, content=Errors(464))
    # Check if amount meets either of the Zakat thresholds (gold or silver)
    if int(amount) < nisab_g and int(amount) < nisab_s:
        return JSONResponse(status_code=325, content=Errors(325, True))
    
    # If int(amount) meets gold threshold
    if int(amount) >= nisab_g:
        jw = round(int(amount) / Sako.Dahab_40, 4)
        requirements = [
            "The amount must be in US dollars 'USD'.",
            "You must have possessed it for one full year.",
            f"The Zakat has been calculated based on the gold price of {round(selfinfo.qiimaha_dahab_24, 4)} USD per gram."
        ]
        return JSONResponse(status_code=200, content=jawaab(jw, requirements, "$"))
    
    # If amount meets silver threshold
    if int(amount) >= nisab_s:
        jw = round(int(amount) / Sako.Dahab_40, 4)
        requirements = [
            "The amount must be in US dollars 'USD'.",
            "You must have possessed it for one full year.",
            f"The Zakat has been calculated based on the silver price of {round(selfinfo.Qiimah_fidada_1G, 4)} USD per gram."
        ]
        return JSONResponse(status_code=200, content=jawaab(jw, requirements, "$"))

