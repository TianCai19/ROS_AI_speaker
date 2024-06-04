rostopic pub -r 1 text_question std_msgs/String "What is the meaning of study?"
# rostopic pub 命令用于发布话题，这里发布的是text_question话题，话题的类型是std_msgs/String，话题的内容是What is the meaning of life?。
# -r 1 表示发布一次，如果不加-r 1，那么会一直发布话题，直到按下Ctrl+C。

rostopic pub  text_question std_msgs/String "What is the meaning of insist?"
 