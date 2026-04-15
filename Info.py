from Errors import Errors
from fastapi.responses import JSONResponse
import json
from datetime import datetime
import pytz
import requests

User_File = "files/location/Userslocation.json"

def InfoAnswer(totalRequests:int, code=200):
    local_time = pytz.timezone("Africa/Mogadishu")
    date = datetime.now(local_time)
    Date_format = f"{date.strftime("%A-%d-%B-%Y")}"
    Time_format = f"{date.strftime("%I:%M %p")}"
    return {
    "code": code,         
    "success": True,
    "message": "Request completed successfully",
    "data": {
    "createdBy": "Jumhuur",
    "statusCode": 200,
    "totalRequests": totalRequests 
  },
    "date": Date_format, 
    "time": Time_format          
}


def LoadUsers():
    try:
        with open(User_File, "r", encoding="utf-8") as File:
            data  = json.loads(File.read())
            return data
    except:
        return []
    

def save_User(user):
    users = LoadUsers()
    for us in users:
        if us["org"] == user["org"] and us["loc"] == user["loc"]:
            return
    users.append(user)
    with open(User_File, "w", encoding="utf-8") as File:
        json.dump(users, File, indent=2)

def Info():
    try:
        with open("files/reports/data_collection.json", "r", encoding="utf-8") as File:
            content = json.loads(File.read())
            return JSONResponse(status_code=200, content=InfoAnswer(len(content)))
    except FileNotFoundError:
        return JSONResponse(status_code=403, content=Errors(code=403))
    except Exception as e:
        return JSONResponse(status_code=403, content=Errors(code=403))


def Locations(client_ip: str = None):
    URL = f"https://ipinfo.io/{client_ip}/json" if client_ip and client_ip not in ["127.0.0.1", "::1"] else "https://ipinfo.io/json"
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        data  = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error", e)
        return {}




def Main_Location(client_ip: str = None):
    Userdata  = Locations(client_ip)
    AllData = {
        "city": Userdata.get("city", "Unknown"),
        "country": Userdata.get("country", "Unknown"),
        "loc": Userdata.get("loc", "Unknown"),
        "org": Userdata.get("org", "Unknown"),
        }
    save_User(AllData)
    return Userdata




