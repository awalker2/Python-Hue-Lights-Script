# Python-Hue-Lights-Script
Script to turn Phillips Hue lights on or off or change brightness by id

This script was created in order to control Phillips Hue lights in my bedroom with a commandline executable. 
I have a Logitech keyboard with macro keys that cannot run Python scripts, but can run .exe files with arguments.
Running the script as a .exe in the background works well for my use case.

I would have liked to add the Hub user ID and IP as envioronment variables, but it did not work
when I added the application to be run in Logitech G HUB, so I pass them in as commands.

How to run:
1 - python -m venv venv
2 - Switch to the virtual environment
3 - pip install requirements.txt
4 - The script can be run standalone, but I also run it as an .exe with noconsole so it runs in the background from my keyboard: 
      pyinstaller --noconsole --onefile modify_lights.py
5 - Run the script like in the examples below.


Examples 
Toggle Bedroom Lights
modify_lights.exe --user "HUB USER ID" --ip "HUB IP" --action "toggle" --lights "[3,4]"
Dim Bedroom Lights
modify_lights.exe --user "HUB USER ID" --ip "HUB IP" --action "dimmer" --lights "[3,4]"
Brighten Bedroom Lights
modify_lights.exe --user "HUB USER ID" --ip "HUB IP" --action "brighter" --lights "[3,4]"
Toggle Desk LEDs
modify_lights.exe --user "HUB USER ID" --ip "HUB IP" --action "toggle" --lights "[5]"
