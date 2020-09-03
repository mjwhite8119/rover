#!/usr/bin/env python

import sys
import os
import rospy
from geometry_msgs.msg import TwistStamped

def publish_twist(left_wheel_msg, right_wheel_msg):
    pub_left = rospy.Publisher('left_wheel_speed_cmd', TwistStamped, queue_size=1)
    pub_right = rospy.Publisher('right_wheel_speed_cmd', TwistStamped, queue_size=1)
    rospy.init_node('publish_twist', anonymous=True)
    rate = rospy.Rate(10) # 1hz
    while not rospy.is_shutdown():
	left_wheel_msg.header.stamp = rospy.Time.now()
	right_wheel_msg.header.stamp = rospy.Time.now()

        # rospy.loginfo(left_wheel_msg)
        # rospy.loginfo(right_wheel_msg)

        pub_left.publish(left_wheel_msg)
        pub_right.publish(right_wheel_msg)
        rate.sleep()

def usage():
    return "usage: %s <left_wheel_speed> <right_wheel_speed>" % os.path.basename(sys.argv[0])

def limit():
    return "speed limit is : %s" % speedLimit 

if __name__ == '__main__':
    if len(sys.argv) == 3:
	left_wheel_msg = TwistStamped()
	right_wheel_msg = TwistStamped()
        left_wheel_msg.twist.linear.x = float(sys.argv[1])
        right_wheel_msg.twist.linear.x = float(sys.argv[2])
        left_wheel_msg.header.frame_id = 'left'
        right_wheel_msg.header.frame_id = 'right'
    else:
        print usage()
        sys.exit(1)

    # Check speed limit 
    speedLimit = float(1.0)
    if float(sys.argv[2]) > speedLimit:
      print limit()
      sys.exit(1)

    if float(sys.argv[1]) > speedLimit:
	print limit()
	sys.exit(1)

    try:
        publish_twist(left_wheel_msg, right_wheel_msg)
    except rospy.ROSInterruptException:
        pass
