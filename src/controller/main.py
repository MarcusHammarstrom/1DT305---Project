# main.py -- put your code here!

from machine import Pin, ADC
import utime
import secrets
from mqtt import MQTTClient

PARSLEY_PIN = 34
OREGANO_PIN = 35

client = MQTTClient(secrets.CONFIG)

oregano_sensor = ADC(Pin(OREGANO_PIN))
oregano_sensor.atten(ADC.ATTN_11DB)
parsley_sensor = ADC(Pin(PARSLEY_PIN))
parsley_sensor.atten(ADC.ATTN_11DB)

while True:
    try:
        client.connect()
        sum_parsley = 0
        sum_oregano = 0
        for i in range(15):
            print("Reading values")
            utime.sleep(1)
            temp_oregano = oregano_sensor.read()
            temp_parsley = parsley_sensor.read()

            sum_oregano += temp_oregano
            sum_parsley += temp_parsley
            #print("Oregano value: " + str(temp_oregano))
            #print("Parsley value: " + str(temp_parsley))
        oregano_val = sum_oregano / 15.0
        parsley_val = sum_parsley / 15.0
        print("Avaraged Oregano value: " + str(oregano_val))
        print("Aaraged Parsley value: " + str(parsley_val))
        client.publish(topic=secrets.AIO_PLANT1_FEED, msg=str(oregano_val), qos=1)
        client.publish(topic=secrets.AIO_PLANT2_FEED, msg=str(parsley_val), qos=1)
    except Exception as e:
        print("Something went wrong")
        print(str(e))
    client.disconnect()