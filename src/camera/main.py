# main.py -- put your code here!

import camera
import utime
import base64
import secrets
import urequests as requests
import gc

def BuildJSON(value):
    data = { "value": value }
    return data

def SendData(value, feed):
    headers = { "X-AIO-Key": secrets.AIO_KEY, "Content-Type": "application/json"}
    data = BuildJSON(value)
    return requests.post(feed, json=data, headers=headers)

camera.init(0, format=camera.JPEG, framesize=camera.FRAME_HVGA)

while True:
    try: 
        utime.sleep(15)
        print("Taking a photo in 15 seconds")
        buffer = camera.capture()
        print("Size of image is " + str(len(buffer)) + "bytes")
        data = base64.b64encode(buffer) # Encode image to base64
        del buffer
        gc.collect()					# Free buffer mem
        data = data.decode("utf-8")     # decode base64 bytes to a base64 string
        response = SendData(data, secrets.AIO_CAMERA_FEED)
        del data
        gc.collect()
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Failed to send data")
        del response
        gc.collect()
    except Exception as e:
        print("Something went wrong")
        print(str(e))
        del e
        gc.collect()
