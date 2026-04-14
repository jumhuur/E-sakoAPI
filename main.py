from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse , FileResponse
from Dahab import xisaab_Dahab
from Lacag import Lacag
from Fido import Fido
from Rikaas import Rikaas
from Geel import Geel
from Loa import Loa
from Adhi import Adhi
from Dalag import Dalag
from Errors import Errors
from Info import Info, Main_Location, LoadUsers,Locations
from Gold_silver_price import gold_silver_price

#app
app = FastAPI(
    title="E-sako API", 
    version="1.01",
    # docs_url=None,
    # redoc_url=None,
    # openapi_url=None
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # dhamaan waa lo ogol_yahay
    allow_credentials=True,
    allow_methods=["GET"],        # GET
    allow_headers=["*"],        # headers
)



@app.exception_handler(404)
async def not_found(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content=Errors(467,False)
    )


@app.get("/api/gold/{xadiga}")
async def xisaab(xadiga,Type:int=24,):
    if Type and xadiga:
        return  xisaab_Dahab(xadiga,Type)
    raise JSONResponse(
            status_code=467,
            content= Errors(467)
        )

@app.get("/api/money/{xadi}")
async def lacag(xadi):
    if xadi:
        return Lacag(xadi)
    else:
        raise JSONResponse(
            status_code=467,
            content= Errors(467)
        )



@app.get("/api/silver/{xadi}")
async def Fido_sako(xadi):
    if xadi:
        return Fido(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )


@app.get("/api/rikaas/{xadi}")
async def Rikaas_xisaab(xadi):
    if xadi:
        return Rikaas(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )

@app.get("/api/camels/{xadi}")
async def xisaab_geel(xadi):
    if xadi:
        return Geel(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )

@app.get("/api/cows/{xadi}")
async def xisaab_lo(xadi):
    if xadi:
        return Loa(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )



@app.get("/api/sheep/{xadi}")
async def xisaab_adhi(xadi):
    if xadi:
        return Adhi(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )


@app.get("/api/crops/{xadi}")
async def xisaab_dalag(xadi,Type=1):
    if xadi:
        return Dalag(xadi,Type)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )


@app.get("/api/price")
async def Price():
    if True:
        return gold_silver_price()
@app.get("/api/info")
async def apiinfo():
    if True:
        return Info()
    

@app.get("/api/online")
async def Online():
    if True:
        return LoadUsers()
    
@app.get("/api/activeUser/{user}")
async def activeUser(user=dict):
    if user:
        return Locations(user=dict)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )


@app.get("/")
async def Home():
    Main_Location()
    return FileResponse("static/index.html")

@app.get("/doc")
def Docs_page():
    return FileResponse("static/docs.html")

