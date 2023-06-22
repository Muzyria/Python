from websocket_client_2 import WebSocketClient
import asyncio


async def send_coordinates(address, coordinates):
    client = WebSocketClient()
    await client.open_connection(address)

    for coord in coordinates:
        await client.push_location_to_websocket(coord[0], coord[1], 0)
        await asyncio.sleep(1)  # Даем время отправке пакета

    await client.close_connection()


def push(coordinates_list):
    address = "192.168.3.219"
    asyncio.run(send_coordinates(address, coordinates_list))
