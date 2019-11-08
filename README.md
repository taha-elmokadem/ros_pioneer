# ros_pioneer
Simple ROS launch files for the pionner based of the turtlebot3

copied from the turltebot3 with a few small changes see here
http://emanual.robotis.com/docs/en/platform/turtlebot3/overview/

## Launching Pioneer
navigate to http://nuc4/process.php and turn on the required nodes
![alt text](https://github.com/Scouttman/ros_pioneer/blob/master/launch_page.png "procmon")

## The old way
### Launching pioneer
open a terminal (ctr-alt-t) and ssh into the pioneer
```bash
ssh mbzirc@nuc4
```
then 
```bash
roslaunch pioneer bringup.launch
```
The pioneer should be beep
The robot should now be online (if it failed (red text) see the debugging help)
to test open a new terminal window (ctrl-shift-t)
```bash
nuc4_setROS
rostopic list
```
should see something like
```bash
    /RosAria/.
    ....
    /scan
```
if you see just
```bash
    /rosout
    /rosout_agg
```
it failed to launch

you can drive it around now with 
```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/RosAria/cmd_vel 
```

#### Debugging
Check that the green stat light is flashing slowly 
If flashing fast press the red reset button 
Check that the ttyUSB are set correctly ATM ttyUSB0 = pionner ttyUSB1 = sick    
can be launched indvidually with    
```bash
rosrun rosaria RosAria _port:=/dev/ttyUSB0 
rosrun sicktoolbox_wrapper sicklms _port:=/dev/ttyUSB1 _baud:=38400 
```
If they are not edit it in ~/catkin_ws/src/ros_pioneer/launch/bringup.launch
    
### Launching Nav
```bash
roslaunch pioneer navigation.launch
```

### Realsenese
```bash
roslaunch realsense2_camera rs_camera.launch 
```
For pointcloud
```bash
roslaunch realsense2_camera rs_camera.launch filters:=pointcloud 
```
To view use rviz or 
```bash
 rqt_image_view /camera/color/image_raw/compressed
```

## Limitations
The planner parameters are not tuned so it is slow and has difficult turning see turtlbot3_navigation/config/ to tune  
The odom messages are slow which may cause issues with the SLAM if so slow down or try SLAM without odom??  
udev rules have not been made of the serial adaptors so they may switch ttyUSB change in the pioneer bringup.launch  

## Note 
The laptop is called sc-staff@asus and is ssh able  
The nuc is mbzirc@nuc4  
check out ~/.bashrc   
roscd package to go there i.e. roscd pioneer  
have a look at the launch files in pioneer/launch/  
procmon runs the web interface
    

