# FAHHST-Assistant 

FAHHST-Assistant is a personal AI voice system built in Python.
Local. fast. no nonsense.

controls your machine • searches the web • talks via Gemini
voice or CLI — your choice

---

## ⚡ FEATURES

### 🤖 AI CORE

* **Conversation Engine** — powered by Gemini (`gemini-2.5-flash`)
* **Persona** — *Vyom*: sharp, helpful, no fluff

### 💻 SYSTEM CONTROL

* **Power Commands** — shutdown / restart / sleep (with confirmation)
* **System Stats** — battery • CPU • memory
* **Controls** — volume + brightness
* **App Launcher** — open anything (calculator, spotify, etc.)

### 🌐 CONNECTIVITY

* **Web Search** — real-time via DuckDuckGo (`ddgs`)
* **Shortcuts** — instant access (YouTube, GitHub, Reddit…)

### 🎙️ MODES

* **Voice Mode** — hands-free (`SpeechRecognition` + `pyttsx3`)

  * wake word: `jarvis`
* **Text Mode (CLI)** — fast, silent, direct

---

## 🚀 INSTALL

clone + setup:

gh repo clone FAHHHH-lab/VoiceAssist
cd VoiceAssist

python3.11 -m venv env
source env/bin/activate
pip install -r libs.txt

> use Python 3.11 for best stability

---

## 📦 DEPENDENCIES

* google.genai • SpeechRecognition • pyttsx3 • rich • pyaudio
* psutil (system stats)
* screen_brightness_control (display)
* ddgs (search)

---

## ▶️ USAGE

get API key: https://makersuite.google.com/app/apikey

run:

export GEMINI_API_KEY="<YOUR_API_KEY_HERE>"
python main.py

select mode:

* **T** → CLI mode
* **V** → Voice mode

---

## 🧪 COMMAND EXAMPLES

* search → *"latest space news"*
* system → *"battery level?"* / *"set brightness to 80%"*
* power → *"restart system"* → confirms before action
* apps → *"open spotify"*
* chat → *"tell me a joke"*

---

## ⚠️ NOTES

* microphone requires `pyaudio`
  → if it fails: install `portaudio` (e.g. `brew install portaudio`)

* macOS permissions may be needed
  → allow system control access for full functionality

* volume control → macOS + Linux only

* recommended Python:
  **3.9 ≤ version ≤ 3.11**

---

> FAHHST = fast. local. under your control.
