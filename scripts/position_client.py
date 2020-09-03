#!/usr/bin/env python

import sys
import rospy
from rover.srv import *

def sendRequest(linear_x, linear_y, angular_z):
    rospy.wait_for_service('set_position')
    try:
        service = rospy.ServiceProxy('set_position', SetPosition)
        resp1 = service(linear_x, linear_y, angular_z)
        return resp1.output
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "usage: %s [command]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        linear_x = float(sys.argv[1])
        linear_y = float(sys.argv[2])
        angular_z = float(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s %s %s"%(linear_x, linear_y, angular_z)
    print "response: %s"%(sendRequest(linear_x, linear_y, angular_z))
