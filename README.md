 🤖 Astro Assistant

**Astro** is a local, voice-activated personal assistant powered by Python and Gemini. It runs on your desktop, listens to your voice, responds using natural AI, and performs system tasks, plays music, manages notes, and more — all offline except for AI replies.

---

## ✅ Features

**🧠 AI & Memory**

* GPT-3.5 conversation via OpenAI
* Session memory (remembers recent messages)
* Repeat last reply
* Typing effect and suggestions

**🎙 Voice Control**

* Wake word: **"Astro"**
* Mic-based speech recognition
* Speaks replies with gTTS and pygame

**💻 System Control**

* Lock your screen
* CPU and RAM usage report
* Shutdown timer (e.g., "shutdown after 10 minutes")
* Run Python scripts by name

**🎵 Music & Fun**

* Play music from YouTube
* Play `.mp3` files from local `/music` folder
* Tells jokes

**📝 Notes & Tasks**

* Voice notes stored in `/notes/note.txt`
* Add to-do tasks in `tasks.json`
* Voice-based reminders with timer

**🌐 Web Integration**

* Google search ("search cyber security on Google")
* Open websites by name ("open website github.com")
* Latest Indian news headlines via News API

---

## 📁 Project Folder Structure

```
astro-assistant/
├── main.py                # Main loop & wake word
├── requirements.txt       # Dependencies
├── musicLibrary.py        # YouTube song links
├── tasks.json             # Auto-created task list
├── notes/                 # Notes folder
│   └── note.txt
├── music/                 # MP3 folder
├── core/
│   ├── ai.py              # GPT-3.5 logic
│   ├── actions.py         # Command processor
│   ├── recognizer.py      # Voice input
│   ├── speaker.py         # Voice output
│   ├── launcher.py        # App opening
│   ├── media.py           # Music, jokes
│   ├── tasks.py           # Notes/reminders
│   ├── system.py          # Lock, CPU info, shutdown
│   └── utils.py           # Greetings, suggestions
└── README.md              # This guide
```

---

## 🚀 How to Use Astro

 1. Install the Virtual Environment in that folder 

    bash:  python -m venv venv 

    For Activating Virtual Environment

        | OS                   | Command                       |
    | -------------------- | ----------------------------- |
    | Windows (CMD)        | `venv\Scripts\activate`       |
    | Windows (PowerShell) | `.\venv\Scripts\Activate.ps1` |
    | macOS/Linux          | `source venv/bin/activate`    |
    

    

2.  Install requirements:

```bash
   pip install -r requirements.txt
   ```
                    or  

    pip install pyttsx3 speechrecognition pywhatkit requests pyjokes psutil winshell pyautogui opencv-python pyperclip    googletrans==4.0.0-rc1 pygame 



2. Add your Gemini API key in `core/ai.py`:

```python
 Gemini API key in ai.py 4 line 
 Action.py 16 line  ## from newsapi.org in 

```

3. Run Astro:

```bash
python main.py
```

4. Say:

* "Astro, play music from folder"
* "Astro, add task complete assignment"
* "Astro, remind me to sleep in 10 minutes"
* "Astro, open YouTube"



## 🧠 Requirements

* Python 3.8+
* Microphone
* Internet for OpenAI/YouTube
* OS: Windows/Linux/Mac

---

**Built by Me — with 💻, 🎤 and ❤️**

---


I'm ready when you are ✅
# Astro-Assistant
