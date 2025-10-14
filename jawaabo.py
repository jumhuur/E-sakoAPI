from datetime import datetime
date = datetime.now()
Date_format = f"{date.strftime("%A %d-%B-%Y")}"
Time_format = f"{date.strftime("%I:%M %p")}"
def jawaab(jawaab:int, shuruudo:list, nooc, code=200, date=Date_format, time=Time_format):
    return {
    "code": code,          # Error or status code
    "response": jawaab,    # Response message or result
    "requirements": shuruudo,  # Conditions or rules (previously "Shuruudo")
    "Unit": nooc,         # The amount or type entered (previously "Qiyaas")
    "date": date,          # Date of request (previously "Taariikh")
    "time": time           # Time of request (previously "Wakhti")
}
