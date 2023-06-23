from websocket_client_2 import WebSocketClient
import asyncio
from generator_path_4_websocket import IntermediateCoordinatesGenerator

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

async def execute_scenario(address):
    connection_manager = WebSocketConnectionManager(address)
    await connection_manager.open_connection()

    try:
        # Вызов методов вычисления маршрута
        generator = IntermediateCoordinatesGenerator()
        route1 = generator.get_start_coordinates()
        await connection_manager.send_coordinates([route1[0]])
        print(route1[0])
        generator.touch_screen()
        await connection_manager.send_coordinates(route1)
        await asyncio.sleep(2)  # Дополнительная задержка

        # Дополнительные методы вычисления маршрута и отправки координат...
        iterator = generator.run_device(4)
        for _ in range(generator.client_data.COURSE_VECTOR_DETAILS_HOLECOUNT):
            route2 = next(iterator)
            print(route2[0])
            await connection_manager.send_coordinates([route2[0]])
            generator.touch_screen()
            await asyncio.sleep(2)  # Дополнительная задержка
            await connection_manager.send_coordinates(route2)

            await asyncio.sleep(1)  # Дополнительная задержка
        await asyncio.sleep(1)  # Дополнительная задержка

        # Вызов методов вычисления маршрута
        await connection_manager.send_coordinates(route1)
        await asyncio.sleep(1)  # Дополнительная задержка

    finally:
        await connection_manager.close_connection()

# Пример использования
address = "192.168.2.30"
asyncio.run(execute_scenario(address))
