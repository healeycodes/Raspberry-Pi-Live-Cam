import io
import time
import json
import base64
import requests
import picamera

url = 'http://192.168.1.100:5000/?password=123'

framerate = 90
quality = 100
res = (1280, 720)
with picamera.PiCamera(framerate=framerate, resolution=res) as camera:
    time.sleep(2)  # camera warm-up time
    while True:
        try:
            image = io.BytesIO()
            camera.capture(image, 'jpeg', quality=quality, use_video_port=True)
            r = requests.post(url, data=image.getvalue())
            # place a `time.sleep` here if you want a slower livecam
        except:
            time.sleep(5)  # wait for WiFi/server to come back
