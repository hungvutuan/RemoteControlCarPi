#!/usr/bin/env python
from importlib import import_module
from flask import Flask, render_template, Response
import os
from importlib import import_module


# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera


app = Flask(__name__)


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


def gen(camera):
    while True:
        """This function generates the frame for displaying the video. The 'yield' increments the iteration by the 
        next, therefore, the image overlaps. The frame variable is used later in the function video_feed() """
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """This function streams the images on the frame, with the next one overlapping and replacing the former. This is
    achieved by setting mimetype to 'multipart/x-mixed-replace'. The idea is that by replacing the image with another
    so quickly, it'd look like a video."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
