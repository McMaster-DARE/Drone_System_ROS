#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
import time
import board
import adafruit_bno055 as bn

print(bn.__version__)
