# boot.py -- run on boot-up

import network
from wifi import keys
from time import sleep

sta_if = network.WLAN(network.STA_IF)     # Create instance of a station interface object

if not sta_if.isconnected():              # Check if connection already established
    print("Connecting to the network...")  
    sta_if.active(True)                   # Activate station interface

    sta_if.connect(keys["SSID"], keys["PASS"]) # Connect to WiFi
    print('Waiting for connection...', end='') 

    while not sta_if.isconnected() and sta_if.status() >= 0: # Wait for connection
        print('.', end='')
        sleep(1)
    
    adress = sta_if.ifconfig()[0] # Retrieve and print device ip-adress
    print("\nConnected to WiFi with adress {}".format(adress))