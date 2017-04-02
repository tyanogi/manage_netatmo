#!/usr/bin/python3
# encoding=utf-8

import lnetatmo
import urllib.request
import authinfo

def main():
    info = my_authinfo.set()
    params = getinfo(info.authorization)
    res = upload(params, info.apikey)
    print(res)

# NETATMOの情報を取得
def getinfo(authorization):

    # パラメータを設定
    params = {
            "field1":"",
            "field2":"",
            "field3":"",
            "field4":"",
            }
    
    weather_station = lnetatmo.WeatherStationData(authorization)
    data = weather_station.lastData()

    ''' 
    dataの中身(sample) ----------------------------------------------
    {'屋内': {'AbsolutePressure': 1020.1, 'Noise': 48, 'Temperature': 25.2, 'temp_trend': 'up', 'Humidity': 32, 'Pressure': 1020.1, 'pressure_trend': 'stable', 'CO2': 1149, 'date_max_temp': 1490859269, 'date_min_temp': 1490823519, 'min_temp': 16.1, 'max_temp': 25.4, 'When': 1490870784, 'wifi_status': 42}, '屋外': {'Temperature': 24.3, 'temp_trend': 'stable', 'Humidity': 35, 'date_max_temp': 1490860768, 'date_min_temp': 1490822573, 'min_temp': 15.8, 'max_temp': 24.7, 'When': 1490870766, 'battery_vp': 6178, 'rf_status': 28}, '風速計': {'WindAngle': -1, 'WindStrength': 0, 'GustAngle': 74, 'GustStrength': 3, 'WindHistoric': [{'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490867447}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490867755}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490868056}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490868357}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490868664}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490868965}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490869267}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490869575}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490869875}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490870176}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490870477}, {'WindStrength': 0, 'WindAngle': -1, 'time_utc': 1490870779}], 'date_max_wind_str': 1490805950, 'date_max_temp': 1490799888, 'date_min_temp': 1490799888, 'min_temp': 0, 'max_temp': 0, 'max_wind_angle': 139, 'max_wind_str': 3, 'When': 1490870779, 'battery_vp': 6252, 'rf_status': 63}, '雨量計': {'Rain': 0, 'sum_rain_24': 0, 'sum_rain_1': 0, 'When': 1490870772, 'battery_vp': 6354, 'rf_status': 49}}
{'field1': 25.2, 'field2': 32, 'field3': 1020.1, 'field4': 1149}
    -----------------------------------------------------------------
    '''
    
    # 拡張可能
    params['field1'] = data['屋内']['Temperature'] 
    params['field2'] = data['屋内']['Humidity']
    params['field3'] = data['屋内']['Pressure']
    params['field4'] = data['屋内']['CO2']

    return params;
    
# NETATMOの情報をThingSpeakにアップロード
def upload(params, apikey):
    # ThingSpeak URL
    ts_url = "https://api.thingspeak.com/update/"
    method = "POST"

    params = urllib.parse.urlencode(params).encode("utf-8")
    
    request = urllib.request.Request(ts_url, data=params, method=method, headers=apikey)
    
    with urllib.request.urlopen(request) as ts_res:
        html = ts_res.read()

    return "ThingSpeak Response: " + str(html)

if __name__ == '__main__':
    main()

