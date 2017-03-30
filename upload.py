#!/usr/bin/python3
# encoding=utf-8

import lnetatmo
import urllib.request

#tokenを取得
authorization = lnetatmo.ClientAuth(
                clientId = "NETATMO Client id",
                clientSecret = "NETATMO Client secret",
                username = "NETATMO Username",
                password = "NETATMOPassword",
                #scope = ""
)

# ThingSpeak URL
ts_url = "https://api.thingspeak.com/update/"

# Setting PostParam
params = {
        "field1":"",
        "field2":"",
        "field3":"",
        "field4":"",
        }
method = "POST"
# Setting PostHeader(ThingSpeak APIKEY)
headers = {"X-THINGSPEAKAPIKEY":"ThingSpeak Write API Key"}

#天気情報の取得
weather_station = lnetatmo.WeatherStationData(authorization)
data = weather_station.lastData()

#天気情報の表示
print(data['屋内'])

params['field1'] = data['屋内']['Temperature'] 
params['field2'] = data['屋内']['Humidity']
params['field3'] = data['屋内']['Pressure']
params['field4'] = data['屋内']['CO2']
print(params)
print("ThingSpeak URL: " + ts_url)

params = urllib.parse.urlencode(params).encode("utf-8")

request = urllib.request.Request(ts_url, data=params, method=method, headers=headers)

with urllib.request.urlopen(request) as ts_res:
    html = ts_res.read()
    print("ThingSpeak Response: " + str(html))

