cmake_minimum_required(VERSION 3.0.2)
project(canary_sensors)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS message_runtime rospy std_msgs
)
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES canary_sensors
  #CATKIN_DEPENDS rospy std_msgs
  #DEPENDS system_lib
)

catkin_install_python(PROGRAMS
  src/temp_publisher.py
  src/mdl_publisher.py
  src/rad_publisher.py
  src/IMU_publisher.py
  src/test.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})


###########
## Build ##
###########


include_directories(
include
   ${catkin_INCLUDE_DIRS}
)

