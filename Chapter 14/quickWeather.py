#!python3 
#quickWeather.py - downloads weather data from quickWeather.py

import json, requests, sys
from datetime import datetime

#Compute location from command line arguments.


def main():
	if len(sys.argv)<2:
		print('Usage: quickWeather.py [location]')
		sys.exit()
	location = ' '.join(sys.argv[1:])
	#TODO: Download JSON data from OpenWeatherMap.org's API
	url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=17&appid=cd2bf382fd14abcd26fad1c24cd2aeff' % (location)
	response = requests.get(url)
	response.raise_for_status()
	#Load JSON data into a Python variable.
	weatherData = json.loads(response.text)
	w = weatherData['list']
	print('Current weater in %s: ' %(location))
	print(w[0]['weather'][0]['main'], '-' ,w[0]['weather'][0]['description'])
	print()
	print ('Tomorrow around ' + datetime.now().strftime('%H:%M'))
	print(w[8]['weather'][0]['main'], '-', w[8]['weather'][0]['description'])
	print()
	print('Day after tomorrow around ' + datetime.now().strftime('%H:%M'))
	print(w[16]['weather'][0]['main'], '-', w[16]['weather'][0]['description'])	

if __name__ =='__main__':
	main()