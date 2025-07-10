# File: core/actions.py

import os, subprocess, webbrowser, random, requests
from core.speaker import speak
from core.ai import aiProcess, last_reply
from core.utils import typing_effect, interjection
from core.launcher import launch_app
from core.recognizer import listen_for_command
from core.system import system_command_handler
from core.tasks import task_command_handler
from core.extras import extra_feature_handler  # ✅ Import extra features
import musicLibrary

def get_news():
    try:
        api_key = "<Your NewsAPI Key>"  # ✅ Api key of News   ## from newsapi.org in 
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
        r = requests.get(url)
        r.raise_for_status()  # 🔒 Raise error if request fails

        articles = r.json().get("articles", [])
        if not articles:
            speak("No news found at the moment.")
            return

        for article in articles[:3]:
            speak(article['title'])

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error: {http_err}")
        speak("The news service is currently unavailable.")

    except Exception as e:
        print(f"❌ News fetch error: {e}")
        speak("Sorry, I couldn’t fetch the news right now.")


def processCommand(c):
    try:
        c = c.lower().strip()
        print("🧠 Interpreting:", c)

        # Prevent duplicate command execution
        if hasattr(processCommand, "last") and c == processCommand.last:
            speak("You've already asked that. Try something new.")
            return
        processCommand.last = c

        if "repeat" in c:
            if last_reply:
                speak(last_reply)
            else:
                speak("Sorry, there's nothing to repeat yet.")
            return

        if task_command_handler(c): return
        if system_command_handler(c): return
        if extra_feature_handler(c): return  # ✅ Unified handler for media, YouTube, jokes, etc.

        if "open vs code" in c or "open visual studio code" in c:
            launch_app(["code"], "Visual Studio Code")
            return

        if "open brave" in c:
            launch_app(["brave", "brave-browser"], "Brave Browser")
            return

        if "open chrome" in c:
            launch_app(["chrome", "google-chrome"], "Google Chrome")
            return

        if "open chatgpt" in c:
            webbrowser.open("https://chat.openai.com")
            speak("Opening ChatGPT")
            return

        if "open website" in c:
            try:
                site = c.split("open website", 1)[1].strip()
                url = site if site.startswith("http") else f"https://{site}"
                speak(f"Opening {site}")
                webbrowser.open(url)
            except Exception as e:
                print(f"❌ Website open error: {e}")
                speak("Sorry, I couldn't understand the website name.")
            return

        if "search" in c and "on google" in c:
            query = c.replace("search", "").replace("on google", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query} on Google")
            return

        if "news" in c or "headlines" in c:
            get_news()
            return

        # Fallback to ChatGPT
        interjection()
        output = aiProcess(c)
        typing_effect(output)
        speak(output)

    except Exception as e:
        print(f"❌ Error in processCommand: {e}")
        speak("Sorry, something went wrong but I'm still here.")
