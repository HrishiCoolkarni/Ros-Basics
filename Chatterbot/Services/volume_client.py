#!/usr/bin/env python3

import sys
import rospy
from Chatterbot.srv import Volume

def volume_client(x,y,z):
    rospy.wait_for_service('volume')
    try:
        find_volume= rospy.ServiceProxy('volume', Volume)
        result= find_volume(x,y,z)
        return result.volume
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)



def usage():
    return "%s [x y z]"%sys.argv[0]
if __name__== '__main__':
    if len(sys.argv)==4:
        x= int(sys.argv[1])
        y= int(sys.argv[2])
        z= int(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s*%s*%s"%(x,y,z))
    print("%s*%s*%s= %s"%(x,y,z,volume_client(x,y,z)))