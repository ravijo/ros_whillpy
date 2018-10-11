#!/usr/bin/env python
# -*- coding: utf-8 -*-

# controller.py: controller service node
# Author: Ravi Joshi
# Date: 2018/10/09

# import modules
import rospy
from ros_whillpy.srv import Connect, ConnectRequest, ConnectResponse
from ros_whillpy.srv import Power, PowerRequest, PowerResponse
from ros_whillpy.srv import Move, MoveRequest, MoveResponse


def main():
    # make sure that services are available
    rospy.wait_for_service('connect')
    rospy.wait_for_service('power')
    rospy.wait_for_service('move')

    try:
        connect = rospy.ServiceProxy('connect', Connect, persistent=False)
        response = connect('/dev/ttyUSB0')
        print 'response from connect service %d message %s' % (
            response.success, response.message)

        power = rospy.ServiceProxy('power', Power, persistent=False)
        response = power(True)
        print 'response from power service %d message %s' % (
            response.success, response.message)

        move = rospy.ServiceProxy('move', Move, persistent=False)
        response = move(20, -80)
        print 'response from move service %d message %s' % (
            response.success, response.message)
    except rospy.ServiceException as e:
        print 'Service call failed %s' % e


if __name__ == '__main__':
    main()
