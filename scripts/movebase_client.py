#!/usr/bin/env python
# Script to move the robot base

import sys
import rospy
from rover.srv import *

def test_client(input):
    rospy.wait_for_service('move_base')
    try:
        test = rospy.ServiceProxy('move_base', Test)
        resp1 = test(input)
        return resp1.output
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "usage: %s [command]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input = str(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s"%(input)
    print "message: %s"%(test_client(input))
