cmake_minimum_required(VERSION 3.0.2)
project(canary_bringup)

find_package(catkin REQUIRED COMPONENTS
  roslaunch
  rospy
  std_msgs
)

catkin_python_setup()

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES canary_bringup
#  CATKIN_DEPENDS roslaunch rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
 catkin_install_python(PROGRAMS
   src/pushbutton_watch.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )


