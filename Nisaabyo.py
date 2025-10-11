import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime

load_dotenv()

class Sako():
    # Noocyada Dahabka
    Noocyo = {
        "24" : 24,
        "22" : 22,
        "21" : 21,
        "20" : 20,
        "18" : 18,
        "16" : 16
    }
    # Saafinimada Noocyada dahabka
    __24 = 1 # saafi 100%
    __22 = 0.9167
    __21 = 0.875
    __18 = 0.75
    __16 = 0.6667

    # nisaabyo
    Nisaab_dahab = 85;
    Nisaab_Fidada = 595;

    # hal ounce inta giraam ee yahay
    one_ounce = 31.1035

    # qiimaha_dahabka = 4018.399902 # waa marka lagu xisaabiyo OUNCE = OO AH 1TROY OO U DHIGMA 31.1035G SAAFI AH 
    # qiimaha_fidada = 50.008999  # waa marka lagu xisaabiyo OUNCE = OO AH 1TROY OO U DHIGMA 31.1035G SAAFI AH

    # halbeegyada xisaabta Midhaha
    Nisaabka_Midhaha = 612;  # waa sida jumhuurka ayaa qaba in uu yahay 612  // 672 // 750  // 653
    x_bilaa_kharash = 0.1;
    x_kharaskha = 0.05;
    isku_jir = 0.075;
    Nocyada_dahabka = [24,22,21,20,18,16]
    def __init__(self):
        data = requests.get(os.getenv("URL_DAHAB"))
        if data.status_code == 200:
            for info in data:
                byte_data = list(data)[0]
                json_string = byte_data.decode('utf-8')
                info = json.loads(json_string)
                self.qiimaha_ounce = info["price"]
                self.nooca = info["symbol"]
                self.Wakhtiga_update_ka = info["updatedAt"]
                self.qiimaha_dahab_24 = self.qiimaha_ounce / Sako.one_ounce
                self.qiimaha_dahab_22 = self.qiimaha_dahab_24 * Sako.__22
                self.qiimaha_dahab_21 = self.qiimaha_dahab_24 * Sako.__21
                self.qiimaha_dahab_18 = self.qiimaha_dahab_24 * Sako.__18
                self.qiimaha_dahab_16 = self.qiimaha_dahab_24 * Sako.__16
        else:
            raise RuntimeError("Ma Helin Wali Qiime Saxa !")
        
    def qiimaha_dahabka(self):
        pass
       
    def qiimaha_fidada(self):
        data = requests.get(os.getenv("URL_FIDO"))
        if data.status_code == 200:
            for info in data:
                byte_data = list(data)[0]
                json_string = byte_data.decode('utf-8')
                info = json.loads(json_string)
                self.qiimaha_ounce = info["price"]
                self.nooca = info["symbol"]
                self.Wakhtiga_update_ka = info["updatedAt"]
            return info
        else:
            raise RuntimeError("Ma Helin Wali Qiime Saxa !")

Sakaat = Sako()