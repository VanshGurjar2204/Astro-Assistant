# File: core/extras.py

import os
import webbrowser
import threading
import datetime
import random
import pyautogui
import pygame
import pywhatkit
import requests

from core.speaker import speak
from core.ai import aiProcess
import musicLibrary

# 🔑 Add your OpenWeatherMap API key here
WEATHER_API_KEY = "<Your_OpenWeather_API_Key>"

# ✅ YouTube command handler (merged & cleaned)
def play_youtube(command):
    command = command.lower()

    if "play" in command and "on youtube" in command:
        topic = command.split("play", 1)[1].split("on youtube")[0].strip()
        if topic:
            speak(f"Playing {topic} on YouTube")
            pywhatkit.playonyt(topic)
            return True

    elif "open" in command and "on youtube" in command:
        topic = command.split("open", 1)[1].split("on youtube")[0].strip()
        if topic:
            speak(f"Searching {topic} on YouTube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={topic}")
            return True

    elif "play" in command:
        for song in musicLibrary.music:
            if song in command:
                webbrowser.open(musicLibrary.music[song])
                speak(f"Playing {song} on YouTube")
                return True

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return True

    return False


# ✅ Weather Report
def weather_report(command):
    if "weather" in command:
        city = command.split("in")[-1].strip() if "in" in command else "your city"
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
            data = requests.get(url).json()
            if data["cod"] == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                speak(f"It’s {temp}°C with {desc} in {city}")
            else:
                speak("I couldn't find that city.")
        except:
            speak("Sorry, I couldn’t get the weather right now.")
        return True
    return False

# ✅ Folder shortcuts
FOLDER_MAP = {
    "downloads": os.path.join(os.environ['USERPROFILE'], "Downloads"),
    "desktop": os.path.join(os.environ['USERPROFILE'], "Desktop"),
    "documents": os.path.join(os.environ['USERPROFILE'], "Documents"),
    "pictures": os.path.join(os.environ['USERPROFILE'], "Pictures"),
    "projects": os.path.join(os.getcwd(), "projects")
}

def open_folder(command):
    for name, path in FOLDER_MAP.items():
        if f"open {name} folder" in command:
            if os.path.exists(path):
                os.startfile(path)
                speak(f"Opening your {name} folder")
            else:
                speak(f"I can't find the {name} folder")
            return True
    return False

# ✅ Reminder with delay
def set_reminder(command):
    if "remind me to" in command and "in" in command:
        try:
            msg = command.split("remind me to")[1].split("in")[0].strip()
            time_part = command.split("in")[1].strip()
            words = time_part.split()
            delay = 0

            for i, word in enumerate(words):
                if word.isdigit():
                    num = int(word)
                    if i + 1 < len(words):
                        unit = words[i + 1].lower()
                        if "second" in unit:
                            delay = num
                        elif "minute" in unit or "min" in unit:
                            delay = num * 60
                        elif "hour" in unit:
                            delay = num * 3600
                    break

            if delay > 0:
                def reminder():
                    speak(f"⏰ Reminder: {msg}")
                threading.Timer(delay, reminder).start()
                speak(f"Okay, I’ll remind you to {msg} in {words[0]} {words[1]}")
            else:
                speak("Sorry, I didn’t catch how long to wait.")
        except Exception as e:
            print(f"❌ Reminder error: {e}")
            speak("Please say something like 'remind me to drink water in 5 minutes'")
        return True
    return False

# ✅ Screenshot
def take_screenshot(command):
    if "screenshot" in command:
        screenshot_dir = os.path.join(os.environ['USERPROFILE'], "Pictures", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        filename = os.path.join(
            screenshot_dir,
            f"shot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )
        pyautogui.screenshot().save(filename)
        speak("Screenshot taken and saved to your Pictures folder.")
        return True
    return False

# ✅ Play Spotify
def play_spotify(command):
    if "play spotify" in command:
        try:
            os.startfile("spotify")  # Windows only
            speak("Opening Spotify")
        except:
            speak("Spotify is not installed or not found.")
        return True
    return False

# ✅ Music from folder
def play_local_music(command):
    if "play music from folder" in command:
        try:
            music_folder = os.path.join(os.getcwd(), "music")
            songs = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
            if songs:
                pygame.mixer.init()
                song_path = os.path.join(music_folder, random.choice(songs))
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()
                speak("Playing music from your folder")
            else:
                speak("No mp3 files found in the music folder")
        except:
            speak("Error accessing music folder")
        return True
    return False

# ✅ Master handler
def extra_feature_handler(command):
    return (
        play_youtube(command)
        or weather_report(command)
        or open_folder(command)
        or set_reminder(command)
        or take_screenshot(command)
        or play_spotify(command)
        or play_local_music(command)
    )
