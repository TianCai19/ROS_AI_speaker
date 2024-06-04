#!/usr/bin/env python
# coding=utf-8
# Software License Agreement (BSD License)
#
# 以下是软件许可协议的内容，指明了版权信息、使用和分发条件，以及免责声明等。
# ...

## 简单的talker示例，它订阅了发布到'chatter'话题上的std_msgs/String消息。
# ...

import rospy  # 导入rospy模块，它是ROS Python API的一个部分，用于编写ROS节点。
from std_msgs.msg import String  # 从std_msgs包中导入String消息类型。

def callback(data):
    # 当接收到新的消息时会调用这个回调函数。
    # 它打印出节点的调用者ID以及接收到的消息内容。
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():
    # 这个函数初始化ROS节点，并订阅'chatter'话题。

    # 在ROS中，节点必须有唯一的名称。如果两个具有相同名称的节点被启动，
    # 先前的节点会被关闭。anonymous=True标志意味着rospy会为我们的'listener'
    # 节点选择一个唯一的名字，这样就可以同时运行多个监听器。
    rospy.init_node('listener', anonymous=True)

    # 创建一个订阅者，订阅名为'chatter'的话题，消息类型为String，
    # 并指定当有消息到达时调用callback函数。
    rospy.Subscriber('chatter', String, callback)

    # spin()函数会阻塞程序直到节点被停止。
    # 它让Python程序不会退出，直到这个节点被明确停止。
    rospy.spin()

if __name__ == '__main__':
    # 如果这个文件是作为主程序运行，那么就调用listener()函数。
    listener()