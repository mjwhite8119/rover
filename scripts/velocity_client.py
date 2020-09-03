#!/usr/bin/env python

import sys
import rospy
from rover.srv import *

def sendRequest(velocity):
    rospy.wait_for_service('set_velocity')
    try:
        service = rospy.ServiceProxy('set_velocity', SetVelocity)
        resp1 = service(velocity)
        return resp1.output
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "usage: %s [command]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        velocity = int(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %d"%(velocity)
    print "message: %s"%(sendRequest(velocity))
