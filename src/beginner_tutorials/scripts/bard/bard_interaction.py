#!/usr/bin/env python
import rospy
from std_msgs.msg import String

from bard import bard_ai_response

# def bard_ai_response(question):
#     # 这里是模拟的 Bard AI 响应。
#     # 您需要替换成实际调用 Bard AI 的代码。
#     # 假设返回的回答是问题的简单重复。
#     return "Bard AI says: " + question

def question_callback(msg):
    rospy.loginfo("Received a question: " + msg.data)
    answer = bard_ai_response(msg.data)
    rospy.loginfo("Answering: " + answer)  # 新增的日志记录
    pub.publish(answer)

if __name__ == '__main__':
    rospy.init_node('bard_interaction')

    # 创建一个订阅者，订阅来自 audio_to_text 节点的文本消息
    rospy.Subscriber('text_question', String, question_callback)

    # 创建一个发布者，发布 Bard AI 的回答
    pub = rospy.Publisher('ai_answer', String, queue_size=10)
    # queue_size=10 表示最多缓存 10 条消息，超过 10 条消息，最早的消息会被丢弃

    rospy.loginfo("Bard interaction node started, waiting for questions.")
    rospy.spin()
    #spin() 会一直阻塞，直到节点被关闭

#  rostopic echo ai_answer
#  rostopic pub text_question std_msgs/String "What is the meaning of life?"