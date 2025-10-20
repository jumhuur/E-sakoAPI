from dotenv import load_dotenv
import json
from datetime import datetime
from reportlab.lib.pagesizes import A4
from Price import gold_price,silver_price

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
    Nisaab_Rikaas = Nisaab_dahab
    Nisaab_Geel = 5
    Nisaab_adhi = 40
    Nisaab_lo = 30
    Nisaab_Midhaha = 612;  # waa sida jumhuurka ayaa qaba in uu yahay 612  // 672 // 750  // 653

    # hal ounce inta giraam ee yahay
    one_ounce = 31.1035

    # qiimaha_dahabka = 4018.399902 # waa marka lagu xisaabiyo OUNCE = OO AH 1TROY OO U DHIGMA 31.1035G SAAFI AH 
    # qiimaha_fidada = 50.008999  # waa marka lagu xisaabiyo OUNCE = OO AH 1TROY OO U DHIGMA 31.1035G SAAFI AH

    # halbeegyada xisaabta Midhaha
    Dahab_40:int = 40
    x_bilaa_kharash = 0.1;
    x_kharaskha = 0.05;
    isku_jir = 0.075;
    Nocyada_dahabka = [24,22,21,20,18,16]
    def __init__(self,go_price=0,si_price=0):
        # price 
        self.qiimaha_ounce = go_price
        self.qiimaha_ounce_fido = si_price

        # clac Types
        self.qiimaha_dahab_24 = self.qiimaha_ounce / Sako.one_ounce
        self.qiimaha_dahab_22 = self.qiimaha_dahab_24 * Sako.__22
        self.qiimaha_dahab_21 = self.qiimaha_dahab_24 * Sako.__21
        self.qiimaha_dahab_18 = self.qiimaha_dahab_24 * Sako.__18
        self.qiimaha_dahab_16 = self.qiimaha_dahab_24 * Sako.__16
        self.Nisaab_lacag_d:int = self.qiimaha_dahab_24 * Sako.Nisaab_dahab
        # silver
        self.Qiimah_fidada_1G = self.qiimaha_ounce_fido / Sako.one_ounce
        self.Nisaab_Lacag_f:int = self.Qiimah_fidada_1G * Sako.Nisaab_Fidada # waa nisaabka lacagta marka fido lagu xisaabiyo

    @staticmethod
    def data_collection(xadiga,nooc=0):
        dateTime  = datetime.now()
        data = {
            "Xadig": xadiga,
            "nooca": nooc,
            "date": dateTime.strftime("%A %d-%B-%Y"),
            "time": dateTime.strftime("%I:%M %p")
        }

        with open("files/reports/data_collection.json", "r") as perv_file:
            prev_data = json.load(perv_file)
        prev_data.append(data)
        with open("files/reports/data_collection.json", "w") as file:
            json.dump(prev_data,file, indent=4)
    
    # def greate_result_file(item,amount,Type,Result, conditions,unit):
    #     pdf = canvas.Canvas("files/reports/result.pdf", pagesize=A4)

    #     pdf.setTitle("Your Zakaat Result")  # Cinwaan
    #     pdf.setFont("Helvetica-Bold", 18)
    #     pdf.drawString(100, 790, f"You callculate : {amount}-{unit} of {item}  Type:{Type} ")
    #     pdf.setFont("Helvetica", 12)
    #     pdf.drawString(100, 770, f"Result is {Result} {unit}")
    #     pdf.line(100, 760, 500, 760)
    #     pdf.drawString(100,735 , "Sakah conditions")
    #     y = 715
    #     for numb , condition in enumerate(conditions, start=1):
    #         pdf.setFont("Helvetica", 12)
    #         text = f"{numb} .{condition}"
    #         pdf.drawString(100, y, text)
    #         y -= 20 
    #     pdf.drawString(100, 655, f"Date : {dateTime.strftime("%A %d-%B-%Y")}")
    #     pdf.drawString(100, 635, f"Time : {dateTime.strftime("%I:%M %p")}")
    #     pdf.drawString(100, 600, "Esakoapi.org")

    #     pdf.save()


selfinfo = Sako(gold_price(), silver_price())
# print(selfinfo.qiimaha_ounce)
# print(selfinfo.qiimaha_ounce_fido)
# print("*" * 25)
# print(Sako.silver_price)
# print(Sako.gold_price)