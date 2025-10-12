from datetime import datetime
date = datetime.now()
Date_format = f"{date.strftime("%A %d-%B-%Y")}"
Time_format = f"{date.strftime("%I:%M %p")}"
def jawaab(jawaab:int, shuruudo:list, nooc, code=200, date=Date_format, time=Time_format):
    return {"code": code, "jawaab":jawaab, "Shuruudo":shuruudo, "Qiyaas":nooc, "Taariikh":date, "Wakhti":time}
