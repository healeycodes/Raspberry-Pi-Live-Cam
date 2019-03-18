import io
import time
import picamera

framerate = 90
quality = 100
resolutions = [(1920, 1080), (1280, 720), (800, 600), (640, 480), (320, 240)]
samples = 50
with picamera.PiCamera(framerate=framerate) as camera:
    time.sleep(2)  # camera warm-up time
    for res in resolutions:
        camera.resolution = res
        timer = time.time()
        sum_time = 0
        for _ in range(0, samples):
            image = io.BytesIO()
            camera.capture(image, 'jpeg', quality=quality, use_video_port=True)
            sum_time += time.time() - timer
            timer = time.time()
        print(res)
        print(sum_time / samples)
