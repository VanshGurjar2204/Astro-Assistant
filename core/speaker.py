# File: core/speaker.py
from gtts import gTTS
import pygame
import os
import time

def speak(text):
    try:
        # Convert text to speech and save as mp3
        tts = gTTS(text=text, lang='en')
        tts.save("temp.mp3")

        # Initialize and play using pygame
        pygame.mixer.init()
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()

        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.quit()  # proper cleanup
        os.remove("temp.mp3")

    except Exception as e:
        print(f"❌ Speech error: {e}")
