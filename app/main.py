from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse , FileResponse
from fastapi.staticfiles import StaticFiles
from app.calculators.gold import xisaab_Dahab
from app.calculators.money import Lacag
from app.calculators.silver import Fido
from app.calculators.rikaas import Rikaas
from app.calculators.camels import Geel
from app.calculators.cows import Loa
from app.calculators.sheep import Adhi
from app.calculators.crops import Dalag
from app.utils.errors import Errors
from app.services.info import Info, Main_Location, LoadUsers
from app.services.metals import gold_silver_price

#app
app = FastAPI(
    title="E-sako API", 
    version="1.01",
    # docs_url=None,
    # redoc_url=None,
    # openapi_url=None
    )

app.mount("/static", StaticFiles(directory="static"), name="static")


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
        content=Errors(404)
    )


@app.get("/api/gold/{xadiga}")
async def xisaab(xadiga,Type=24,):
    return  xisaab_Dahab(xadiga,Type)

@app.get("/api/money/{xadi}")
async def lacag(xadi):
    return Lacag(xadi)



@app.get("/api/silver/{xadi}")
async def Fido_sako(xadi):
    return Fido(xadi)


@app.get("/api/rikaas/{xadi}")
async def Rikaas_xisaab(xadi):
    return Rikaas(xadi)

@app.get("/api/camels/{xadi}")
async def xisaab_geel(xadi):
    return Geel(xadi)

@app.get("/api/cows/{xadi}")
async def xisaab_lo(xadi):
    return Loa(xadi)



@app.get("/api/sheep/{xadi}")
async def xisaab_adhi(xadi):
    return Adhi(xadi)


@app.get("/api/crops/{xadi}")
async def xisaab_dalag(xadi,Type=1):
    return Dalag(xadi,Type)


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



@app.get("/")
async def Home(request: Request):
    client_ip = request.headers.get("x-forwarded-for")
    if client_ip:
        client_ip = client_ip.split(",")[0].strip()
    else:
        client_ip = request.client.host
    Main_Location(client_ip)
    return FileResponse("static/index.html")

@app.get("/doc")
def Docs_page(request: Request):
    client_ip = request.headers.get("x-forwarded-for")
    if client_ip:
        client_ip = client_ip.split(",")[0].strip()
    else:
        client_ip = request.client.host
    Main_Location(client_ip)
    return FileResponse("static/docs.html")

