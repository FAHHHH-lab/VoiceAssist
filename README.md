# VoiceAssist

VoiceAssist is a personal AI voice assistant built in Python. It listens to your commands via microphone, responds using Google Gemini AI, and can open websites, provide information, or assist with general queries. It’s your mini “Jarvis” that runs right from your computer!

---

## Features

-  **Voice Command Recognition** – Uses `SpeechRecognition` to capture your commands.  
-  **Text-to-Speech** – Speaks back responses using `pyttsx3`.  
-  **Web Integration** – Open popular websites instantly with simple voice commands.  
-  **AI-Powered Responses** – Uses Google Gemini AI for intelligent, context-aware replies.  
-  **Rich Console Output** – Beautiful Markdown rendering with the `rich` library.  
-  **Wake Word Detection** – Only responds when you say `"jarvis"` to avoid accidental activation.

---

## Installation

```bash
gh repo clone lilcloudcoder/VoiceAssist
cd VoiceAssist
pip install -r libs.txt 
export GEMINI_API_KEY="<YOUR_API_KEY_HERE>"
python main.py
```
### NOTE:
- Replace <YOUR_API_KEY_HERE> to **Your Real Gemini API key**
- Generate one at: https://aistudio.google.com/api-keys

---
Thanks For Visiting!
