#!/usr/bin/python3
# encoding=utf-8

import lnetatmo
import urllib.request
import authinfo

info = authinfo.set()

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

#天気情報の取得
weather_station = lnetatmo.WeatherStationData(info.authorization)
data = weather_station.lastData()

params['field1'] = data['屋内']['Temperature'] 
params['field2'] = data['屋内']['Humidity']
params['field3'] = data['屋内']['Pressure']
params['field4'] = data['屋内']['CO2']

params = urllib.parse.urlencode(params).encode("utf-8")

request = urllib.request.Request(ts_url, data=params, method=method, headers=headers)

with urllib.request.urlopen(request) as ts_res:
    html = ts_res.read()
    print("ThingSpeak Response: " + str(html))

