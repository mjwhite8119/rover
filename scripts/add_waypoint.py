#!/usr/bin/env python

import sys
import os
import rospy
from geometry_msgs.msg import Pose

def waypoint(pose_msg):
    pub = rospy.Publisher('waypoint_cmd', Pose, queue_size=1)
    rospy.init_node('waypoint', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        rospy.loginfo(pose_msg)
        pub.publish(pose_msg)
	break
        rate.sleep()

def usage():
    return "usage: %s <X grid location> <Y grid location>" % os.path.basename(sys.argv[0])

if __name__ == '__main__':
    if len(sys.argv) == 3:
	pose_msg = Pose()
        pose_msg.position.x = float(sys.argv[1])
	pose_msg.position.y = float(sys.argv[2])
    else:
        print usage()
        sys.exit(1)

    try:
        waypoint(pose_msg)
    except rospy.ROSInterruptException:
        pass
