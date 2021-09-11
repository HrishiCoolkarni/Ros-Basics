#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub= rospy.Publisher('change', String, queue_size=10)
    rospy.init_node('Talker_1', anonymous=True)
    i=1
    rate= rospy.Rate(10)
    while not rospy.is_shutdown() and i<=10:
        hello_str= "Hello world %s" %str(i)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        i=i+1
        rate.sleep()


if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass