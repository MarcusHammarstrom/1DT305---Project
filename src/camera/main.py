# main.py -- put your code here!

import camera
import utime

camera.init(0, format=camera.JPEG)

while True:
    print("Taking a photo in 5 seconds")
    utime.sleep(5)
    try: 
        buffer = camera.capture()
        print("Size of image is " + len(buffer) + "bytes")
        file_path = "img.jpg"
        file = open(file_path, "w")
        file.write(buffer)
        file.close()
    except:
        print("Something went wrong")