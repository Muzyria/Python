import json
import websockets

class WebSocketClient:
    def __init__(self):
        self.socket = None
        self.connection_state = "disconnected"

    async def open_connection(self, address):
        self.connection_state = "connecting"

        try:
            self.socket = await websockets.connect(f"ws://{address}:5557")
            self.connection_state = "connected"
            print("WebSocket connected")
        except Exception as e:
            await self.close_connection()
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

        print("Sending packet:", packet)
        await self.socket.send(json.dumps(packet))
