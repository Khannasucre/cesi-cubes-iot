from datetime import datetime
import requests
import serial
import time

url = 'http://10.244.128.66:8000/api/v1/meteo/'

timestamp = int(time.time()) + 3600
date =  datetime.utcfromtimestamp(timestamp)
date = date.strftime('%Y-%m-%d %H:%M:%S')

port = 'COM3' 
baud_rate = 115200

ser = serial.Serial(port, baud_rate)

while True:
    line = ser.readline().decode('utf-8').strip()
    print(line)
    if line[:5] == "Found":
        print("Not now")
    else :
        a = line.split("/")
        print(a)
        data = {
            "temperature" : float(a[0]),
            "humidity" : float(a[1]),
            "pressure" : float(a[2]),
            "date" : date
        }
        print(data)
        if data.values():
            post = requests.post(url,json=data)
            print(post.content)
        else:
            print('no data')
