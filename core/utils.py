import datetime, psutil, time
from core.speaker import speak
import random

def intro_greeting():
    hour = datetime.datetime.now().hour
    now = datetime.datetime.now().strftime("%I:%M %p")
    battery = psutil.sensors_battery()
    level = battery.percent if battery else "Unknown"

    if hour < 12:
        greet = "Good morning"
    elif hour < 18:
        greet = "Good afternoon"
    else:
        greet = "Good evening"

    speak(f"{greet}, it's {now}. Your battery is at {level} percent.")

def typing_effect(text):
    print("🤖 Astro:", end=" ", flush=True)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()


def interjection():
    speak(random.choice([
        "Working on it...", "Give me a second...", "Let me check that..."
    ]))
