# DARE_ROS

### This project provides Python scripts for reading data from different sensors on a Raspberry Pi and then publishing that information onto ROS topics. The supported sensors include a Radiation sensor, a Magnetometer, and a Temperature sensor. These scripts can be used to read data from the sensors and integrate them into your projects.

## 'RadSens.py' and 'rad_publisher.py' (Radiation Sensor)
* Converts the CG_RadSens library to CircuitPython for use on a Raspberry Pi Pico.
* Communicates with the RadSens device over I2C.
* Reads radiation-related parameters such as chip ID, firmware version, radiation intensity (dynamic and static), pulse count, and more.
* Provides methods to control the sensor, set configurations, and retrieve sensor information.
* Publishes continuous radiation sensor readings (dynamic intensity, static intensity, pulse count) to 'rad_topic' using ROS.

## 'LIS3MDL.py' and 'mdl_publisher.py' (Magnetometer)
* Utilizes the Adafruit LIS3MDL library to interface with the LIS3MDL magnetometer sensor.
* Reads magnetic field values along the X, Y, and Z axes from the LIS3MDL sensor.
* Prints the formatted magnetic field values to the console once per second.
* Publishes continuous LIS3MDL magnetometer readings (X, Y,Z) to 'mdl_topic' using ROS at a rate.

## 'TMP117.py' (Magnetometer)
* Uses the Adafruit TMP117 library to interact with the TMP117 temperature sensor.
* Monitors the temperature readings from the sensor.
* Integrates a simple recording functionality triggered by a push button, logging time and temperature to a file ("myfile.txt") when the button is pressed.
* Publishes continuous temperature readings in Celsius from a TMP117 sensor to 'temp_topic' using ROS.


  
