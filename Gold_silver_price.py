from fastapi.responses import JSONResponse
from Nisaabyo import selfinfo

def gold_silver_price():

    return JSONResponse(status_code=200, content={"XAU": selfinfo.gold_price, "XAG":selfinfo.silver_price})