from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from Dahab import xisaab_Dahab
from Lacag import Lacag
from Fido import Fido
from Rikaas import Rikaas
from Geel import Geel
from Loa import Loa
from Adhi import Adhi
from Errors import Errors
#app
app = FastAPI(title="E-sako API", version="1.01")


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

@app.get("/")
def home():
    return {"code" : 200, "Fariin": "ku soo dhawaaw E-sako API"}


@app.get("/api/dahab/{nooc},{xadiga}")
async def xisaab(nooc:int,xadiga:float):
    if nooc and xadiga:
        return  xisaab_Dahab(nooc,xadiga)
    raise JSONResponse(
            status_code=467,
            content= Errors(467)
        )

@app.get("/api/lacag/{xadi}")
async def lacag(xadi:int):
    if xadi:
        return Lacag(xadi)
    else:
        raise JSONResponse(
            status_code=467,
            content= Errors(467)
        )



@app.get("/api/fido/{xadi}")
async def Fido_sako(xadi:int):
    if xadi:
        return Fido(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )


@app.get("/api/rikaas/{xadi}")
async def Rikaas_xisaab(xadi:int):
    if xadi:
        return Rikaas(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )

@app.get("/api/geel/{xadi}")
async def xisaab_geel(xadi:int):
    if xadi:
        return Geel(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )

@app.get("/api/lo/{xadi}")
async def xisaab_lo(xadi):
    if xadi:
        return Loa(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )



@app.get("/api/adhi/{xadi}")
async def xisaab_adhi(xadi):
    if xadi:
        return Adhi(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )

