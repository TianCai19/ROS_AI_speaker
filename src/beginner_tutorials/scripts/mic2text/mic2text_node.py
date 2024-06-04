#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from audio2text import audio2text
from capture_mirc_audio import capture_audio

def wait_for_input():
    # Wait for the user to press 'r' followed by Enter to start recording
    print("Press 'r' and Enter to start recording, or 'q' and Enter to quit:")
    while not rospy.is_shutdown():
        user_input = input().strip().lower()  # Read user input from the terminal
        if user_input == 'r':
            return True  # User requested to start recording
        elif user_input == 'q':
            return False  # User requested to quit
        else:
            print("Invalid input. Press 'r' and Enter to start recording, or 'q' and Enter to quit:")

def capture_and_send_question():
    # Initialize a ROS node for this script
    rospy.init_node('question_sender')

    # Create a publisher that will post messages to the 'text_question' topic
    pub = rospy.Publisher('text_question', String, queue_size=10)

    # Wait for the publisher to establish a connection to subscribers
    rospy.sleep(1)

    while not rospy.is_shutdown():
        if wait_for_input():
            try:
                # Capture audio and convert it to text
                question_text = audio2text(capture_audio())
                rospy.loginfo(f"Sending question: {question_text}")

                # Publish the text as a ROS message
                pub.publish(question_text)
            except Exception as e:
                rospy.logerr(f"Failed to capture and send question: {e}")
        else:
            break  # Exit the loop if user decides to quit

if __name__ == '__main__':
    print("Starting the question sender node...")
    try:
        capture_and_send_question()
    except rospy.ROSInterruptException:
        pass
