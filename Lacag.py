from fastapi.responses import JSONResponse
from Nisaabyo import Sako, selfinfo
from Errors import Errors
from jawaabo import jawaab
from Gold_silver_price import gold_silver_price
import re
import json

def Lacag(amount: int):
    response = gold_silver_price()
    json_data = json.loads(response.body)
    XAU , XAG = json_data.values()
    gold_24 = round(int(XAU) / Sako.one_ounce, 4)
    silver_1G = round(int(XAG) / Sako.one_ounce, 4)

    nisab_money_gold = round(gold_24 * Sako.Nisaab_dahab, 4)
    nisab_money_silver = round(silver_1G * Sako.Nisaab_Fidada,4)
    
    Sako.data_collection(amount)
    reg = r"^\d+$"
    if not re.match(reg, str(amount)):
        return JSONResponse(status_code=464, content=Errors(464))
    
    # Check if amount meets either of the Zakat thresholds (gold or silver)
    if int(amount) < nisab_money_gold and int(amount) < nisab_money_silver:
        return JSONResponse(status_code=325, content=Errors(325, True))
    
    # If int(amount) meets gold threshold
    if int(amount) >= nisab_money_gold:
        jw = round(int(amount) / Sako.Dahab_40, 4)
        requirements = [
            "The amount must be in US dollars 'USD'.",
            "You must have possessed it for one full year.",
            f"The Zakat has been calculated based on the gold price of {round(selfinfo.qiimaha_dahab_24, 4)} USD per gram."
        ]
        return JSONResponse(status_code=200, content=jawaab(jw, requirements, "$"))
    
    # If amount meets silver threshold
    if int(amount) >= nisab_money_silver:
        jw = round(int(amount) / Sako.Dahab_40, 4)
        requirements = [
            "The amount must be in US dollars 'USD'.",
            "You must have possessed it for one full year.",
            f"The Zakat has been calculated based on the silver price of {round(selfinfo.Qiimah_fidada_1G, 4)} USD per gram."
        ]
        return JSONResponse(status_code=200, content=jawaab(jw, requirements, "$"))

