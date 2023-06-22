from websocket_client_2 import WebSocketClient
import asyncio

async def send_coordinates(address, coordinates):
    client = WebSocketClient()
    await client.open_connection(address)

    for coord in coordinates:
        await client.push_location_to_websocket(coord[0], coord[1], 0)
        await asyncio.sleep(1)  # Даем время отправке пакета

    await client.close_connection()

# Пример вызова
latitude = 42.123456
longitude = -71.987654
accuracy = 0
coordinates = [(42.1, -71.9), (42.2, -71.8), (42.3, -71.7)]  # Список координат

address = "192.168.2.30"
asyncio.run(send_coordinates(address, coordinates))
