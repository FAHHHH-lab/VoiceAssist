import speech_recognition as sr
import pyttsx3
import os
import google.genai as genai
from google.genai import types
from rich.console import Console
from rich.markdown import Markdown
from system_tools import SystemTools

console = Console()

# Initialize the TTS engine once
engine = pyttsx3.init()

# Global config for TTS
TTS_ENABLED = True

def speak(text: str):
    if TTS_ENABLED:
        engine.say(text)
        engine.runAndWait()

def process_command(cmd: str):
    sys_tools = SystemTools()
    
    # Define tool mapping for system tools
    # Note: Google Search is handled natively by Gemini config, not manual mapping in this loop style usually,
    # but the python client handles it if we pass the Tool object.
    
    # We combine system tools with Google Search
    tools_list = [
        sys_tools.shutdown_system,
        sys_tools.restart_system,
        sys_tools.sleep_system,
        sys_tools.get_battery_status,
        sys_tools.get_system_stats,
        sys_tools.set_brightness,
        sys_tools.set_volume,
        sys_tools.open_app,
        sys_tools.open_website,
        sys_tools.web_search,
    ]

    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    model = "gemini-2.5-flash"
    
    persona = [
        "You're Vyom, a helpful Gen Alpha assistant.",
        "Always call the user 'Sir'.",
        "You speak professional, talkative Gen Alpha style, markdown format only. Keep your responses extremely extremely short like a voice assistant.",
        "You have access to system tools AND a web search tool. USE THEM freely.",
        "If asked to search or for info you don't know, YOU MUST USE the 'web_search' tool. Do not just say you will search.",
        "After searching, summarize the results for the user.",
        "CRITICAL: For 'shutdown_system' and 'restart_system', you MUST ask for explicit confirmation first if the user hasn't provided it in the current turn.",
    ]

    config = types.GenerateContentConfig(
        system_instruction=persona,
        tools=tools_list,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
             disable=False,
             maximum_remote_calls=3
        ), 
    )

    try:
        chat = client.chats.create(
            model=model,
            config=config,
            history=[]
        )
        
        # Send message
        response = chat.send_message(cmd)
        
        # Text response
        if response.text:
            console.rule("[bold cyan]BOT")
            console.print(Markdown(response.text))
            speak(response.text)
            
    except Exception as e:
        console.print(f"[bold red]AI Error:[/bold red] {e}")
        if TTS_ENABLED:
            speak("I encountered an error processing that request.")


def listen_continuously():
    r = sr.Recognizer()
    mic = sr.Microphone()
    wake_word = "jarvis"

    with mic as source:
        console.print("[yellow]Calibrating microphone...[/yellow]")
        r.adjust_for_ambient_noise(source, duration=1)
        speak("Jarvis online, waiting for your call.")

    while True:
        try:
            with mic as source:
                console.print("[green]Listening...[/green]")
                audio = r.listen(source,phrase_time_limit=5,timeout=2)

            command = r.recognize_google(audio).lower().strip()  # type: ignore
            console.print(f"[bold magenta]You said:[/bold magenta] {command}")

            if command == "exit":
                speak("Shutting down")
                break

            # Wake-word check
            if command.startswith(wake_word):
                speak("Yes Sir")
                # Remove wake word from command
                actual_cmd = command.replace(wake_word, "", 1).strip()

                if actual_cmd:
                    process_command(actual_cmd)
                else:
                    console.print("[cyan]Awaiting your command...[/cyan]")

            else:
                console.print("[dim]Ignored (no wake word detected)[/dim]")

        except sr.UnknownValueError:
            console.print("[blue]Could not understand audio[/blue]")

        except sr.RequestError:
            speak("Recognition service unavailable")
            break

        except KeyboardInterrupt:
            speak("Shutting down")
            break

        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

def start_text_mode():
    global TTS_ENABLED
    TTS_ENABLED = False # Disable TTS for text mode
    console.print("[green]Entered Text Mode. Type 'exit' to quit.[/green]")
    while True:
        try:
            cmd = console.input("[bold magenta]>>> [/bold magenta]")
            if cmd.lower() in ["exit", "quit", "shutdown"]:
                break
            if not cmd.strip():
                continue
            process_command(cmd)
        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    try:
        console.rule("[bold yellow]VoiceAssist Configuration")
        mode = console.input("[bold cyan]Select Mode (T for Text / V for Voice): [/bold cyan]").strip().upper()
        
        if mode == 'T':
            start_text_mode()
        elif mode == 'V':
            listen_continuously()
        else:
            console.print("[red]Invalid mode selected. Defaulting to Voice.[/red]")
            listen_continuously()
            
    except KeyboardInterrupt:
        print("\nExiting...")