# main.py -- put your code here!

import camera
import utime
import base64
import secrets
from mqtt import MQTTClient
import gc

def SendData(value):
    url = "https://io.adafruit.com/api/v2/MarcusHammarstrom/feeds/plant-camera/data"
    headers = {"X-AIO-Key": secrets.AIO_KEY, "Content-Type": "application/json"}
    data = BuildJSON(value)
    print(value)
    return requests.post(url=url, headers=headers, json=data)
    
def BuildJSON(value):
    data = { "value": value }
    print(str(data))
    return data

client = MQTTClient(secrets.AIO_CLIENT_ID, secrets.AIO_SERVER, secrets.AIO_PORT, secrets.AIO_USER, secrets.AIO_KEY, 60)
client.connect()

while True:
    try: 
        print("Taking a photo in 15 seconds")
        utime.sleep(15)
        camera.init(0, format=camera.JPEG, framesize=camera.FRAME_HVGA)
        buffer = camera.capture()
        print("Size of image is " + str(len(buffer)) + "bytes")
        data = base64.b64encode(buffer) # Encode image to base64
        del buffer
        gc.collect()					# Free buffer mem
        data = data.decode("utf-8")     # decode base64 bytes to a base64 string
        client.publish(topic=secrets.AIO_CAMERA_FEED, msg=data, qos=1)
        del data
        gc.collect()
    except Exception as e:
        print("Something went wrong")
        print(str(e))
        del e
        gc.collect()
    camera.deinit()
