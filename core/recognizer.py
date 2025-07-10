import speech_recognition as sr

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening for command...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=15)
            return r.recognize_google(audio)
        except:
            return None
