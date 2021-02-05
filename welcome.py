"""
This function saves a welcome message.
"""

import json

def welcome2():
    greeting2 = {
        "message": "Hello, orquestra world! 🎻",
        "schema": "another message",
    }

    with open("greeting2.json",'w') as f:
        f.write(json.dumps(greeting2, indent=2)) # Write message to file as this will serve as output artifact
