# canary_sensors

# Canary Sensor Package

The `canary_sensor` package is designed to provide sensor functionality for the Canary system within the Robot Operating System (ROS) environment.

## Package Overview

The package contains several Python scripts and configuration files that enable the integration of various sensors into the Canary system. Including: 

### Python Scripts

- **RadSens.py**: Python module providing sensor functionality
- **IMU_publisher.py**: Script for publishing Inertial Measurement Unit (IMU) data
- **mdl_publisher.py**: Script for publishing model data
- **rad_publisher.py**: Script for publishing radiation data
- **temp_publisher.py**: Script for publishing temperature data

### Configuration Files

- **CMakeLists.txt**: CMake configuration file for building the package.
- **setup.py**: Setup script for the package.


## Launch File

The package includes a launch file `sensors.launch`, which facilitates the launching of sensor publisher nodes. This launch file allows for easy initialization of the sensor functionality provided by the package.

### How to Use

To use this package, follow these steps:

1. Clone the `canary_sensor` package into your ROS workspace/catkin workspace
2. Ensure that all required dependencies are installed
3. Execute the `sensors.launch` launch file using the `roslaunch` command



  
