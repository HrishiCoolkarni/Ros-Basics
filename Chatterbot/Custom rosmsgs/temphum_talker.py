#!/usr/bin/env python3
import random
import rospy
from Chatterbot.msg import temphum

def temphum_talker():
    pub= rospy.Publisher('Temphum_topic', temphum, queue_size=10)
    rospy.init_node('Temphum_talker', anonymous=True)
    rate= rospy.Rate(10)
    i=1
    while not rospy.is_shutdown():
        temp_hum= temphum()
        temp_hum.id= str(i)
        temp_hum.patient= "Covid patient %s"%str(i)
        temp_hum.temperature= 20+ random.random()*2
        temp_hum.humidity= 32.5 + random.random()*2
        rospy.loginfo(temp_hum)
        pub.publish(temp_hum)
        i=i+1
        rate.sleep()

if __name__=='__main__':
    try:
        temphum_talker()
    except rospy.ROSInterruptException:
        pass