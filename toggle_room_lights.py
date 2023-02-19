import requests
import argparse
import json
import time
import os

bridge_ip = os.getenv("HUE_BRIDGE_IP")
user_id = os.getenv("HUE_USER_ID")
# 30 Matches the step of the official Hue switch
brightness_step = 30

parser = argparse.ArgumentParser(
        prog = 'Hue Lights Modify',
        description = 'Turns A List of Lights by ID on/off or raises/lowers the brightness',
        epilog = 'Text at the bottom of help')

parser.add_argument('-a', '--action',help='Action= toggle, brighter, dimmer', required=True)
parser.add_argument(
    '-l', '--lights',  # either of this switches
    type=json.loads,        # /parameters/ are ints
    default=[]      # since we're not specifying required.
)
args = parser.parse_args()
action = args.action
light_ids = args.lights

session = requests.session()
session.verify = False
session.headers = {
  'Content-Type': 'application/json'
}

time.sleep(0.25)
if action == 'toggle':
    light_states = []
    for light_id in light_ids:
        light_state = session.get(f"https://{bridge_ip}/api/{user_id}/lights/{light_id}/").json()["state"]["on"]
        light_states.append(light_state)

    new_state = None
    if True in light_states:
        new_state = False
    else:
        new_state = True

    for light_id in light_ids:
        request = session.put(
            f"https://{bridge_ip}/api/{user_id}/lights/{light_id}/state", 
            json={"on": new_state}
        )
        print(request.json())
elif action == 'brighter' or action == 'dimmer':
    lights_bris = {}
    for light_id in light_ids:
        light_bri = session.get(f"https://{bridge_ip}/api/{user_id}/lights/{light_id}/").json()["state"]["bri"]
        # Light value is 0-254
        if action == 'brighter':
            new_bri = min([light_bri + brightness_step, 254])
        elif action == 'dimmer':
            new_bri = max([light_bri - brightness_step, 0])
        lights_bris[light_id] = new_bri
    for light_id in light_ids:
        request = session.put(
            f"https://{bridge_ip}/api/{user_id}/lights/{light_id}/state", 
            json={"bri": lights_bris[light_id]}
        )
        print(request.json())
else:
    print("Invalid action")


