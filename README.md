## Raspberry Pi Live Cam

![My Pi!](https://github.com/healeycodes/Raspberry-Pi-Live-Cam/blob/master/my-pi-320.png)

This repository hosts all the files for my coding [tutorial](https://healeycodes.com/python/raspberrypi/beginners/webdev/2019/03/18/raspberry-pi-live-cam.html) on building a live cam with your Raspberry Pi.

- Flask Web App: `app.py`
- Raspberry Pi Script: `camera.py`

<br>

There's also a camera benching script `benchcamera.py` that was used during testing.

- 7.5fps at 720p - JPEG 100 quality.

<br>

#### Web App

Install dependencies `pip install -r requirements.txt`. Set the password for the image upload route `PASSWORD='123'`.

Test the app locally with `FLASK_APP=app.py flask run`. See the Flask [docs](http://flask.pocoo.org/) for hosting on a web server.

<br>

#### Raspberry Pi

No `requirements.txt` as it may depend on your distro - although, this should be bulletproof. Install dependencies `pip install picamera requests`. Edit the `url` variable in `camera.py` to your Flask app's address/port.

There are also some commented variables for adjusting resolution and capture rate (use `time.sleep` for highest accuracy).

The Raspberry Pi side of things works fine in testing with Python 2.7 but was written for Python 3.

Run with `python camera.py`. 

<br>

#### Possible Improvements

Some thoughts to improve the project but make it a worse tutorial.

- Upload images via WebSocket (save bandwidth and latency).
- Use a safe compare function for password checking to avoid timing attacks.
- Serve images to clients over WebSocket as they arrive (same as above).
- Use Flask for uploading images, serve images as a static file via HTTP server (scales infinitely).
- When receiving images, scale them to different resolutions (e.g., `/live800x600.jpeg`).

<br>

📷

<br>

#### License

Standard MIT.
