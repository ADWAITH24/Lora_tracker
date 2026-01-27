import requests
import json
import time
import random

FIREBASE_URL = "https://myloramap-4cc73-default-rtdb.asia-southeast1.firebasedatabase.app/"

# Starting coordinates
lat, lng = 12.9716, 77.5946

while True:
    # Randomly "walk" the coordinates slightly
    lat += random.uniform(-0.001, 0.001)
    lng += random.uniform(-0.001, 0.001)
    
    payload = {
        "lat": lat,
        "lng": lng,
        "msg": "Simulator Active",
        "time": time.strftime("%H:%M:%S")
    }
    
    # Push to Firebase
    requests.put(FIREBASE_URL, data=json.dumps(payload))
    print(f"Simulated position sent: {lat}, {lng}")
    
    time.sleep(2) # Update every 2 seconds