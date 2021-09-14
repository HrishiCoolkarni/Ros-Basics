import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard  %s", data.data)

def listner():
    rospy.init_node('listner', anonymous=True)
    rospy.Subscriber('Chatter', String, callback)
    rospy.spin()

if __name__== '__main__':
    try:
        listner()
    except rospy.ROSInterruptException():
        pass