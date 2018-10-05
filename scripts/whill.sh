#!/bin/bash
# author: ravi joshi
# date: 12 oct 2018
# this shell script initializes necessary ROS environment variables
# this script should be executed at whill ROS node

# make sure we don't have the variables already set
unset baxter_hostname

# hostname of the baxter robot
baxter_hostname="011312P0016.local"

# first initialize all ROS variables
source devel/setup.bash

# next modify ROS_MASTER_URI to point out to baxter comptuer
export ROS_MASTER_URI="http://${baxter_hostname}:11311"
