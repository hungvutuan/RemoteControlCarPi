import time
import RPi.GPIO as GPIO

# GPIO Mode
GPIO.setmode(GPIO.BCM)
# Set GPIO Pins
LED_L = 2
LED_R = 4
# Set GPIO Pins
TRIG = 18
ECHO = 24
LED = 23
LED_S = 3
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
# LED setup
GPIO.setup(LED_L, GPIO.OUT)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED_S, GPIO.OUT)


def led_off():
    GPIO.output(LED_L, GPIO.LOW)
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_S, GPIO.LOW)


def led_left():
    GPIO.output(LED_L, GPIO.HIGH)
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_S, GPIO.LOW)


def led_right():
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_L, GPIO.LOW)
    GPIO.output(LED_S, GPIO.LOW)


def led_stop():
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_L, GPIO.LOW)
    GPIO.output(LED_S, GPIO.HIGH)


def distance():
    GPIO.output(TRIG, False)
    time.sleep(0.1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start = time.time()
    stop = time.time()

    # Save StartTime
    while GPIO.input(ECHO) == 0:
        start = time.time()

    # Save StopTime
    while GPIO.input(ECHO) == 1:
        stop = time.time()
    return (stop - start) / 0.000058  # cm


def measure():
    try:
        while True:
            dist = distance()
            print("Distance: %.2f cm" % dist)
            if dist < 15:
                GPIO.output(LED, GPIO.HIGH)
            else:
                GPIO.output(LED, GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stop measurement")
        GPIO.cleanup()
