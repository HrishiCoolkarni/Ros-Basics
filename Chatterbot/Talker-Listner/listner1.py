#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
global i
i= True
def callback(data):
    rospy.loginfo("I heard %s",data.data)
    if(data.data=="Hello world 10"):
        global i
        i=False

def listner():
    rospy.Subscriber('change', String, callback)
    rospy.init_node('Listner', anonymous=True)
    rate= rospy.Rate(10)
    while not rospy.is_shutdown() and i:

        rate.sleep()

if __name__=='__main__':
    try:
        listner()
    except rospy.ROSInterruptException():
        pass