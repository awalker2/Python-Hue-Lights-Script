# Python-Hue-Lights-Script
Script to turn Phillips Hue lights on or off or change brightness by id

This script was created in order to control Phillips Hue lights in my bedroom with a commandline executable. 
I have a Logitech keyboard with macro keys that cannot run Python scripts, but can run .exe files with arguments.
Running the script as a .exe in the background works well for my use case.

How to run:
1 - Set HUE_BRIDGE_IP and HUE_USER_ID environment variables for your Hue hub.
2 - python -m venv venv
3 - Switch to the virtual environment
4 - pip install requirements.txt
5 - The script can be run standalone, but I also run it as an .exe with noconsole so it runs in the background from my keyboard: 
      pyinstaller --noconsole --onefile modify_lights.py
6 - Run the script like in the examples below.


Examples 
Toggle Bedroom Lights
modify_lights.exe --action "toggle" --lights "[3,4]"
Dim Bedroom Lights
modify_lights.exe --action "dimmer" --lights "[3,4]"
Brighten Bedroom Lights
modify_lights.exe --action "brighter" --lights "[3,4]"
Toggle Desk LEDs
modify_lights.exe --action "toggle" --lights "[5]"
