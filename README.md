# Plant automation

Marcus Hammarström / mh226yz

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

The ESP32-CAM provides images of the plants to view online. \
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

Jumper wires are used to connect the different electrical components together, such as providing power to the moisture sensors and giving way for the analog signal back to the board. \
<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/jumper-wires.png?raw=true" alt="Image" width="250" height="250">
</p>

### Breadboard

The solderless breadboard is a useful plastic block with a grid of electrical connections easily accessible through small holes. In this project it was used to aid in connecting the ESP32 to the sensors and the relay.
<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/breadboard.png?raw=true" alt="Image" width="250" height="250">
</p>

### Relay

The relay serves as a electronic switch to turn on and off the waterpump. \
<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/relay.png?raw=true" alt="Image" width="250" height="250">
</p>

### Water pump

The waterpump is used to transport water from the tank to the plants. \
<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/pump.png?raw=true" alt="Image" width="250" height="250">
</p>

### Battery holder

To provide 12v power to the waterpump i needed either a battery, battery holder or a transformer. I choose to go with a battery holder that holds 8AA batteries to provide power to the pump. \
<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/battery-holder.png?raw=true" alt="Image" width="250" height="250">
### </p>
Water tank

For the waterpump I needed to have something to hold the water. \
<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/water-tank.png?raw=true" alt="Image" width="250" height="250">
</p>

### PVC Hose

To move water from the tank to the plants i needed a hose to transport it in. \
<p align="center">
    <img src="https://github.com/MarcusHammarstrom/1DT305---Project/blob/main/img/pvc.png?raw=true" alt="Image" width="250" height="250">
</p>

### Hose connector

The hose connector serves to split the hose into two, one for each plant. \
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

Both sensors aswell as the ESP32-Cam is connected to the ESP32 3.3V pin aswell as an ESP32 ground pin. The soil moisture sensors are connected to GPIO 32 and GPIO 35 on the ESP32 board. GPIO 32 and GPIO 35 are two different channels on the ESP32 boards ADC1.

The waterpump positive wire is connected to the positive side of the battery pack. The negative side of the battery is connected into the relay modules COM port. The water pumps negative side is then connected to the relay modules NO (Normally Open) side.

The 5V output of the ESP32 is then connected to the 

## Platform

## The code

## Transmitting the data

## Presenting the data

## Finalizing the design