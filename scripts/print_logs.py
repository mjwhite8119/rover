#!/usr/bin/env python

import sys
import os
import rospy
from std_msgs.msg import String

def send(msg):
    pub = rospy.Publisher('print_log_cmd', String, queue_size=1)
    rospy.init_node('print_logs', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
	break
        rate.sleep()

def usage():
    return "usage: %s " % os.path.basename(sys.argv[0])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        msg = String()
	msg.data = "100"		
    if len(sys.argv) == 2:
        msg = String()
	msg.data = sys.argv[1]
    else:
        print usage()
        sys.exit(1)

    try:
        send(msg)
    except rospy.ROSInterruptException:
        pass
