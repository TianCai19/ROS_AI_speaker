#!/usr/bin/env python
import rospy
from std_msgs.msg import String
# Assuming text2audio.py provides a function named 'convert_and_play'
from text2audio import convert_and_play

def answer_callback(msg):
    rospy.loginfo("Received answer to convert to speech: " + msg.data)
    convert_and_play(msg.data)

if __name__ == '__main__':
    rospy.init_node('answer_to_speech_node')

    rospy.Subscriber('ai_answer', String, answer_callback)

    rospy.loginfo("Answer to speech node started, waiting for answers.")
    rospy.spin()
