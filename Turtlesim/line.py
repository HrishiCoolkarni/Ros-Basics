#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
global final_pose
final_pose= Pose()
def callback(data):
    global final_pose
    final_pose.x= float(data.x)
def line():
    pub= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('Line', anonymous= True)
    len= float(input("Enter the length of line: "))
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    velocity= Twist()
    velocity.linear.x=1
    rate= rospy.Rate(10)
    global final_pose
    
    rospy.loginfo(len+5.544444561004639)
    
    while not rospy.is_shutdown() and len+5.544444561004639>final_pose.x+0.1:
        
        rospy.Subscriber('/turtle1/pose', Pose, callback)
        # len= len + 5.544444561004639  -final_pose.x
        pub.publish(velocity)
        rate.sleep()
    velocity.linear.x=0
    rospy.loginfo(final_pose.x)
    pub.publish(velocity) 

if __name__=='__main__':
    try:
        line()
    except rospy.ROSInterruptException:
        pass