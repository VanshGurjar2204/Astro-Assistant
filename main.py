# File: main.py
from core.recognizer import listen_for_command
from core.speaker import speak
from core.actions import processCommand
from core.utils import intro_greeting
import sys

WAKE_WORD = "astro"

if __name__ == "__main__":
    speak("Hi, I’m Astro — your personal AI assistant. Initializing...")
    intro_greeting()

    while True:
        try:
            command = listen_for_command()
        except Exception as e:
            print(f"Mic error: {e}")
            speak("Mic problem occurred. Trying again.")
            continue

        if command:
            command = command.lower()

            if any(x in command for x in ["shutdown", "exit", "bye"]):
                speak("Goodbye! Astro shutting down.")
                sys.exit()

            if WAKE_WORD in command:
                try:
                    print("✅ Activated")
                    speak("Astro light up")
                    print("🎧 Listening for your command...")
                    speak("What do you want me to do?")
                    command = listen_for_command()
                    if command:
                        try:
                            processCommand(command)
                        except Exception as e:
                            print(f"❌ Error during command processing: {e}")
                            speak("Sorry, I had trouble with that command but I'm still here.")
                    else:
                        speak("I didn't hear any command.")
                except Exception as e:
                    print(f"❌ Error after wake word: {e}")
                    speak("Sorry, something went wrong but I'm still here.")
