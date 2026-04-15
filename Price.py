import requests
import os
import time
from dotenv import load_dotenv
load_dotenv()
def gold_price():
    URL =  os.getenv("URL_DAHAB")
    Dahab_data = requests.get(URL, headers={"Cache-Control": "no-cache", "Pragma": "no-cache", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
    if Dahab_data.status_code == 200:
        response = Dahab_data.json()
        return response["price"]
    else:
        raise RuntimeError(f"Ma Helin Wali Qiima dahabka oo Saxa ! Status: {Dahab_data.status_code}")


def silver_price():
    URL = os.getenv("URL_FIDO")
    Fido_data = requests.get(URL, headers={"Cache-Control": "no-cache", "Pragma": "no-cache", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
    if Fido_data.status_code == 200:
        response = Fido_data.json()
        return response["price"]
    else:
        raise RuntimeError(f"Ma Helin Wali Qiimaha fidada oo Saxa ! Status: {Fido_data.status_code}")
