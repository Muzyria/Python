import asyncio
import websockets


async def websocket_handler(websocket, path):
    while True:
        message = await websocket.recv()

        print(f"Отримано повідомлення: {message}")

        response = f"Ви сказали: {message}"
        await websocket.send(response)


start_server = websockets.serve(websocket_handler, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
