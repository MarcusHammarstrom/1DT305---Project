# Plant automation

Marcus Hammarström / mh226yz

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/final2.jpg?raw=true" alt="Image" width="300">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/final3.jpg?raw=true" alt="Image" width="300">
</p>

Plant automation is a project for monitoring and watering two plants at home. Providing moisture sensing, automated irrigation as well as regular photos of the plants. Recreating this project will give usefull skills for home automation and a functioning plant monitoring and watering system.

The project will take approximately 4-5 hours to recreate.

## Objective

The purpose of this project was for me to learn more about home automation, gathering data and analysing data. I have also been interested in growing plants but have struggled with the routine to keep them alive for long periods of time. This project will improve my skills in working with IoT devices and inspire me to explore more ideas in the future.

## Material

| Component | Bought at | Price |
| ------------- | ------------- | ------------- |
| ESP32 Dev Kit C V4 NodeMCU | [Amazon](https://www.amazon.se/AZDelivery-V4-Development-osoldered-Efterf%C3%B6ljarmodul/dp/B08BTS62L7/ref=sr_1_3?crid=3KC5YUYP4F0ZZ&dib=eyJ2IjoiMSJ9.TNKcIAfxqmm9xC5lJX-Zq9vog15DYbOLTf5Vhevs2ziLby2--QHKJEHlCarHz62JldxKeamabka_FPkAWXEXiOw8qtkEULH-W6jtCLeIxeWGkI41fFQDnG2g8lJEEoQkGLEAUgBLbLOxhbeOUqlMSsQ1lydTBIvAEZ_DTptMILTQ-0gyyArCDR70tN6NV37yxbTwVm2mVylHFfpTKjiVEKljiLDY1WsPE1jsP2am8mGvMOCCHMTKaYOiTrSO1mNx8E0cZt6JQVA_LvJDfohEnLUFcC-1LuHDpvYZ04gQoRk.0Rt2zEs5GJiBcWSTRMxMuNlH_9Prx69c8zJrawEP9V0&dib_tag=se&keywords=esp32%2Bnodemcu%2Baz-delivery&qid=1719564973&sprefix=esp32%2Bnodemcu%2Baz-deliver%2Caps%2C165&sr=8-3&th=1) | 119SEK |
| ESP32-CAM | [Amazon](https://www.amazon.se/ESP32-CAM-kameramodul-utvecklingskort-OV2640-OV7670/dp/B07WS3W52J/ref=sr_1_8?crid=9M6TCNEH1PDE&dib=eyJ2IjoiMSJ9.IUq3fecYMBqLQqtgIrLsAQN5FQk48qNhho0QUa9ueFvHIA4w4Cm6JY1tcAj9D47U-HHTf31PnlAP7CbTzHOg9qA6lnbQoOI8kySti6WeNUX6SErqF67VlLQ6k-PdffbA8OYVB3fGgfPbDs01IjGqTUxRxkLhu_tpueSc_YBB9tymxCshSRtyXdAH6ySbwu7C51gUAGG4GSJxgme8wd3KdWVzsABt_HcTh-hcAktQORA_tm0GoYWseieGt6GtOjC4xj-4-T8z5ICgztkpQJEizL5puicqXvwBblkrD6c4xiE.psHiWaLRVy-3-PO3KtJJgOb-B407Qq-zcC7r1FeBZFg&dib_tag=se&keywords=esp32+cam&qid=1719570410&sprefix=esp32+cam+%2Caps%2C144&sr=8-8) | 147SEK |
| FT232RL USB till TTL Seriell Adapter | [Amazon](https://www.amazon.se/dp/B01N9RZK6I?ref=ppx_yo2ov_dt_b_product_details&th=1) | 74SEK |
| 2x Soil moisture sensors | [Amazon](https://www.amazon.se/dp/B07V2BBVQR?ref=ppx_yo2ov_dt_b_product_details&th=1) | 109SEK for 3 |
| Jumper wires | [Amazon](https://www.amazon.se/dp/B01EV70C78?ref=ppx_yo2ov_dt_b_product_details&th=1) | 90SEK |
| Breadboard | [Electrokit](https://www.electrokit.com/en/kopplingsdack-400-anslutningar) | 49SEK |
| Relay | [Amazon](https://www.amazon.se/dp/B07VPKBRXF?psc=1&ref=ppx_yo2ov_dt_b_product_details) | 79SEK |
| Water pump | [Amazon](https://www.amazon.se/dp/B09SH3KLB9?psc=1&ref=ppx_yo2ov_dt_b_product_details) | 168SEK |
| Battery holder | [Amazon](https://www.amazon.se/dp/B0732ZX9CR?ref=ppx_yo2ov_dt_b_product_details) | 110SEK |
| Water tank | [Biltema](https://www.biltema.se/fritid/friluftsliv-och-camping/vattendunkar/vattendunk-20-liter-2000058554) | 90SEK |
| PVC Hose | [Biltema](https://www.biltema.se/bat/vvs/slangar/pvc-slangar/pvc-slang-5-m-x-12-mm-2000060033) | 55SEK |
| Hose connector | [Biltema](https://www.biltema.se/bil---mc/bilreservdelar/avgassystem/avgassystem-universala/slanganslutningar-68-st-2000047976) | 169SEK |

### ESP32

The ESP32 module is the controller that handles all the sensor data from the soil moisture sensors and processes it before sending to Adafruit IO. It is also responsible for signalling the waterpump to be activated.
<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/ESP32.png?raw=true" alt="Image" width="250" height="250">
</p>

### ESP32-CAM

The ESP32-CAM provides images of the plants to view online.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/ESP32-Cam.png?raw=true" alt="Image" width="250" height="250">
</p>

### FT232RL USB till TTL Seriell Adapter

The FT232RL adapter provides a way of programming the ESP32-CAM since it does not have it's own USB-port. By VCC, GND and UART pins from the CAM-board to the adapter we can plug it into the computer to program it.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/FT232RL.png?raw=true" alt="Image" width="250" height="250">
</p>

### Soil moisture sensors

The soil moistures sensors provide data to the ESP32 by measuring the capacitance of the soil. It does this by sending an analog signal to the controller which through it's analog to digital converter can give a digital value from 0-4095.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/sensors.png?raw=true" alt="Image" width="250" height="250">
</p>

### Jumper wires

Jumper wires are used to connect the different electrical components together, such as providing power to the moisture sensors and giving way for the analog signal back to the board.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/jumper-wires.png?raw=true" alt="Image" width="250" height="250">
</p>

### Breadboard

The solderless breadboard is a useful plastic block with a grid of electrical connections easily accessible through small holes. In this project it was used to aid in connecting the ESP32 to the sensors and the relay.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/breadboard.png?raw=true" alt="Image" width="250" height="250">
</p>

### Relay

The relay serves as a electronic switch to turn on and off the waterpump.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/relay.png?raw=true" alt="Image" width="250" height="250">
</p>

### Water pump

The waterpump is used to transport water from the tank to the plants.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/pump.png?raw=true" alt="Image" width="250" height="250">
</p>

### Battery holder

To provide 12v power to the waterpump i needed either a battery, battery holder or a transformer. I choose to go with a battery holder that holds 8AA batteries to provide power to the pump.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/battery-holder.png?raw=true" alt="Image" width="250" height="250">
</p>

### Water tank

For the waterpump I needed to have something to hold the water.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/water-tank.png?raw=true" alt="Image" width="250" height="250">
</p>

### PVC Hose

To move water from the tank to the plants i needed a hose to transport it in.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/pvc.png?raw=true" alt="Image" width="250" height="250">
</p>

### Hose connector

The hose connector serves to split the hose into two, one for each plant.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/hose-connector.png?raw=true" alt="Image" width="250" height="250">
</p>

## Computer setup

My first choice of IDE was Visual Studio Code and use PyMakr to upload the code. But after running into problems with PyMakr while trying to upload code to the ESP32-Cam, I decided to switch to Thonny.

### Development environment setup

1. Flashing micropython firmware to the boards.

    Download firmware from this [Link](https://micropython.org/download/ESP32_GENERIC/) and follow the instruction for how to flash the firmware onto the ESP32 board. \
    To make the board ready to flash you need to hold down the BOOT button. \
    Download the ESP32-Cam firmware from [this repository](https://github.com/lemariva/micropython-camera-driver). \
    Connect GPIO 0 to GND on the ESP32-Cam board to be able to flash the board.

2. Thonny

    Download and install [Thonny (here)](https://github.com/thonny/thonny/releases/download/v4.1.4/thonny-4.1.4.exe)

## Putting everything together


### Wiring

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/circuit.png?raw=true" alt="Image">
</p>

The circuit diagram is made on the online platform [Circuit Diagram](https://www.circuit-diagram.org/). The pinout on the ESP32 board and the ESP32-CAM board are not 100% accurate to the boards I have because they did not have these boards on the website. But the pins that are in use are accurate and describes reality well.

Both sensors aswell is connected to the ESP32 3.3V pin aswell as an ESP32 ground pin. The ESP32-Cam is connected to the 5V pin and a seperate GND pin. The soil moisture sensors are connected to GPIO 32 and GPIO 35 on the ESP32 board. GPIO 32 and GPIO 35 are two different channels on the ESP32 boards ADC1. It is important that the sensors are connected to the 3.3V output and not 5V. If connected to the 5V output the analog signal will be at a constant maximum at rest.

The waterpump positive wire is connected to the positive side of the battery pack. The negative side of the battery is connected into the relay modules COM port. The water pumps negative side is then connected to the relay modules NO (Normally Open) side.

The 5V output of the ESP32 is then connected to DC+ on the relay module and DC- is connected to another GND pin on the ESP32 board. The IN port of the relay module is then connected to GPIO 26 pin of the ESP32 board to allow the board to send a high signal to the relay module.

## Platform

Since I wanted to expirement with an image feed i went looking for one that could support it. My choice came to be Adafruit IO since they could display images if sent as Base64 image data strings. It is also a cloud platform so the setup was much more straightforward than a self-hosted option. Self-hosted options were of interest but the scope of my project i chose to make it simpler when other parts took more time.

Adafruit IO offers multiple different options for displaying your data. I chose line charts to show data history from the moisture sensors and a gauge to show current value from the moisture sensors. I also set up an image feed for the images sent from the ESP32-CAM.

## The code

The following code is in the boot.py file for both the ESP32 and the ESP32-CAM and it connects to my WiFi at home.
```py
import network
import secrets
from utime import sleep

network.WLAN(network.AP_IF).active(False) # Make sure access point interface is inactive
sta_if = network.WLAN(network.STA_IF)     # Create instance of the station interface

if not sta_if.isconnected():              # Check if connection already established
    print("Connecting to the network...")  
    sta_if.active(True)                   # Activate station interface

    sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD) # Connect to WiFi
    print('Waiting for connection...', end='') 

    while not sta_if.isconnected() and sta_if.status() >= 0: # Wait for connection
        print('.', end='')
        sleep(1)
    
    adress = sta_if.ifconfig()[0] # Retrieve and print device ip-adress
    print("\nConnected to WiFi with adress {}".format(adress))
```
First we make sure that the Access Point interface of the board isn't active. Then we create an instance of the station interface. If the interface isn't connected to a network we will make sure the station interface is active and then proceed to connect to my home WiFi using the right credentials. When connected, the device IP-adress is printed. 

### Camera

The following is the code for processing images on the ESP32-CAM board. This process is done over and over in a loop.
```py
camera.init(0, format=camera.JPEG, framesize=camera.FRAME_HVGA)
buffer = camera.capture()
print("Size of image is " + str(len(buffer)) + "bytes")
data = base64.b64encode(buffer) # Encode image to base64
data = data.decode("utf-8")     # decode base64 bytes to a base64 string
camera.deinit()
```
The object "camera" is initialized by setting format and framesize. A picture is then captured and stored in a buffer. The size of the buffer is printed on the serial feed. The picture is then finally encoded to the base64 format and then converted from base64 bytes to a base64 string. And before doing it in the next iteration of the loop, we deinitialize the camera.

### Controller

The first thing the controller does in it's main loop is decide if it should water the plants or not.
```py
current_time = utime.localtime(utime.time() + (2 * 3600))
if (current_time[3] == 12 and current_time[4] == 00):
    WaterPlants()
```
It does so every day at noon and the watering process is quite simple. 
```py
def WaterPlants():
    pump.value(1)
    utime.sleep(6)
    pump.value(0)
    utime.sleep(60) # Sleep for 60 seconds to avoid activating function again on the same day. 
```
Turn the waterpump on by signalling the relay. Wait 6seconds and turn the relay off, Sleep for another minute to avoid calling the watering function one more time. 

To gather sensor data i took 10 readings over a period of 5 seconds to avoid noise in readings.
```py
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
```
I then called a function called CalculateMoisture that gives back a value that compares the sensor to calibrated readings.
```py
def CalculateMoisture(chives, dill):
    chives_moisture = (MAX_CHIVES - chives) / CHIVES_DIFF	# Scale the sensor readings. 0 value means dry, 1 mean completely wet.
    dill_moisture = (MAX_DILL - chives) / DILL_DIFF
    return (chives_moisture * 100, dill_moisture * 100)		# Put moisture value in percentage form.
```
To get calibrate the sensors I measured it's reading when the sensor was completely dry and when the sensor was complety dipped in glass of water. 

## Transmitting the data

Both the camera module and the controller are connected to the internet through WiFi. The data is then transmitted to three different feeds on Adafruit IO via their Web API and the data is sent using JSON format.

For both the camera feed and the plant moisture, data is sent every 15 seconds to their different feeds. 

### Camera

After the camera takes an image and process it to the correct base64 format it calls a function SendData.
```py
response = SendData(data, secrets.AIO_CAMERA_FEED)
```
```py
def SendData(value, feed):
    headers = { "X-AIO-Key": secrets.AIO_KEY, "Content-Type": "application/json"}
    data = BuildJSON(value)
    return requests.post(feed, json=data, headers=headers)
```
SendData is responsible for sending the correct http-request by adding the Adafruit IO key and the correct content type as headers.

### Controller 

The controller sends it's data the same way by calling the same SendData function.
```py
SendData(str(dill_moisture), secrets.AIO_PLANT1_FEED)
SendData(str(chives_moisture), secrets.AIO_PLANT2_FEED)
```

## Presenting the data

The data is presented on a dashboard on io.adafruit.com.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/dashboard.png?raw=true" alt="Image" width="800">
</p>

Here, the data is presented in three different formats. For the current value of the sensors, it is displayed with gauges.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/gauges.png?raw=true" alt="Image" width="800">
</p>

With these values it should be noted that it resresents how close the value is reading to the reading 100% in water, it does not however represent being above 90% actual moisture in the soil. 

The sensor data is also presented in line charts to provide some history. 

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/charts.png?raw=true" alt="Image" width="800">
</p>

And finally we have an image feed displaying the latest sent image from the camera. 

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/image-feed.png?raw=true" alt="Image" width="800">
</p>

## Finalizing the design

Finally the project is done, and this is what it looks like.

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/final1.jpg?raw=true" alt="Image" width="450">
</p>

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/final2.jpg?raw=true" alt="Image" width="450">
</p>

<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/final3.jpg?raw=true" alt="Image" width="450">
</p>