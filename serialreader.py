
import requests
import serial

url = 'http://10.244.128.66:8000/api/v1/meteo/'

port = 'COM3' 
baud_rate = 115200

ser = serial.Serial(port, baud_rate)

while True:
    line = ser.readline().decode('utf-8').strip()

    a = line.split("/")
    data = {
        "temperature" : a[0],
        "humidity" : a[1],
        "pressure" : a[2]
    }

    if data.values():
        post = requests.post(url,json=data)
        print(post.content)
    else:
        print('no data')
