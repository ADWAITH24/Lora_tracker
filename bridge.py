import serial
import requests
import json

# Configuration
ser = serial.Serial('COM10', 9600) # Replace 'COM3' with your Arduino port
FIREBASE_URL = "https://myloramap-4cc73-default-rtdb.asia-southeast1.firebasedatabase.app/"

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print(f"Received: {line}")
        
        # Split your data (Assumes format: lat,lng,msg)
        parts = line.split(',')
        if len(parts) >= 3:
            payload = {
                "lat": float(parts[0]),
                "lng": float(parts[1]),
                "msg": parts[2]
            }
            # Send to Firebase
            requests.put(FIREBASE_URL, data=json.dumps(payload))