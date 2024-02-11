#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
import time
import board
import adafruit_bno055

def IMU_publisher():
    # Initialize the ROS publisher for the 'IMU_topic' with Float32 messages
    pub = rospy.Publisher('IMU_topic', Float32, queue_size=10)
    
    # Initialize the ROS node as 'IMU_publisher' and allow multiple nodes with the same name
    rospy.init_node('IMU_publisher', anonymous=True)
    
    # Set the publishing rate to 1 Hz
    rate = rospy.Rate(1)
    
    # Log a message indicating that the publisher node has started
    rospy.loginfo("Publisher Node Started, now publishing messages")

    # Initialize I2C communication and create a BNO055 sensor object
    i2c = board.I2C()  # I2C interface using board.SCL and board.SDA
    IMUsens = adafruit_bno055.BNO055_I2C(i2c)
    
    # Initialize the sensor
    if IMUsens.init():
       print("BNO055 initialized successfully!")
    else:
       print("Failed to initialize BNO055!")
       while True:
          pass  # Halt execution

    # Main loop for continuously publishing readings
    while not rospy.is_shutdown():

         # Read the IMU values from the bno055 sensor
        
        temperature = sensor.temperature
        acceleration = sensor.acceleration
        magneticData = sensor.magnetic
        gyro = sensor.gyro
        euler = sensor.euler
        quaternion = sensor.quaternion
        linear_Accel = sensor.linear_acceleration
        gravity = sensor.gravity

        # Log the temperature to the console for debugging
        rospy.loginfo("Temperature: {} degrees C".format(temperature))        
        rospy.loginfo("Accelerometer (m/s^2): {}".format(acceleration))        
        rospy.loginfo("Magnetometer (microteslas): {}".format(magneticData))        
        rospy.loginfo("Gyroscope (rad/sec): {}".format(gyro))        
        rospy.loginfo("Euler angle: {}".format(euler))        
        rospy.loginfo("Quaternion: {}".format(quaternion))        
        rospy.loginfo("Linear acceleration (m/s^2): {}".format(linear_Accel))        
        rospy.loginfo("Gravity (m/s^2): {}".format(gravity))        

        # Publish only the numerical temperature value to the 'IMU_topic'
        pub.publish(temperature)
        pub.publish(acceleration)
        pub.publish(magneticData)
        pub.publish(gyro)
        pub.publish(euler)
        pub.publish(quaternion)
        pub.publish(linear_Accel)
        pub.publish(gravity)

        rate.sleep()

if __name__ == '__main__':
    try:
        # Call the IMU publisher function
        IMU_publisher()
    except rospy.ROSInterruptException:
        # Handle a ROS interrupt exception 
        pass
