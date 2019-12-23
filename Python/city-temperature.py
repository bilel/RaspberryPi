#Replace APIKEY
#Replace CityId id=..
#Temperature is displayed in Celsius

from jq import jq
import requests
import simplejson as json
r =requests.get('https://api.openweathermap.org/data/2.5/weather?id=2468925&appid=APIKEY')
tempek= jq(".main.temp").transform(r.json())
tempec = tempek - 273.15
print (tempec)
