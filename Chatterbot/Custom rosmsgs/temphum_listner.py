#!/usr/bin/env python3

import rospy
from Chatterbot.msg import temphum

def callback(data):
    rospy.loginfo("I heard : ")
    rospy.loginfo("%s"%data.id)
    rospy.loginfo("%s"%data.patient)
    rospy.loginfo("%f"%data.temperature)
    rospy.loginfo("%f"%data.humidity)


def temphum_listner():
    rospy.init_node('Temphum_Listner', anonymous=True)
    rospy.Subscriber('Temphum_topic',temphum, callback)
    rospy.spin()

if __name__== '__main__':
    try:
        temphum_listner()
    except rospy.ROSInterruptException:
        pass
