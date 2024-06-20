# main.py -- put your code here!

from machine import Pin, ADC
import time

LED_PIN = 2
SENSOR_PIN = 34

led = Pin(2, Pin.OUT)
sensor = ADC(Pin(SENSOR_PIN))
sensor.atten(ADC.ATTN_11DB)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)