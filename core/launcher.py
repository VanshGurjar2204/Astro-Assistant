import shutil
import subprocess
from core.speaker import speak

def launch_app(app_names, fallback_name=None):
    for app in app_names:
        path = shutil.which(app)
        if path:
            speak(f"Launching {fallback_name or app}")
            subprocess.Popen(path)
            return
    speak(f"Couldn't find {fallback_name or 'the app'} on this system.")

