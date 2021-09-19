#!/usr/bin/env python3

from Chatterbot.srv import Volume, VolumeResponse
import rospy

def handle_volume(req):
    print("Returning [%s * %s * %s = %s]"%(req.a, req.b, req.c,(req.a*req.b*req.c)))
    return VolumeResponse(req.a*req.b*req.c)


def volume_server():
    rospy.init_node('Volume_server')
    s= rospy.Service('volume',Volume, handle_volume)
    rospy.loginfo("Ready to find volume.")
    rospy.spin()

if __name__=='__main__':
    volume_server()
