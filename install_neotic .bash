#!/bin/bash

# Configure your Ubuntu repositories
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

# Set up your keys
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

# Update your Debian package index
sudo apt update

# Install ROS Noetic Desktop Full
# sudo apt install ros-noetic-desktop-full
sudo apt install ros-noetic-desktop


# Environment setup
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc

# Dependencies for building packages
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

# Initialize rosdep
sudo apt install python3-rosdep
sudo rosdep init
rosdep update