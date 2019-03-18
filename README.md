## Raspberry Pi Live Cam

![My Pi!](https://github.com/healeycodes/Raspberry-Pi-Live-Cam/blob/master/my-pi-320.png)

This repository hosts all the files for my tutorial on building a live cam with your Raspberry Pi.

The web app is built with Flask and the Raspberry Pi script is written in Python 3 using the `picamera` module.

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

📷

<br>

#### License

Standard MIT.
