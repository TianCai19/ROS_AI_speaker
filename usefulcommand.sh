source /opt/ros/melodic/setup.bash

# 
catkin_make
#cakin_make 发生了什么？
# 几张情况，如果你的工作空间是空的，那么catkin_make会创建一个build文件夹，一个devel文件夹，一个src文件夹，一个CMakeLists.txt文件，一个package.xml文件。
# 如果你的工作空间不是空的，那么catkin_make会在build文件夹中生成中间文件，会在devel文件夹中生成可执行文件，会在install文件夹中生成安装文件，会在log文件夹中生成日志文件。
# 如果你的工作空间不是空的，那么catkin_make会在src文件夹中生成源代码文件，会在CMakeLists.txt文件中生成编译时的配置信息，会在package.xml文件中生成软件包的信息。
#catkin_make是一个catkin工具，用于编译catkin工作空间中的软件包。
#catkin_make命令会在catkin工作空间的根目录下创建一个build文件夹，用于存放编译生成的中间文件。
#catkin_make命令会在catkin工作空间的根目录下创建一个devel文件夹，用于存放编译生成的可执行文件。
#catkin_make命令会在catkin工作空间的根目录下创建一个install文件夹，用于存放编译生成的安装文件。
#catkin_make命令会在catkin工作空间的根目录下创建一个log文件夹，用于存放编译生成的日志文件。
#catkin_make命令会在catkin工作空间的根目录下创建一个src文件夹，用于存放源代码文件。
#catkin_make命令会在catkin工作空间的根目录下创建一个CMakeLists.txt文件，用于存放编译时的配置信息。
#catkin_make命令会在catkin工作空间的根目录下创建一个package.xml文件，用于存放软件包的信息。


echo $ROS_PACKAGE_PATH

source devel/setup.bash

## what is a package?
# 一个ROS软件包，是指包含了ROS程序的源代码、编译配置文件、依赖关系、软件包信息的一个目录。
# ROS软件包的目录结构如下：
# The simplest possible package might have a structure which looks like this:

# my_package/
#   CMakeLists.txt
#   package.xml

# Packages in a catkin Workspace
# The recommended method of working with catkin packages is using a catkin workspace, but you can also build catkin packages standalone. A trivial workspace might look like this:

# workspace_folder/        -- WORKSPACE
#   src/                   -- SOURCE SPACE
#     CMakeLists.txt       -- 'Toplevel' CMake file, provided by catkin
#     package_1/
#       CMakeLists.txt     -- CMakeLists.txt file for package_1
#       package.xml        -- Package manifest for package_1
#     ...
#     package_n/
#       CMakeLists.txt     -- CMakeLists.txt file for package_n
#       package.xml        -- Package manifest for package_n


catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
# 运行的路径是catkin_ws/src，这里的catkin_ws是工作空间的根目录，src是源代码文件夹。
# catkin_create_pkg命令用于创建ROS软件包，其语法格式如下：
# catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
# 运行之后，会在当前目录下创建一个名为beginner_tutorials的ROS软件包，该软件包依赖于std_msgs、rospy、roscpp三个软件包。
# 文件结构如下：

    

roscd beginner_tutorial/../.. 
# 快速进入工作空间的根目录，这里是/home/dev/catkin_ws,方便进行 catkin_make等操作。


## when you want to use ROS, you have to run this command
 roscore
# # roscore 启动主节点

# In your catkin workspace
 cd ~/catkin_ws
 source ./devel/setup.bash
#  catkin specific If you are using catkin, 
# make sure you have sourced your workspace's setup.sh file after
#  calling catkin_make but before trying to use your applications:
echo $ROS_PACKAGE_PATH

rosrun beginner_tutorial talker.py
# rosrun 命令用于运行ROS程序包中的可执行文件，这里运行的是beginner_tutorials包中的talker.py可执行文件。
# 运行talker.py可执行文件后，会在终端中输出一段话，这段话是由talker.py文件中的代码生成的。
rosrun beginner_tutorial listener



nano ~/.bashrc
code ~/.bashrc
# 修改这个文件能够让你的环境变量永久生效，这里添加了一行source /home/dev/catkin_ws/devel/setup.bash，这样每次打开终端时，都会自动执行这个命令，从而使得环境变量永久生效。
# source命令的作用是在当前bash环境中读取并执行指定的文件中的命令，如果文件中定义了环境变量，它们会被导入到当前的shell会话中。

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc

rostopic echo /ai_answer
#rostopic echo 命令用于查看话题的内容，这里查看的是/ai_answer话题的内容。

rosrun rqt_graph rqt_graph
# rqt_graph 命令用于查看当前系统中的节点和话题的关系图，这里查看的是当前系统中的节点和话题的关系图。

## 配置 conda 环境
conda create -n py36 python=3.6
#py36是环境的名字，python=3.6是指定python的版本，这里指定的是python3.6版本。

pip install PyYAML==5.3.1
# 安装特定版本的PyYAML，这里安装的是5.3.1版本。


# 安装 requirements.txt 文件中的依赖包
pip install -r requirements.txt

# 激活和退出conda环境
conda activate py36
conda deactivate

## pip也是很有用
pip install -r requirements.txt

# 显示当前环境中安装的包
pip list
# 显示某个包的版本
pip show PyYAML

conda env export > environment.yml
# conda env export 命令用于导出当前环境的依赖包信息，这里导出的是当前环境的依赖包信息到environment.yml文件中。
# 这样方便我们在其他电脑上创建相同的环境，只需要运行conda env create -f environment.yml命令即可。

conda env create -f environment.yml

rqt_graph