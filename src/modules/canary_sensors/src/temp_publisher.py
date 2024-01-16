#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import time
import board
import adafruit_tmp117

def temp_publisher():
    # Initialize the ROS publisher for the 'temp_topic' with Float32 messages
    pub = rospy.Publisher('temp_topic', Float32, queue_size=10)
    
    # Initialize the ROS node as 'tmp117_publisher' and allow multiple nodes with the same name
    rospy.init_node('tmp117_publisher', anonymous=True)
    
    # Set the publishing rate to 1 Hz
    rate = rospy.Rate(1)
    
    # Log a message indicating that the publisher node has started
    rospy.loginfo("Publisher Node Started, now publishing messages")

    # Initialize I2C communication and create a TMP117 sensor object
    i2c = board.I2C()  # I2C interface using board.SCL and board.SDA
    tmp117 = adafruit_tmp117.TMP117(i2c)

    # Main loop for continuously publishing temperature readings
    while not rospy.is_shutdown():
        # Read the temperature from the TMP117 sensor
        temperature = tmp117.temperature
        
        # Log the temperature to the console for debugging
        rospy.loginfo("Temperature: %.2f degrees C", temperature)
        
        # Publish only the numerical temperature value to the 'temp_topic'
        pub.publish(temperature)

        rate.sleep()

if __name__ == '__main__':
    try:
        # Call the temperature publisher function
        temp_publisher()
    except rospy.ROSInterruptException:
        # Handle a ROS interrupt exception 
        pass
