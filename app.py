# Author: Athul Prakash 

import requests
import json
import datetime

today = datetime.date.today().strftime('%d-%m-%y') # For date time format

headers = {
    "accept" : "application/json",
    "Accept-Language" : "hi_IN"
}

url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=297&date={today}"


data = requests.get(url, headers)

print(data.text)

