import os
import subprocess
import psutil
import screen_brightness_control as sbc
import webbrowser
from ddgs import DDGS
from typing import Dict, Any

class SystemTools:
    """
    A collection of system tools for VoiceAssist to perform hardware and OS level actions.
    """
    
    def web_search(self, query: str) -> str:
        """
        Performs a web search using DuckDuckGo and returns the top results.
        Use this to answer questions about current events, facts, or general knowledge.
        """
        print(f"[SystemTools] Searching Web for: {query}...")
        try:
            results = DDGS().text(query, max_results=5)
            if not results:
                return "No results found."
            
            # Format results
            response = [f"Result {i+1}: {r['title']}\n{r['body']}" for i, r in enumerate(results)]
            return "\n\n".join(response)
        except Exception as e:
            return f"Error performing web search: {e}"

    def shutdown_system(self):
        """
        Shuts down the system.
        """
        # In a real scenario, we might want to verify confirmation here again,
        # but the prompt engineering in main.py should handle the "ask for confirmation" part.
        # This function executes the command.
        if os.name == 'nt': # Windows
            os.system("shutdown /s /t 1")
        else: # Mac/Linux
            # Requires sudo or user permissions. On Mac 'osascript' is safer for user session.
            subprocess.run(["osascript", "-e", 'tell app "System Events" to shut down'])
            # Fallback if osascript fails or for Linux:
            # os.system("shutdown -h now") 

    def restart_system(self):
        """
        Restarts the system.
        """
        if os.name == 'nt':
            os.system("shutdown /r /t 1")
        else:
            subprocess.run(["osascript", "-e", 'tell app "System Events" to restart'])
            # os.system("shutdown -r now")

    def sleep_system(self):
        """
        Puts the system to sleep.
        """
        if os.name == 'nt':
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            subprocess.run(["pmset", "sleepnow"])

    def get_battery_status(self) -> str:
        """
        Returns the current battery percentage and charging status.
        """
        try:
            battery = psutil.sensors_battery()
            if battery:
                percent = battery.percent
                charging = "charging" if battery.power_plugged else "not charging"
                return f"Battery is at {percent}% and is {charging}."
            else:
                return "Battery information not available."
        except Exception as e:
            return f"Error getting battery status: {e}"

    def get_system_stats(self) -> str:
        """
        Returns CPU and Memory usage.
        """
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        return f"CPU Usage: {cpu_percent}%. Memory Usage: {memory.percent}%."

    def set_brightness(self, level: int):
        """
        Sets the screen brightness to the specified percentage (0-100).
        """
        try:
            sbc.set_brightness(level)
            return f"Brightness set to {level}%."
        except Exception as e:
            return f"Error setting brightness: {e}"

    def set_volume(self, level: int):
        """
        Sets the system volume to the specified percentage (0-100).
        MacOS only implementation for now.
        """
        try:
            # AppleScript to set volume (0-100 maps to 0-7 roughly? No, output volume is 0-100)
            # Actually 'set volume output volume' takes 0-100
            subprocess.run(["osascript", "-e", f"set volume output volume {level}"])
            return f"Volume set to {level}%."
        except Exception as e:
            return f"Error setting volume: {e}"

    def open_app(self, app_name: str):
        """
        Opens an application by name.
        """
        try:
            if os.name == 'nt':
                # Windows implementation logic (simplified)
                os.system(f"start {app_name}")
            else:
                # MacOS
                subprocess.run(["open", "-a", app_name])
            return f"Opening {app_name}..."
        except Exception as e:
            return f"Error opening app: {e}"
    
    def open_website(self, url: str):
        """
        Opens a website.
        """
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)
        return f"Opening {url}..."
