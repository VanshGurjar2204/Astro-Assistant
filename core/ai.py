import requests
from core.speaker import speak

API_KEY = "<Your NewsAPI Key>" ## api key of gemini
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

history = []  # 🧠 Session memory
last_reply = ""

def aiProcess(command):
    global last_reply, history

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }

    # 🧠 Always ask Gemini to reply shortly
    prompt = f"Reply in one short sentence: {command}"

    # Add user message to history
    history.append({
        "role": "user",
        "parts": [{"text": prompt}]
    })

    payload = {
        "contents": history[-6:]  # Use last 3 turns
    }

    try:
        response = requests.post(URL, headers=headers, json=payload)
        response.raise_for_status()

        reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        last_reply = reply

        # Add Gemini's reply to memory
        history.append({
            "role": "model",
            "parts": [{"text": reply}]
        })

        return reply

    except Exception as e:
        print(f"❌ Error: {e}")
        speak("Gemini had a problem.")
        return "An error occurred."
