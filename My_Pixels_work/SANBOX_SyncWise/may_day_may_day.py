# from websocket_client_2 import WebSocketClient
# import asyncio
#
#
# async def send_coordinates(address, coordinates):
#     client = WebSocketClient()
#     await client.open_connection(address)
#
#     for coord in coordinates:
#         await client.push_location_to_websocket(coord[0], coord[1], 0)
#         await asyncio.sleep(1)  # Даем время отправке пакета
#
#     await client.close_connection()
#
#
# def push(ip_device, coordinates_list):
#     asyncio.run(send_coordinates(ip_device, coordinates_list))
from websocket_client_2 import WebSocketClient
import asyncio


class WebSocketConnectionManager:
    def __init__(self, address):
        self.client = WebSocketClient()
        self.address = address
        self.connection_opened = False

    async def open_connection(self):
        if not self.connection_opened:
            await self.client.open_connection(self.address)
            self.connection_opened = True

    async def close_connection(self):
        if self.connection_opened:
            await self.client.close_connection()
            self.connection_opened = False

    async def send_coordinates(self, coordinates):
        await self.open_connection()

        for coord in coordinates:
            await self.client.push_location_to_websocket(coord[0], coord[1], 0)
            await asyncio.sleep(1)  # Даем время отправке пакета

    async def send_coordinates_and_close(self, coordinates):
        await self.send_coordinates(coordinates)
        await self.close_connection()


def push(ip_device, coordinates_list):
    # connection_manager = WebSocketConnectionManager(ip_device)
    # asyncio.run(connection_manager.send_coordinates_and_close(coordinates_list))
    connection_manager = WebSocketConnectionManager(ip_device)
    await connection_manager.open_connection()  # Открыть соединение

    # Отправить координаты
    await connection_manager.send_coordinates(coordinates_list)

    # Другие операции...

    await connection_manager.close_connection()  # Разорвать соединение