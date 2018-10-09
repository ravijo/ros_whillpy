cmake_minimum_required(VERSION 2.8.3)
project(ros_whillpy)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
)

## System dependencies are found with CMake's conventions
#find_package(Pyserial)

## Generate services in the 'srv' folder
add_service_files(
   FILES
   power.srv
   move.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
)
