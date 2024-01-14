#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
import time
import board
import adafruit_lis3mdl

def mdl_publisher():
    # Initialize the ROS publisher for the 'mdl_topic' with Float32 messages
    pub = rospy.Publisher('mdl_topic', Float32MultiArray, queue_size=10)
    
    # Initialize the ROS node as 'mdl_publisher' and allow multiple nodes with the same name
    rospy.init_node('mdl_publisher', anonymous=True)
    
    # Set the publishing rate to 1 Hz
    rate = rospy.Rate(1)
    
    # Log a message indicating that the publisher node has started
    rospy.loginfo("Publisher Node Started, now publishing messages")

    # Initialize I2C communication and create a LIS3MDL sensor object
    i2c = board.I2C()  # I2C interface using board.SCL and board.SDA
    sensor = adafruit_lis3mdl.LIS3MDL(i2c)

    # Main loop for continuously publishing temperature readings
    while not rospy.is_shutdown():
        # Read the magnetic field values from the LIS3MDL sensor
        mag_x, mag_y, mag_z = sensor.magnetic

        # Log the temperature to the console for debugging
        rospy.loginfo("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT".format(mag_x, mag_y, mag_z) )
        
        mag_data = Float32MultiArray(data=[mag_x, mag_y, mag_z])
        
        # Publish only the numerical temperature value to the 'temp_topic'
        pub.publish(mag_data)

        rate.sleep()

if __name__ == '__main__':
    try:
        # Call the Magnometer publisher function
        mdl_publisher()
    except rospy.ROSInterruptException:
        # Handle a ROS interrupt exception 
        pass
