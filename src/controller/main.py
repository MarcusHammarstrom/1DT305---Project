# main.py -- put your code here!

from machine import Pin, ADC
import utime
import secrets
import urequests as requests

MIN_OREGANO = 0
MIN_PARSLEY = 0
MAX_OREGANO = 0
MAX_PARSLEY = 0

PARSLEY_PIN = 34
OREGANO_PIN = 35

oregano_sensor = ADC(Pin(OREGANO_PIN))
oregano_sensor.atten(ADC.ATTN_11DB)
parsley_sensor = ADC(Pin(PARSLEY_PIN))
parsley_sensor.atten(ADC.ATTN_11DB)

def BuildJSON(value):
    data = { "value": value }
    return data

def SendData(value, feed):
    headers = { "X-AIO-Key": secrets.AIO_KEY, "Content-Type": "application/json"}
    data = BuildJSON(value)
    return requests.post(feed, json=data, headers=headers)

while True:
    try:
        sum_parsley = 0
        sum_oregano = 0
        for i in range(10):
            utime.sleep(0.5)
            temp_oregano = oregano_sensor.read()
            temp_parsley = parsley_sensor.read()

            sum_oregano += temp_oregano
            sum_parsley += temp_parsley
            print("Oregano value: " + str(temp_oregano))
            print("Parsley value: " + str(temp_parsley))
        oregano_val = sum_oregano / 15.0
        parsley_val = sum_parsley / 15.0
        print("Avaraged Oregano value: " + str(oregano_val))
        print("Aaraged Parsley value: " + str(parsley_val))
        #SendData(str(oregano_val), secrets.AIO_PLANT1_FEED)
        #SendData(str(parsley_val), secrets.AIO_PLANT2_FEED)
    except Exception as e:
        print("Something went wrong")
        print(str(e))
    client.disconnect()