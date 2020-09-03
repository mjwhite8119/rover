#!/usr/bin/env python

import sys
import rospy
from rover.srv import *

def control_client(input):
    rospy.wait_for_service('control')
    try:
        test = rospy.ServiceProxy('control', Control)
        resp1 = test(input)
        return resp1.output
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "usage: %s [command]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input = int(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s"%(input)
    print "message: %s"%(control_client(input))
