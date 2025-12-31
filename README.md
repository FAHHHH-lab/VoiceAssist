# VoiceAssist

VoiceAssist is a personal AI voice assistant built in Python. It acts as a local "Jarvis", capable of controlling your system, searching the web, and chatting via Google Gemini. It supports both **Voice** and **Text (CLI)** modes.

---

## Features

### 🤖 AI Core
-   **Conversation**: Powered by Google Gemini (`gemini-2.5-flash`).
-   **Persona**: "Vyom" - a helpful, professional Gen Alpha assistant.

### 💻 System Control
-   **Power**: Shutdown, Restart, Sleep (with safety confirmation).
-   **Hardware Stats**: Check Battery level, CPU usage, and Memory usage.
-   **Adjustments**: Control System Volume and Screen Brightness.
-   **Apps**: Launch applications (e.g., "Open Calculator").

### 🌐 Connectivity
-   **Web Search**: Real-time privacy-focused search using DuckDuckGo (`ddgs`).
-   **Web Shortcuts**: Voice commands to open popular sites (YouTube, GitHub, Reddit, etc.).

### 🎙️ Modes
-   **Voice Mode**: Hands-free interactions with `SpeechRecognition` and `pyttsx3` TTS.
    -   Wake Word: `"jarvis"`
-   **Text Mode (CLI)**: Fast, silent keyboard interaction.

---

## Installation

```bash
# Clone the repository
gh repo clone lilcloudcoder/VoiceAssist
cd VoiceAssist

# Install dependencies (requires psutil, screen_brightness_control, ddgs, etc.)
python3.11 -m venv env # I HIGHLY RECOMMEND PYTHON3.11
source env/bin/activate
pip install -r libs.txt
```


### Dependencies
-   `google.genai`, `SpeechRecognition`, `pyttsx3`, `rich`, `pyaudio`
-   `psutil` (System Monitoring)
-   `screen_brightness_control` (Display)
-   `ddgs` (Web Search)

---

## Usage
Generate a API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

Run the script:
```bash
export GEMINI_API_KEY="<YOUR_API_KEY_HERE>"
python main.py
```

You will be prompted to select a mode:
-   **T**: Text Mode (CLI). Type commands silently.
-   **V**: Voice Mode. Speak to Jarvis.

### Example Commands
-   **Search**: *"Search for the latest space news"*
-   **System**: *"What is my battery level?"*, *"Set brightness to 80%"*
-   **Power**: *"Restart the system"* (Agent will ask for confirmation: *"Yes, do it"*)
-   **Apps**: *"Open Spotify"*
-   **Chat**: *"Tell me a joke"*

### Notes
-   **Microphone**: Requires `pyaudio`. If installation fails, install `portaudio` via your package manager (e.g., `brew install portaudio`).
-   **Permissions**: MacOS may prompt for **"System Events"** control permissions on the first run of system commands (like volume/sleep). Allow these for full functionality.


### Features that are only supported for macOS and linux : SetVolume
### Highly recommend ≤ python@v3.11 / ≥ python@3.9.*
---
Built with ❤️ by LilCloudCoder.
