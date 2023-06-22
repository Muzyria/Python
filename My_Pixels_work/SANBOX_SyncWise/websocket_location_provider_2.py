import json
import time

import websockets
import asyncio

class Preferences:
    default_config = {
        "lastLat": 37.73841,
        "lastLng": -122.23472,
        "lastAddress": "192.168.1.88",
        "lastSpeed": 0,
        "useSpeed": 1,
        "lastAcc": 0,
        "lastAlt": 0,
        "useAlt": 1
    }

    def __init__(self):
        self.json_object = self.load_preferences()

    def load_preferences(self):
        # Load preferences from storage or use default config
        prefs = None
        try:
            with open("preferences.json") as file:
                prefs = json.load(file)
        except FileNotFoundError:
            pass

        return prefs if prefs else self.default_config

    def save_preferences(self):
        # Save preferences to storage
        with open("preferences.json", "w") as file:
            json.dump(self.json_object, file)

    def last_lat(self, lat=None):
        if lat is None:
            return self.json_object["lastLat"]

        self.json_object["lastLat"] = lat
        return self

    def last_lng(self, lng=None):
        if lng is None:
            return self.json_object["lastLng"]

        self.json_object["lastLng"] = lng
        return self

    def last_address(self, address=None):
        if address is None:
            return self.json_object["lastAddress"]

        self.json_object["lastAddress"] = address
        return self

    def last_speed(self, speed=None):
        if speed is None:
            return self.json_object["lastSpeed"]

        self.json_object["lastSpeed"] = speed
        return self

    def use_speed(self, use=None):
        if use is None:
            return self.json_object["useSpeed"]

        self.json_object["useSpeed"] = use
        return self

    def last_acc(self, acc=None):
        if acc is None:
            return self.json_object["lastAcc"]

        self.json_object["lastAcc"] = acc
        return self

    def last_alt(self, alt=None):
        if alt is None:
            return self.json_object["lastAlt"]

        self.json_object["lastAlt"] = alt
        return self

    def use_alt(self, use=None):
        if use is None:
            return self.json_object["useAlt"]

        self.json_object["useAlt"] = use
        return self


class WebSocketClient:
    def __init__(self):
        self.socket = None
        self.connection_state = "disconnected"
        self.prefs = Preferences()

    async def open_connection(self, address):
        self.connection_state = "connecting"

        try:
            self.socket = await websockets.connect(f"ws://{address}:5557")
            self.connection_state = "connected"
            print("WebSocket connected")
        except Exception as e:
            self.close_connection()
            print(f"Connection error: {e}")

    async def close_connection(self):
        if self.socket is None:
            return

        await self.socket.close()
        self.socket = None
        self.connection_state = "disconnected"
        print("WebSocket closed")

    async def push_location_to_websocket(self, latitude, longitude, accuracy):
        if self.socket is None:
            return

        if self.connection_state != "connected":
            return

        packet = {
            "version": 1,
            "lat": float(latitude),
            "lng": float(longitude),
            "acc": float(accuracy)
        }

        if self.prefs.use_speed() == 1:
            speed = self.prefs.last_speed()
            packet["speed"] = float(speed)

        if self.prefs.use_alt() == 1:
            alt = self.prefs.last_alt()
            packet["alt"] = float(alt)

        print("Sending packet:", packet)
        await self.socket.send(json.dumps(packet))


async def main(latitude, longitude, accuracy):
    client = WebSocketClient()
    await client.open_connection("192.168.2.30")

    for _ in range(50):
        await client.push_location_to_websocket(latitude, longitude, accuracy)
        await asyncio.sleep(1)  # Даем время отправке пакета

    await client.close_connection()

# Пример использования
latitude = 50.07808654956364
longitude = 36.23110681531438
accuracy = 0

asyncio.run(main(latitude, longitude, accuracy))
