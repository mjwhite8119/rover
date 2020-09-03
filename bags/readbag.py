import rosbag
bag = rosbag.Bag('forward.bag')
for topic, msg, t in bag.read_messages(topics=['/chip8445/odom']):
	print msg
bag.close()
