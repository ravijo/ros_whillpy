#!/usr/bin/env python
# -*- coding: utf-8 -*-

# move_forward.py: move whill forward
# Author: Ravi Joshi
# Date: 2019/07/04

# import modules
import rospy
from ros_whillpy.srv import Connect, ConnectRequest, ConnectResponse
from ros_whillpy.srv import Power, PowerRequest, PowerResponse
from ros_whillpy.srv import Move, MoveRequest, MoveResponse


def main():
    # move straight forward for defined steps
    steps = 10

    # make sure that services are available
    connect_service_name = '/ros_whillpy/connect'
    power_service_name = '/ros_whillpy/power'
    move_service_name = '/ros_whillpy/move'

    rospy.wait_for_service(connect_service_name)
    rospy.wait_for_service(power_service_name)
    rospy.wait_for_service(move_service_name)

    try:
        connect = rospy.ServiceProxy(
            connect_service_name, Connect, persistent=True)
        response = connect('/dev/ttyUSB0')
        print 'response from %s service %d message %s' % (connect_service_name,
                                                          response.success,
                                                          response.message)

        power = rospy.ServiceProxy(power_service_name, Power, persistent=True)
        response = power(True)
        print 'response from %s service %d message %s' % (power_service_name,
                                                          response.success,
                                                          response.message)

        move = rospy.ServiceProxy(move_service_name, Move, persistent=True)
        
        # move straight for defined steps
        for _ in range(steps):
            response = move(10, 0)
            print 'response from %s service %d message %s' % (move_service_name,
                                                              response.success,
                                                              response.message)
            rospy.sleep(0.2)
    except rospy.ServiceException as e:
        print 'Service call failed %s' % e


if __name__ == '__main__':
    main()
