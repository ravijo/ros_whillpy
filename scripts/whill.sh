#!/bin/bash
# author: ravi joshi
# date: 12 oct 2018
# this shell script initializes necessary ROS environment variables
# this script should be executed at whill ROS node in the following way
# $ cd ~/ros_ws
# $ source whill.sh

# make sure we don't have these variables set already
unset your_ip
unset your_hostname
unset baxter_hostname

# ip address of this machine (raspberrypi board)
your_ip="172.17.69.112"

# hostname of this machine (raspberrypi board)
# make sure hostname is resolvable. if not,
# assign the ip address to hostname as well
your_hostname="172.17.69.112"

# hostname of the baxter robot
baxter_hostname="011312P0016.local"

# first initialize all ROS variables
source devel/setup.bash

# next modify ROS_IP and ROS_HOSTNAME
export ROS_IP="${your_ip}"
export ROS_HOSTNAME="${your_hostname}"

# next modify ROS_MASTER_URI to point out to baxter comptuer
export ROS_MASTER_URI="http://${baxter_hostname}:11311"

# show ROS_MASTER_URI in shell prompt
export PS1="[whill] ${PS1}"
