#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import String

def random_color():
    led = random.randint(0, 9)
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    return ("Led: "+str(led)+" color(RGB):"+str(r)+" , "+str(g)+" , "+str(b))



def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    #rospy.logwarn('orange - warning')
    #rospy.logout('white - info')
    #rospy.logerr('Red - error')
    #rospy.logfatal('Red- fatal')
    rospy.logwarn('Starting talker...')
    #rospy.loginfo('Talking')    

    count = 0

    while not rospy.is_shutdown():
        
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)    #publish to terminal
        
        hello_str = random_color()

        pub.publish(hello_str)      #publish to topic
        rate.sleep()                #sleeps at defined rate



        # show node is active ## needs to have clearing lines
        count += 1 
        if count == 10:
            print('Talking [\\] ') 
        if count == 20:
            print('Talking [|] ') 
        if count == 30:
            print('Talking [/] ') 
        if count == 40:
            print('Talking [-] ') 
            count = 0


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
