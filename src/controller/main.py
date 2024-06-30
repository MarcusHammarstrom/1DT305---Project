# main.py -- put your code here!

from machine import Pin, ADC
import utime
import secrets
import urequests as requests
import ntptime

MAX_CHIVES = 2544
MAX_DILL = 2536
MIN_CHIVES = 905
MIN_DILL = 848

CHIVES_DIFF = MAX_CHIVES - MIN_CHIVES
DILL_DIFF = MAX_DILL - MIN_DILL

DILL_PIN = 32
CHIVES_PIN = 35
PUMP_PIN = 26

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

def CalculateMoisture(chives, dill):
    chives_moisture = (MAX_CHIVES - chives) / CHIVES_DIFF	# Scale the sensor readings. 0 value means dry, 1 mean completely wet.
    dill_moisture = (MAX_DILL - chives) / DILL_DIFF
    return (chives_moisture * 100, dill_moisture * 100)		# Put moisture value in percentage form.

ntptime.host = "0.se.pool.ntp.org"
ntptime.settime()

pump = Pin(PUMP_PIN, Pin.OUT)
    
while True:
    try:
        current_time = utime.localtime(utime.time() + (2 * 3600))
        print("Hour: " + str(current_time[3]))
        print("Minute: " + str(current_time[4]))
        if (current_time[3] == )
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
        chives_moisture, dill_moisture = CalculateMoisture(chives_val, dill_val)
        print("Chives value: " + str(chives_moisture))
        print("Dill value: " + str(dill_moisture))
        #SendData(str(dill_moisture), secrets.AIO_PLANT1_FEED)
        #SendData(str(chives_moisture), secrets.AIO_PLANT2_FEED)
        utime.sleep(10)
    except Exception as e:
        print("Something went wrong")
        print(str(e))