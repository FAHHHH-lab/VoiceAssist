# VoiceAssist

VoiceAssist is a personal AI voice assistant built in Python. It listens via your microphone, responds using Google Gemini, and can open websites, answer quick queries (time/date/search), and chat — like a mini “Jarvis” running locally.

---

## Features

-  **Wake Word Detection** – Only responds when you say `"jarvis"` (case‑insensitive).
-  **Voice Command Recognition** – Powered by `SpeechRecognition` with ambient‑noise calibration.
-  **Text‑to‑Speech** – Speaks responses with `pyttsx3` (trimmed to avoid very long blocking reads).
-  **Web Shortcuts** – Say `open <site>` for many popular sites (Google, YouTube, GitHub, Reddit, etc.).
-  **Quick Utilities** – `search for <query>`, "what's the time", "what's the date".
-  **AI‑Powered Replies** – Uses Google Gemini with a concise, voice‑friendly persona.
-  **Robustness** – Graceful handling of missing API key, network hiccups (with retries/backoff),
   and clearer console output using `rich`.

---

## Installation

```bash
gh repo clone lilcloudcoder/VoiceAssist
cd VoiceAssist
pip install -r libs.txt
export GEMINI_API_KEY="<YOUR_API_KEY_HERE>"
python main.py
```

### Notes
- Replace `<YOUR_API_KEY_HERE>` with your real Gemini API key. Generate one at: https://aistudio.google.com/api-keys
- Microphone access requires `pyaudio` (already in `libs.txt`). If install fails on your OS, consult your package manager for portaudio.

---

## Usage
- Say: `jarvis open youtube`
- Say: `jarvis search for best python tutorials`
- Say: `jarvis what's the time` or `jarvis what's the date`
- Say: `jarvis` …then your question for AI.
- Exit: say `exit/quit/shutdown` (with or without wake word), or press Ctrl+C.

### Config (in `main.py`)
- `WAKE_WORD` – default: `"jarvis"`
- `MODEL_NAME` – default: `"gemini-2.5-flash"`
- `PHRASE_TIME_LIMIT`, `LISTEN_TIMEOUT` – tune listening behavior.

---
Thanks for visiting!
