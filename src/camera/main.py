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

def SendData(value):
    headers = { "X-AIO-Key": secrets.AIO_KEY, "Content-Type": "application/json"}
    data = BuildJSON(value)
    return requests.post(secrets.AIO_CAMERA_FEED, json=data, headers=headers)

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
        response = SendData(data)
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
    camera.deinit()
