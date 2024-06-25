# main.py -- put your code here!

from machine import Pin, ADC
import utime

PARSLEY_PIN = 35
OREGANO_PIN = 34

oregano_sensor = ADC(Pin(OREGANO_PIN))
oregano_sensor.atten(ADC.ATTN_11DB)
parsley_sensor = ADC(Pin(PARSLEY_PIN))
parsley_sensor.atten(ADC.ATTN_11DB)

while True:
    oregano_val = oregano_sensor.read()
    parsley_val = parsley_sensor.read()
    print("Oregano value: " + str(oregano_val))
    print("Parsley value: " + str(parsley_val))