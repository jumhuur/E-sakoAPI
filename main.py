import os
import threading
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse , FileResponse
from fastapi.staticfiles import StaticFiles
from Dahab import xisaab_Dahab
from Lacag import Lacag
from Fido import Fido
from Rikaas import Rikaas
from Geel import Geel
from Loa import Loa
from Adhi import Adhi
from Dalag import Dalag
from Errors import Errors
#app
app = FastAPI(
    title="E-sako API", 
    version="1.01",
    # docs_url=None,
    # redoc_url=None,
    # openapi_url=None
    )


# app = FastAPI(
#     title="E-sako API", 
#     version="1.01",
#     )


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
async def xisaab(xadiga:float,Type:int=24,):
    if Type and xadiga:
        return  xisaab_Dahab(xadiga,Type)
    raise JSONResponse(
            status_code=467,
            content= Errors(467)
        )

@app.get("/api/money/{xadi}")
async def lacag(xadi:int):
    if xadi:
        return Lacag(xadi)
    else:
        raise JSONResponse(
            status_code=467,
            content= Errors(467)
        )



@app.get("/api/silver/{xadi}")
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

@app.get("/api/camels/{xadi}")
async def xisaab_geel(xadi:int):
    if xadi:
        return Geel(xadi)
    else:
        return JSONResponse(
            status_code=467,
            content= Errors(467)
        )

@app.get("/api/cattle/{xadi}")
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

# @app.get("/report/result")
# def get_report():
#     folder = "files/reports"
#     os.makedirs(folder, exist_ok=True)
#     filepath = f"{folder}/{"result"}.pdf"
#     # try:
#     #     import time
#     #     time.sleep(2)  # sug 2 ilbiriqsi kadib tir
#     #     os.remove(filepath)
#     # except Exception as e:
#     #     print(f"Error deleting file: {e}")
#     # threading.Thread(target=filepath, args=({"result.pdf"},)).start()
#     return FileResponse(filepath, media_type="application/pdf", filename="result.pdf")


@app.get("/")
def Home():
    return FileResponse("static/index.html")

@app.get("/doc")
def Docs_page():
    return FileResponse("static/docs.html")

