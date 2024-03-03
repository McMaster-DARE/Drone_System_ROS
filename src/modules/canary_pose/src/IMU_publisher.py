#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu
import time
import board
import adafruit_bno055


def IMU_publisher():
    # Initialize the ROS publisher for the 'IMU_topic' with Float32 messages
    imu_pub = rospy.Publisher('/imu', Imu, queue_size=10)
    
    # Initialize the ROS node as 'IMU_publisher' and allow multiple nodes with the same name
    rospy.init_node('IMU_publisher', anonymous=True)
    
    # Set the publishing rate to 1 Hz
    rate = rospy.Rate(1)
    
    # Log a message indicating that the publisher node has started
    rospy.loginfo("Publisher Node Started, now publishing messages")

    # Initialize I2C communication and create a BNO055 sensor object
    i2c = board.I2C()  # I2C interface using board.SCL and board.SDA
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    
    i = Imu()

    # Main loop for continuously publishing readings
    while not rospy.is_shutdown():

        # Read the IMU values from the bno055 sensor 
        # can also get: temp, magnetic, euler, quaternion, linear accel  
        i.header.stamp = rospy.Time.now()
        i.header.frame_id = ''
        i.orientation = sensor.quaternion  
        i.angular_velocity = sensor.gyro
        i.linear_acceleration = sensor.linear_acceleration   
          
        # Log the temperature to the console for debugging                    
        rospy.loginfo("Orientation: %s", i.orientation)
        rospy.loginfo("Angular Velocity: %s", i.angular_velocity)
        rospy.loginfo("Linear Acceleration: %s", i.linear_acceleration)
             

        # Publish only the numerical temperature value to the 'IMU_topic'
        
        imu_pub.publish(i)

        rate.sleep()

if __name__ == '__main__':
    try:
        # Call the IMU publisher function
        IMU_publisher()
    except rospy.ROSInterruptException:
        # Handle a ROS interrupt exception 
        pass
