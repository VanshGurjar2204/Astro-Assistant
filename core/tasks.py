import os, json, threading
from core.speaker import speak
from core.recognizer import listen_for_command

NOTES_DIR = "notes"
TASKS_FILE = "tasks.json"
os.makedirs(NOTES_DIR, exist_ok=True)
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "w") as f:
        json.dump([], f)

def task_command_handler(command):
    command = command.lower()

    if "take a note" in command:
        speak("What should I write?")
        note = listen_for_command()
        with open(os.path.join(NOTES_DIR, "note.txt"), "a") as f:
            f.write(note + "\n")
        speak("Note saved")
        return True

    elif "add task" in command:
        task = command.split("add task", 1)[1].strip()
        with open(TASKS_FILE, "r+") as f:
            tasks = json.load(f)
            tasks.append({"task": task, "done": False})
            f.seek(0)
            json.dump(tasks, f, indent=2)
        speak("Task added")
        return True

    elif "remind me" in command:
        try:
            parts = command.split("in")
            msg = parts[0].replace("remind me to", "").strip()
            minutes = int(parts[1].strip().split()[0])
            threading.Timer(minutes * 60, lambda: speak(f"Reminder: {msg}")).start()
            speak(f"Okay, I will remind you to {msg} in {minutes} minutes")
        except:
            speak("Please say something like 'remind me to drink water in 10 minutes'")
        return True

    return False
