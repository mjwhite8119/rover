#!/usr/bin/env python

import sys
import rospy
from rover.srv import *

def sendRequest(kp, ki, kd):
    rospy.wait_for_service('set_pid')
    try:
        service = rospy.ServiceProxy('set_pid', SetPID)
        resp1 = service(kp, ki, kd)
        return resp1.output
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "usage: %s [command]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        kp = float(sys.argv[1])
        ki = float(sys.argv[2])
        kd = float(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s %s %s"%(kp, ki, kd)
    print "response: %s"%(sendRequest(kp, ki, kd))
