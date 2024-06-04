from gtts import gTTS
import pygame
import os

def text_to_speech(text, language='en'):
    # Create gTTS object
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the speech as an MP3 file
    tts.save("output.mp3")

def play_speech():
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load the saved MP3 file
    pygame.mixer.music.load("output.mp3")
    
    # Play the speech
    pygame.mixer.music.play()

    # Wait for the speech to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Remove the temporary MP3 file
    os.remove("output.mp3")

def convert_and_play(text, language='en'):
    # Convert text to speech
    text_to_speech(text, language=language)

    # Play the generated speech
    play_speech()

if __name__ == "__main__":
    # Input text you want to convert to speech
    text_to_convert = "Hello, this is a text-to-speech example."


    # Convert text to speech and play the audio
    convert_and_play(text_to_convert)
