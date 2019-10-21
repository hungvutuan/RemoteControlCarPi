#!/usr/bin/env python
import random
import motor
# import led

from flask import Flask, render_template, Response, request, jsonify

"""import camera driver"""
# import os
# from importlib import import_module
# if os.environ.get('CAMERA'):
#     Camera = import_module('camera_' + os.environ['CAMERA']).Camera
# else:
#     from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera import Camera

app = Flask(__name__)
app.secret_key = "vth"

LEFT, RIGHT, FORWARD, BACKWARD, STOP = "left", "right", "forward", "backward", "stop"
AVAILABLE_COMMANDS = {
    'Left': LEFT,
    'Forward': FORWARD,
    'Right': RIGHT,
    'Backward': BACKWARD,
    'Stop': STOP
}


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html', commands=AVAILABLE_COMMANDS)


def gen(camera):
    while True:
        """This function generates the frame for displaying the video. The 'yield' increments the iteration by the 
        next, therefore, the image overlaps. The frame variable is used later in the function video_feed()"""
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


@app.route('/<cmd>')
def command(cmd=None):
    if cmd == STOP:
        # led.led_stop()
        motor.stop()
    elif cmd == FORWARD:
        # led.led_off()
        motor.forward()
    elif cmd == BACKWARD:
        # led.led_off()
        motor.backward()
    elif cmd == LEFT:
        # led.led_left()
        motor.left()
    elif cmd == RIGHT:
        # led.led_right()
        motor.right()
    return "Success", 200, {'Content-Type': 'text/plain'}


@app.route('/log_out')
def shutdown_server():
    """Send a request to shutdown werkzeug server and load the signing out page"""
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return render_template("log_out.html")


def dist():             # alternative for led.distance()
    return (random.random())*100


@app.route('/get_dist/', methods=['GET', 'POST'])
def get_dist():
    if request.method == 'GET':
        request.args.get('dist', default=0, type=int)
        # Run this for Raspberry Pi
        # return jsonify(result=led.distance())
        # Debug
        return jsonify(result=dist())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True, threaded=True)
