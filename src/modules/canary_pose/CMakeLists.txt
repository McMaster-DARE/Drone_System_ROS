cmake_minimum_required(VERSION 3.0.2)
project(canary_pose)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES canary_pose
  CATKIN_DEPENDS geometry_msgs rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/IMU_publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

include_directories(
include
   ${catkin_INCLUDE_DIRS}
)
