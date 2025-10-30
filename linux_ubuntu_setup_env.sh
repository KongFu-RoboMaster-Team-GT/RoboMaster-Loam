#!/bin/bash
#this is a script for linux machine setup. if you can't run it, try following command:
# chmod +x linux_ubuntu_setup_env.sh
#and then run with:
# ./linux_ubuntu_setup_env.sh
#NOTICE: this script does not install ros, since it is machine dependent.
sudo apt update
sudo apt upgrade
sudo apt install build-essential python3 python3-opencv python3-numpy libpcl-dev -y

#install ros for 20.04
sudo apt install -y python3-rosdep2
sudo rosdep init
rosdep update
rosdep install --from-paths ~/ros2_dashing/ros2-linux/share --ignore-src --rosdistro dashing -y --skip-keys "console_bridge fastcdr fastrtps libopensplice67 libopensplice69 osrf_testing_tools_cpp poco_vendor rmw_connext_cpp rosidl_typesupport_connext_c rosidl_typesupport_connext_cpp rti-connext-dds-5.3.1 tinyxml_vendor tinyxml2_vendor urdfdom urdfdom_headers"
sudo apt install -y libpython3-dev python3-pip
pip3 install -U argcomplete



pip3 install -U pyserial
sudo apt install python3-tqdm python3-pil python3-colcon-common-extensions ros-foxy-gtsam ros-rolling-rviz2 ros-galactic-rclpy ros-rolling-rclcpp -y