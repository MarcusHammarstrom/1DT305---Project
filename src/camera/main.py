# main.py -- put your code here!

import camera
import utime

while True:
    try: 
        print("Taking a photo in 10 seconds")
        utime.sleep(10)
        camera.init(0, format=camera.JPEG)
        buffer = camera.capture()
        print("Size of image is " + str(len(buffer)) + "bytes")
        file_path = "img.jpg"
        file = open(file_path, "w")
        file.write(buffer)
        file.close()
    except Exception as e:
        print("Something went wrong")
        print(str(e))
    camera.deinit()
