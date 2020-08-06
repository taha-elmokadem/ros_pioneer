#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/RosAria/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    speed = input("Input your speed:")
    distance = input("Type your distance:")
    anglespeed = input("Input your angular speed (degrees/sec):")
    isForward = input("GO?:" )#True or False
    relative_angular = 0.625*PI
    angular_speed = anglespeed*2*PI/360
    #Checking if the movement is forward or backwards
    if (isForward):
        vel_msg.linear.x = abs(speed)
    #else:
        #vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    i=1

    while i<5:

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        current_angular = 0
        vel_msg.linear.x = abs(speed)
        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        time.sleep(3)
        t0 = rospy.Time.now().to_sec()
        vel_msg.angular.z = abs(angular_speed)
        while(current_angular<relative_angular):
            
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angular = angular_speed*(t1-t0)
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        time.sleep(3)
        i+=1
    rospy.spin()
        


if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
