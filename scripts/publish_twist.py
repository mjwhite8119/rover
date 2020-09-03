#!/usr/bin/env python

import sys
import os
import rospy
from geometry_msgs.msg import TwistStamped

def publish_pose(twist_msg):
    pub = rospy.Publisher('twist_cmd', TwistStamped, queue_size=1)
    rospy.init_node('publish_twist', anonymous=True)
    rate = rospy.Rate(10) # 1hz
    while not rospy.is_shutdown():
	twist_msg.header.stamp = rospy.Time.now()
        rospy.loginfo(twist_msg)
        pub.publish(twist_msg)
        rate.sleep()

def usage():
    return "usage: %s <linear X> <angular Z>" % os.path.basename(sys.argv[0])

def limit():
    return "speed limit is : %s" % speedLimit 

if __name__ == '__main__':
    if len(sys.argv) == 3:
	twist_msg = TwistStamped()
        twist_msg.twist.linear.x = float(sys.argv[1])
        twist_msg.twist.angular.z = float(sys.argv[2])
    else:
        print usage()
        sys.exit(1)

    # Check speed limit for angular and linear
    speedLimit = float(1.0)
    if float(sys.argv[2]) > float(0.0):
      if float(sys.argv[2]) > speedLimit:
        print limit()
        sys.exit(1)

    elif float(sys.argv[1]) > speedLimit:
	print limit()
	sys.exit(1)

    try:
        publish_pose(twist_msg)
    except rospy.ROSInterruptException:
        pass
