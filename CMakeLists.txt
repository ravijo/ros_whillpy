cmake_minimum_required(VERSION 2.8.3)
project(ros_whillpy)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
  message_generation
)

## Generate services in the 'srv' folder
add_service_files(
   FILES
   Connect.srv
   Power.srv
   Move.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
)
