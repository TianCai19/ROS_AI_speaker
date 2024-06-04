
# AI Speaker Project

## Overview
This project is a ROS (Robot Operating System) based AI Speaker system designed to perform interactive voice-based Q&A using ROS Noetic on Ubuntu 22.04 with Python 3.9. It captures voice input, converts it to text, processes the text to generate responses, and then converts these responses back into speech.

## Prerequisites
- Ubuntu 22.04
- ROS Noetic
- Conda (for managing Python environments)
- Python 3.9

## Environment Setup
1. **Install ROS Noetic**: Follow the official ROS Noetic installation guide for Ubuntu.
2. **Configure Python Environment with Conda**:
   - Install Conda if not already installed.
   - Create a new Conda environment with Python 3.9: `conda create --name myenv python=3.9`
   - Activate the Conda environment: `conda activate myenv`
3. **Install Project Dependencies**:
   - Navigate to the project directory.
   - Run `bash install_neotic.bash` to install necessary ROS packages and dependencies.
   - Install Python dependencies: `pip install -r src/beginner_tutorials/scripts/requirements.txt`

## System Architecture
Below is a node graph that illustrates the flow of information between the components:

![ROS Node Graph](rosgraph.png)

- `/question_sender`: Captures and sends voice as text questions.
- `/bard_interaction`: Receives questions and sends back generated answers.
- `/answer_to_speech_node`: Converts received text answers to speech.

To view this graph on your system, run `rosrun rqt_graph rqt_graph` after starting all nodes.

## Components

### Bard Interaction Node
This node subscribes to the `/text_question` topic to receive questions and uses the Bard AI to generate answers, which are published on the `/ai_answer` topic.

### Microphone to Text Node (`mic2text`)
Captures audio from the microphone, converts it to text using Google Cloud Speech API, and publishes the text to the `/text_question` topic.

### Text to Speech Node (`text2audio`)
Converts text messages received on the `/ai_answer` topic into speech using the gTTS library and plays the audio using Pygame.

## Running the Project
1. Start the ROS core: `roscore`
2. In separate terminals, run each node:
   - `rosrun beginner_tutorials question_sender.py`
   - `rosrun beginner_tutorials bard_interaction.py`
   - `rosrun beginner_tutorials answer_to_speech_node.py`

## Project Structure
```
AI_speaker/
│
├── build/
├── devel/
├── src/
│   ├── beginner_tutorials/
│   │   ├── CMakeLists.txt
│   │   ├── environment.yml
│   │   ├── package.xml
│   │   ├── scripts/
│   │   │   ├── bard/
│   │   │   ├── mic2text/
│   │   │   └── text2audio/
│   │   └── ...
│   ├── CMakeLists.txt (link to the 'beginner_tutorials' CMakeLists.txt)
│   └── ...
├── install_neotic.bash
├── RunAllnodes.bash
└── usefulcommand.sh
```
## Interacting with the System
- Recording a Question: After starting the question_sender node, press 'r' and Enter to start recording your voice.
- Receiving an Answer: The system will process your question and provide an audible answer through the speakers.

## Additional Information
- Contributions to the AI Speaker project are welcome. Please refer to the contributing guidelines for more information.
- Ensure that the Google API key for the Speech service is properly set up in a `.env` file for the `mic2text` component.
- For the `text2audio` component, gTTS and Pygame must be correctly installed within the Conda environment.


