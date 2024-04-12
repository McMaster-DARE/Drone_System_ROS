#!/usr/bin/python

import RPi.GPIO as gpio
import subprocess
import time

gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.IN, pull_up_down = gpio.PUD_UP)

def handle_button_press(channel):
    subprocess.call(["python", "$(find canary_bringup)/launch/bringup.launch"])

gpio.add_event_detect(5, gpio.FALLING, callback = handle_button_press, bouncetime=300)

while True:
    time.sleep(360)