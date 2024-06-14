#!/usr/bin/env python3

import RPi.GPIO as gpio
import roslaunch # added
import rospy # added
import subprocess
import time                                                                  

gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.IN, pull_up_down = gpio.PUD_UP)

# From here 
rospy.init_node('en_Mapping', anonymous=True)
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)

find_command = ["rospack", "find", "canary_bringup"]
package_path = subprocess.check_output(find_command).strip().decode('utf-8')
launch_file = package_path + "/launch/bringup.launch"

launch_process = None
# to here

def handle_button_press(channel):
    # From here 
    global launch_process
    
    if launch_process is None:
    	launch_process = roslaunch.parent.ROSLaunchParent(uuid, [launch_file])
    	launch_process.start()
    	rospy.loginfo("launch file started")
    	
    else:
    
    	launch_process.shutdown()
    	launch_process = None
    	rospy.loginfo("Launch file stoppped")
    
    #subprocess.call(["python", "$(find canary_bringup)/launch/bringup.launch"])
# to here

gpio.add_event_detect(5, gpio.FALLING, callback = handle_button_press, bouncetime=300)
# From here 
try:
    while not rospy.is_shutdown():
        time.sleep(1)
except KeyboardInterrupt:
    gpio.cleanup()
    if launch_process is not None:
    	launch_process.shutdown()
#to here
#while True:
 #   time.sleep(360) 
