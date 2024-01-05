#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

""" Display magnetometer data once per second """

import time
import board
#module from the Adafruit CircuitPython library for interacting with the LIS3MDL magnetometer sensor.
import adafruit_lis3mdl

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lis3mdl.LIS3MDL(i2c)

while True:
    #  reads the magnetic field values along the X, Y, and Z axes from the LIS3MDL sensor 
    # and assigns them to the variables mag_x, mag_y, and mag_z.
    mag_x, mag_y, mag_z = sensor.magnetic

    # prints the formatted magnetic field values to the console, specifying the format for floating-point 
    # numbers with two decimal places
    print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT".format(mag_x, mag_y, mag_z))
    print("")
    time.sleep(1.0)
