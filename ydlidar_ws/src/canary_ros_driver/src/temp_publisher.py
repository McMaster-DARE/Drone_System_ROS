#!/usr/bin/env
import rospy
from std_msgs.msg import String

def temp_publisher():
    pub = rospy.Publisher('temp_topic', String, queue_size=10)
    rospy.init_node('tmp117_publisher', anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher Node Started, now publishing messages")
    while not rospy.is_shutdown():
        msg = "Hello Emil - %s" % rospy.get_time()
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        temp_publisher()
    except rospy.ROSInterruptException:
        pass
