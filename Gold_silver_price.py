from fastapi.responses import JSONResponse
from Price import gold_price,silver_price

def gold_silver_price():

    return JSONResponse(status_code=200, content={"XAU": gold_price(), "XAG":silver_price()})