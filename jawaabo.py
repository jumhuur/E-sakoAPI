from datetime import datetime
import pytz


def jawaab(jawaab:int, shuruudo:list, nooc, code=200):
    local_time = pytz.timezone("Africa/Mogadishu")
    date = datetime.now(local_time)
    Date_format = f"{date.strftime("%A %d-%B-%Y")}"
    Time_format = f"{date.strftime("%I:%M %p")}"
    return {
    "code": code,          # Error or status code
    "response": jawaab,    # Response message or result
    "requirements": shuruudo,  # Conditions or rules (previously "Shuruudo")
    "Unit": nooc,         # The amount or type entered (previously "Qiyaas")
    "date": Date_format,          # Date of request (previously "Taariikh")
    "time": Time_format           # Time of request (previously "Wakhti")
}
