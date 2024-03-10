#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu
import time
import board
import adafruit_bno055

def create_vector3(p):
    v = Vector3()
    v.x = p[0]
    v.y = p[1]
    v.z = p[2]
    
    return v

def IMU_publisher():
    # Initialize the ROS publisher for the 'IMU_topic' with Imu messages
    imu_pub = rospy.Publisher('/imu/data', Imu, queue_size=10)
    
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
    i.orientation_covariance = [0.0, 0.0,0.0,
    				 0.0, 0.0, 0.0,
    				 0.0, 0.0, 0.0,]
    i.angular_velocity_covariance = [0.0, 0.0,0.0,
    				 0.0, 0.0, 0.0,
    				 0.0, 0.0, 0.0,]
    i.linear_acceleration_covariance = [0.0, 0.0,0.0,
    				 0.0, 0.0, 0.0,
    				 0.0, 0.0, 0.0,]

    # Main loop for continuously publishing readings
    while not rospy.is_shutdown():

        # Read the IMU values from the bno055 sensor 
        # can also get: temp, magnetic, euler, quaternion, linear accel  
        q = sensor.quaternion
        gy = sensor.gyro
        acc = sensor.linear_acceleration
        
        
        i.header.stamp = rospy.Time.now()
        i.header.frame_id = 'imu_frame'
        i.orientation = Quaternion(q[0], q[1], q[2], q[3])
        i.angular_velocity = create_vector3(gy)
        i.linear_acceleration = create_vector3(acc)
          
        # Log the temperature to the console for debugging                    
        #rospy.loginfo("Orientation: %s", i.orientation)
        #rospy.loginfo("Angular Velocity: %s", i.angular_velocity)
        #rospy.loginfo("Linear Acceleration: %s", i.linear_acceleration)
             

        # Publish only the numerical temperature value to the 'IMU_topic'
        try:
            imu_pub.publish(i)
        except struct.error:
            continue
        rate.sleep()

if __name__ == '__main__':
    try:
        # Call the IMU publisher function
        IMU_publisher()
    except rospy.ROSInterruptException:
        # Handle a ROS interrupt exception 
        pass
