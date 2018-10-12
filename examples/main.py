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
    connect_service_name = '/ros_whillpy/connect'
    power_service_name = '/ros_whillpy/power'
    move_service_name = '/ros_whillpy/move'

    rospy.wait_for_service(connect_service_name)
    rospy.wait_for_service(power_service_name)
    rospy.wait_for_service(move_service_name)

    try:
        connect = rospy.ServiceProxy(
            connect_service_name, Connect, persistent=False)
        response = connect('/dev/ttyUSB0')
        print 'response from connect service %d message %s' % (
            response.success, response.message)

        power = rospy.ServiceProxy(power_service_name, Power, persistent=False)
        response = power(True)
        print 'response from power service %d message %s' % (
            response.success, response.message)

        move = rospy.ServiceProxy(move_service_name, Move, persistent=False)
        response = move(20, -80)
        print 'response from move service %d message %s' % (
            response.success, response.message)
    except rospy.ServiceException as e:
        print 'Service call failed %s' % e


if __name__ == '__main__':
    main()
