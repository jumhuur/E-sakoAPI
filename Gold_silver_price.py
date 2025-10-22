from fastapi.responses import JSONResponse
from Price import gold_price,silver_price
import json
from Nisaabyo import Sako

def gold_silver_price():
    return JSONResponse(status_code=200, content={"XAU": gold_price(), "XAG":silver_price()})


def Price_24_1g():
    response = gold_silver_price()
    json_data = json.loads(response.body)
    XAU , XAG = json_data.values()
    gold_24 = round(int(XAU) / Sako.one_ounce, 4)
    silver_1G = round(int(XAG) / Sako.one_ounce, 4)
    nisab_money_gold = round(gold_24 * Sako.Nisaab_dahab, 4)
    nisab_money_silver = round(silver_1G * Sako.Nisaab_Fidada,4)
    return {"g_24": gold_24, "s_1":silver_1G, "nisab_g" : nisab_money_gold, "nisab_s": nisab_money_silver}