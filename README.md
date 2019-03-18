## Raspberry Pi Live Cam

![My Pi!](https://github.com/healeycodes/Raspberry-Pi-Live-Cam/blob/master/my-pi-320.png)

This repository hosts all the files for my tutorial on building a live cam with your Raspberry Pi.

The web app is built with Flask and the Raspberry Pi script is written in Python using the `picamera` module.

### Install

#### Server

`pip install -r requirements.txt`

`PASSWORD='123'`

`FLASK_APP=app.py flask run`

#### Raspberry Pi

No `requirements.txt` as it may depend on your distro.

`pip install requests`

`pip install picamera`

Edit the `url` variable in `camera.py` to your Flask app's address/port.

`python camera.py`

<br>

📷

<br>

#### License

Standard MIT.
