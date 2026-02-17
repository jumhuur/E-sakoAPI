from jawaabo import jawaab
from Errors import Errors
from fastapi.responses import JSONResponse
import json
from datetime import datetime
import pytz



def InfoAnswer(totalRequests:int, code=200):
    local_time = pytz.timezone("Africa/Mogadishu")
    date = datetime.now(local_time)
    Date_format = f"{date.strftime("%A %d-%B-%Y")}"
    Time_format = f"{date.strftime("%I:%M %p")}"
    return {
    "code": code,          # Error or status code
    "success": True,    # Response message or result
    "message": "Request completed successfully",
    "data": {
    "createdBy": "Jumhuur",
    "statusCode": 200,
    "totalRequests": totalRequests 
  },
    "date": Date_format,          # ("Taariikh")
    "time": Time_format           # ("Wakhti")
}

def Info():
    try:
        with open("files/reports/data_collection.json", "r", encoding="utf-8") as File:
            content = json.loads(File.read())
            return InfoAnswer(len(content))
    except FileNotFoundError:
        return "file not found"
    except Exception as e:
        print(f"Error: {e}")

