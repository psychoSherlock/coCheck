# Author: Athul Prakash 

import requests
import json
import datetime



today = datetime.date.today().strftime('%d-%m-%y') # For date time format

headers = {
    "accept" : "application/json",
    "Accept-Language" : "hi_IN"
}
kannurID = 297


class cowin:
	def __init__(self,time=today):
		self.time = time
	def checkById(self, id):
		"""
		Return list of sessions from api
		"""
		self.id = id
		print(f"Fetching data for ID {id} on {self.time}")

		url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={id}&date={self.time}"
		data = requests.get(url, headers)

		# dump = json.dumps(data.text, indent=4) # For coverting python to json
		jsonData = json.loads(data.text) # for loading data as json
		
		return jsonData

# ADd more. Also add location getting feature

	def checkByDis(self, distr):
		self.distr = distr
		"""
		Return list of CENTERS from api
		"""
		print(f'Fetching data for district ID {distr} on date {self.time}')
		url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={distr}&date={self.time}"

		data = requests.get(url, headers)
		jsonData = json.loads(data.text)

		return jsonData

"""
		for i in range(len(jsonData['sessions'])):
		    centerName = jsonData['sessions'][i]['name']
		    vaccineName = jsonData['sessions'][i]['vaccine']
		    age_limit = jsonData['sessions'][i]['min_age_limit']
		    totalCapacity = jsonData['sessions'][i]['available_capacity']
		    dose1 = jsonData['sessions'][i]['available_capacity_dose1']
		    dose2 = jsonData['sessions'][i]['available_capacity_dose2']
		    # print(f'{centerName} {vaccineName} {age_limit} {totalCapacity} {dose1} {dose2}')
		    tableData.append([vaccineName, centerName, age_limit, totalCapacity, dose1, dose2])
		return centerName
"""
