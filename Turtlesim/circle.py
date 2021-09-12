#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def circle():
    rospy.init_node('Circle', anonymous=True)
    pub= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    velocity= Twist()
    r= int(input("Enter the radius: "))
    v= int(input("Enter the velocity: "))
    rate= rospy.Rate(10)
    while not rospy.is_shutdown():
        velocity.angular.z= v/r
        velocity.linear.x= v
        pub.publish(velocity)
        rate.sleep()

    velocity.angular.z=0
    velocity.linear.x=0
    pub.publish(velocity)




if __name__== '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass