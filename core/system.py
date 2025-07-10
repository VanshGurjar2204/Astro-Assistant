import os, ctypes, psutil, re, subprocess
from core.speaker import speak

def extract_seconds(text):
    match = re.search(r'(\\d+)', text)
    return int(match.group(1)) * 60 if match else 60

def system_command_handler(command):
    command = command.lower()

    if "open downloads" in command:
        os.startfile(os.path.join(os.environ['USERPROFILE'], 'Downloads'))
        return True

    elif "lock screen" in command:
        speak("Locking the screen")
        ctypes.windll.user32.LockWorkStation()
        return True

    elif "cpu usage" in command or "ram usage" in command:
        usage = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        speak(f"CPU is at {usage} percent and RAM is at {ram} percent.")
        return True

    elif "shutdown after" in command:
        seconds = extract_seconds(command)
        os.system(f"shutdown -s -t {seconds}")
        speak(f"System will shut down in {seconds // 60} minutes")
        return True

    elif "run" in command and (".py" in command or "script" in command):
        try:
            file = command.split("run", 1)[1].strip()
            if not file.endswith(".py"):
                file += ".py"
            subprocess.run(["python", file])
            speak(f"Running script {file}")
        except:
            speak("Couldn't run the script")
        return True

    return False
