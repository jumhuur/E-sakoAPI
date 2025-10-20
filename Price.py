import requests
import os
from dotenv import load_dotenv
load_dotenv()
def gold_price():
    Dahab_data = requests.get(os.getenv("URL_DAHAB"), headers={"Cache-Control": "no-cache", "Pragma": "no-cache"} )
    if Dahab_data.status_code == 200:
        response = Dahab_data.json()
        return response["price"]
    else:
        raise RuntimeError("Ma Helin Wali Qiime Saxa !")


def silver_price():
    URL = os.getenv("URL_FIDO")
    Fido_data = requests.get(URL, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
    if Fido_data.status_code == 200:
        response = Fido_data.json()
        return response["price"]
    else:
        raise RuntimeError("Ma Helin Wali Qiime Saxa !")
    
