#!/usr/bin/env python

import sys
import rospy
from rover.srv import *

def bool_client(data):
    rospy.wait_for_service('setbool')
    try:
        test = rospy.ServiceProxy('setbool', std_srvs/SetBool)
        resp1 = test(data)
        return resp1.message
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "usage: %s [command]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        data = bool(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s"%(data)
    print "message: %s"%(bool_client(data))
