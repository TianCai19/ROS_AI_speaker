#!/bin/bash

# Start roscore
gnome-terminal -- bash -c "roscore"

# Wait for roscore to start
sleep 5

# Open three different terminal windows
gnome-terminal -- bash -c "echo 'Window 1'; exec bash"
gnome-terminal -- bash -c "python src/beginner_tutorials/scripts/mic2text/mic2text_node.py"
gnome-terminal -- bash -c "python src/beginner_tutorials/scripts/bard/bard_interaction.py"
gnome-terminal -- bash -c "python src/beginner_tutorials/scripts/text2audio/text2audio_node.py"
