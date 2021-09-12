#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def spiral():
    rospy.init_node('spiral', anonymous=True)
    pub= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    velocity= Twist()
    r= float(input("Enter the initial radius: "))
    v= float(input("Enter the velocity: "))
    rate= rospy.Rate(10)

    while not rospy.is_shutdown():
        velocity.linear.x= v
        velocity.angular.z= v/r
        pub.publish(velocity)
        r= r+0.005
        rate.sleep()
    velocity.angular.z=0
    velocity.linear.x=0
    pub.publish(velocity)


if __name__=='__main__':
    try:
        spiral()
    except rospy.ROSInterruptException:
        pass