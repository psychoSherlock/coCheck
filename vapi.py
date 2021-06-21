# Author: Athul Prakash 
# vapi stand for vaccine api BTW :D

import requests
import json
import datetime
import csv


today = datetime.date.today().strftime('%d-%m-%y') # For date time format

headers = {
    "accept" : "application/json",
    "Accept-Language" : "hi_IN"
}
kannurID = 297


class api:
	def __init__(self,time=today):
		self.time = time
	def checkByDistrictId(self, ID):
		"""
		Return list of sessions from api
		"""
		self.ID = ID
		print(f"Fetching data for ID {ID} on {self.time}")

		url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={ID}&date={self.time}"
		data = requests.get(url, headers)

		# dump = json.dumps(data.text, indent=4) # For coverting python to json
		jsonData = json.loads(data.text) # for loading data as json
		
		return jsonData

# ADd more. Also add location getting feature

	def checkByPincode(self, pincode):
		self.pincode = pincode
		"""
		Return list of CENTERS from api
		"""
		print(f'Fetching data for Pincode {pincode} on date {self.time}')
		url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={self.time}"

		data = requests.get(url, headers)
		jsonData = json.loads(data.text)

		return jsonData

def getDistricts():
	"""
	Return all districts with theit id. eg: district, id = cowin().getDistricts
	"""
	csvFile = 'district_mapping.csv'
	csvFile = open(csvFile, 'r')
	csvData = csv.reader(csvFile)
	return csvData




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
