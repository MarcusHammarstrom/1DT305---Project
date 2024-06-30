# main.py -- put your code here!

from machine import Pin, ADC
import utime
import secrets
import urequests as requests

MIN_CHIVES = 0
MIN_DILL = 0
MAX_CHIVES = 0
MAX_DILL = 0

DILL_PIN = 32
CHIVES_PIN = 35

chives_sensor = ADC(Pin(CHIVES_PIN))
chives_sensor.atten(ADC.ATTN_11DB)
dill_sensor = ADC(Pin(DILL_PIN))
dill_sensor.atten(ADC.ATTN_11DB)

def BuildJSON(value):
    data = { "value": value }
    return data

def SendData(value, feed):
    headers = { "X-AIO-Key": secrets.AIO_KEY, "Content-Type": "application/json"}
    data = BuildJSON(value)
    return requests.post(feed, json=data, headers=headers)

while True:
    try:
        sum_dill = 0
        sum_chives = 0
        print("Making sensor readings")
        for i in range(10):
            utime.sleep(0.5)
            temp_chives = chives_sensor.read()
            temp_dill = dill_sensor.read()

            sum_chives += temp_chives
            sum_dill += temp_dill
        chives_val = sum_chives / 10.0
        dill_val = sum_dill / 10.0
        print("Chives value: " + str(chives_val))
        print("Dill value: " + str(dill_val))
        #SendData(str(dill_val), secrets.AIO_PLANT1_FEED)
        #SendData(str(chives_val), secrets.AIO_PLANT2_FEED)
        utime.sleep(10)
    except Exception as e:
        print("Something went wrong")
        print(str(e))