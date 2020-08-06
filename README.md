# ros_pioneer
Simple ROS launch files for the pionner based of the turtlebot3

copied from the turltebot3 with a few small changes see here
http://emanual.robotis.com/docs/en/platform/turtlebot3/overview/

### Launching pioneer
open a terminal (ctr-alt-t) and ssh into the pioneer
```bash
ssh sc-staff@HOSTNAME
```
where HOSTNAME is your robot's name (written on the robot). If some problems are found where the hostname cannot be resolved, use the robot's ip to connect.
Then, run
```bash
roslaunch pioneer bringup.launch
```
The pioneer should be beep.
The robot should now be online (if it failed (red text) see the debugging help)
to test open a new terminal window (on your local computer connected to the same network), and run
```bash
export ROS_MASTER_URI=http://HOSTNAME:11311
rostopic list
```
by replacing HOSTNAME with your robot name.
To verify that the robot is working properly, you should see something like
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
Check that the ttyUSB are set correctly ATM ttyUSB0 = ttyPionner, ttyUSB1 = ttySick    
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
    

