#!/usr/bin/env python
import rospy
import subprocess
import os
from rostopic import get_topic_class

def topic_exists(topic_name):
    """
    Check if the topic exists and is being published.
    """
    try:
        get_topic_class(topic_name)
        return True
    except Exception as e:
        return False

def launch_recording_launch_file(launch_file, topic_name, bag_file_name):
    """
    Launch a ROS launch file to start recording the topic.
    """
    command = ["roslaunch", "canary_lidar", launch_file, 
               "topic:=" + topic_name, "bag_file_name:=" + bag_file_name]
    subprocess.Popen(command)
    rospy.loginfo(f"Launched {launch_file} for recording topic {topic_name} into bag file {bag_file_name}.")

def main():
    rospy.init_node('wait_and_record')

    topic_name = rospy.get_param('~topic', '/scan')
    bag_file_name = rospy.get_param('~bag_file_name', 'lidar_scan_data')

    rospy.loginfo(f"Waiting for topic {topic_name} to become available...")
    
    # Wait for the topic to become available
    rate = rospy.Rate(1) # 1 Hz
    while not rospy.is_shutdown():
        if topic_exists(topic_name):
            rospy.loginfo(f"Topic {topic_name} found!")
            break
        rate.sleep()

    # Start recording
    launch_recording_launch_file("lidar_record.launch", topic_name, bag_file_name)

if __name__ == '__main__':
    main()
