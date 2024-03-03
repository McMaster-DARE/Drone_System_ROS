#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
import time
import board
import adafruit_bno055

def IMU_publisher():
    # Initialize the ROS publisher for the 'IMU_topic' with Float32 messages
    accel_pub = rospy.Publisher('accelerometer_topic', Float32MultiArray, queue_size=10)
    gyro_pub = rospy.Publisher('gyro_topic', Float32MultiArray, queue_size=10)
    grav_pub = rospy.Publisher('grav_topic', Float32MultiArray, queue_size=10)
    
    # Initialize the ROS node as 'IMU_publisher' and allow multiple nodes with the same name
    rospy.init_node('IMU_publisher', anonymous=True)
    
    # Set the publishing rate to 1 Hz
    rate = rospy.Rate(1)
    
    # Log a message indicating that the publisher node has started
    rospy.loginfo("Publisher Node Started, now publishing messages")

    # Initialize I2C communication and create a BNO055 sensor object
    i2c = board.I2C()  # I2C interface using board.SCL and board.SDA
    sensor = adafruit_bno055.BNO055_I2C(i2c)

    # Main loop for continuously publishing readings
    while not rospy.is_shutdown():

        # Read the IMU values from the bno055 sensor 
	# can also get: temp, magnetic, euler, quaternion, linear accel         
        ax,ay,az = sensor.acceleration
        p,r,y = sensor.gyro
        gx,gy,gz = sensor.gravity

	
        # Log the temperature to the console for debugging      
        rospy.loginfo("Accelerometer, X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} (m/s^2)".format(ax,ay,az))               
        rospy.loginfo("Gyroscope,  X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} (rad/sec)".format(p,r,y))               
        rospy.loginfo("Gravity,  X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} (m/s^2)".format(gx,gy,gz))  
              

	# Format into a 32bit FloatArray
        acceleration = Float32MultiArray(data=[ax,ay,az])
        gyro = Float32MultiArray(data=[p,r,y])
        gravity = Float32MultiArray(data=[gx,gy,gz])

        # Publish only the numerical temperature value to the 'IMU_topic'
        
        accel_pub.publish(acceleration)
        gyro_pub.publish(gyro)
        grav_pub.publish(gravity)

        rate.sleep()

if __name__ == '__main__':
    try:
        # Call the IMU publisher function
        IMU_publisher()
    except rospy.ROSInterruptException:
        # Handle a ROS interrupt exception 
        pass
