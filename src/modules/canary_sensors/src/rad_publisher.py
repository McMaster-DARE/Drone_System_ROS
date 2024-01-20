#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
import time
import board
from canary_sensors.RadSens import CG_RadSens

def rad_publisher():
    # Initialize the ROS publisher for the 'temp_topic' with Float32 messages
    pub = rospy.Publisher('rad_topic', Float32MultiArray, queue_size=10)
    
    # Initialize the ROS node as 'tmp117_publisher' and allow multiple nodes with the same name
    rospy.init_node('radsens_publisher', anonymous=True)
    
    # Set the publishing rate to 1 Hz
    rate = rospy.Rate(1)
    
    # Log a message indicating that the publisher node has started
    rospy.loginfo("Publisher Node Started, now publishing messages")

    # Initialize I2C communication and create a TMP117 sensor object
    i2c = board.I2C()  # I2C interface using board.SCL and board.SDA
    radsens = CG_RadSens(i2c)
    
    # Initialize the sensor
    if radsens.init():
       print("CG_RadSens initialized successfully!")
    else:
       print("Failed to initialize CG_RadSens!")
       while True:
          pass  # Halt execution

    # Main loop for continuously publishing readings
    while not rospy.is_shutdown():
        # Read the data from the RadSens
        dynamic_intensity = radsens.get_rad_intensy_dynamic()
        static_intensity = radsens.get_rad_intensy_dynamic()
        num_pulses = radsens.get_number_of_pulses()
        
        # Log the data to the console for debugging
        rospy.loginfo("Dynamic Intensity: %.2f uR/h", dynamic_intensity)
        rospy.loginfo("Static Intensity: %.2f uR/h", static_intensity)
        rospy.loginfo("Number of Pulses: %.2f", num_pulses)
        
        # Assemble data into an array
        rad_data = Float32MultiArray(data=[dynamic_intensity, static_intensity, num_pulses])
        
        # Publish only the numerical temperature value to the 'temp_topic'
        pub.publish(rad_data)

        rate.sleep()

if __name__ == '__main__':
    try:
        # Call the temperature publisher function
        rad_publisher()
    except rospy.ROSInterruptException:
        # Handle a ROS interrupt exception 
        pass
