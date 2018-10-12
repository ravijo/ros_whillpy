#!/usr/bin/env python
# -*- coding: utf-8 -*-

# controller.py: controller service node
# Author: Ravi Joshi
# Date: 2018/10/09

# import modules
import rospy
import whillpy
from ros_whillpy.srv import Connect, ConnectRequest, ConnectResponse
from ros_whillpy.srv import Power, PowerRequest, PowerResponse
from ros_whillpy.srv import Move, MoveRequest, MoveResponse


class Controller:
    def __init__(self):
        self.whill = None

        # define a name (this is going to be used as namespace for ros services)
        name = 'ros_whillpy'
        rospy.init_node('%s_service_node' % name)

        # define services
        connect_service = rospy.Service(
            '/%s/connect' % name, Connect, self.handle_connect)
        power_service = rospy.Service(
            '/%s/power' % name, Power, self.handle_power)
        move_service = rospy.Service('/%s/move' % name, Move, self.handle_move)

        rospy.loginfo('Service ros_whillpy is initialized successfully')
        rospy.spin()

    def handle_connect(self, req):
        response = ConnectResponse()
        try:
            self.whill = whillpy.connect(port=req.port)
        except Exception as e:
            response.success = -1
            message = str(e)
        else:
            response.success = 1
            message = 'Success'
        response.message = message
        return response

    def handle_power(self, req):
        response = PowerResponse()
        try:
            response.success = self.whill.set_power(req.option)
        except Exception as e:
            response.success = -1
            message = str(e)
        else:
            message = 'Success'
        response.message = message
        return response

    def handle_move(self, req):
        response = MoveResponse()
        try:
            response.success = self.whill.move(
                straight=req.straight, turn=req.turn)
        except Exception as e:
            response.success = -1
            message = str(e)
        else:
            message = 'Success'
        response.message = message
        return response

    def __del__(self):
        ''' cleanup the serial connection object
        '''
        if self.whill:
            self.whill.__del__()  # shouldn't it be automatic ?


if __name__ == '__main__':
    Controller()
