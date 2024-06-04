#!/usr/bin/env python
# coding=utf-8


## 简单的讲述者（talker）示例，发布 std_msgs/String 消息到 'chatter' 话题。

import rospy  # 导入 rospy 模块，它是 ROS Python API 的一部分，用于编写 ROS 节点。
from std_msgs.msg import String  # 从 std_msgs 包中导入 String 消息类型。

def talker():
    # 定义一个发布者（publisher），发布 'chatter' 话题，消息类型为 String，
    # 队列大小（queue_size）为 10。
    pub = rospy.Publisher('chatter', String, queue_size=10)
    
    # 初始化一个名为 'talker' 的节点，anonymous=True 表示自动生成一个唯一的节点名，
    # 以避免节点名称冲突。
    rospy.init_node('talker', anonymous=True)
    
    # 设置循环频率（rate）为 10hz。
    rate = rospy.Rate(10)
    
    # 当节点没有被关闭（shutdown）时，循环执行以下操作。
    while not rospy.is_shutdown():
        # 根据当前时间生成一个字符串（string）。
        hello_str = "hello world %s" % rospy.get_time()
        
        # 将该字符串作为日志信息（loginfo）打印出来。
        rospy.loginfo(hello_str)
        
        # 发布（publish）消息到 'chatter' 话题。
        pub.publish(hello_str)
        
        # 根据设置的频率（rate）休眠（sleep），以达到循环的频率。
        rate.sleep()

if __name__ == '__main__':
    try:
        # 尝试执行 talker 函数。
        talker()
    except rospy.ROSInterruptException:
        # 如果有 ROS 中断异常（ROSInterruptException），则不做任何操作。
        pass