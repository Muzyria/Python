# import asyncio
# import websockets
#
#
# async def websocket_handler(websocket, path):
#     while True:
#         message = await websocket.recv()
#
#         print(f"Отримано повідомлення: {message}")
#
#         response = f"Ви сказали: {message}"
#         await websocket.send(response)
#
#
# start_server = websockets.serve(websocket_handler, 'localhost', 8765)
#
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


import hmac
import hashlib
import base64
import socketio
import json

# Инициализация сокетного соединения
sio = socketio.Client()


# Пример класса хранения данных
class Storage:
    def get_data_field(self, field_name):
        data = {
            'username': 'your_username',  # Замените 'your_username' на ваше значение
            'token': 'your_token'  # Замените 'your_token' на ваше значение
        }
        return data.get(field_name)


# Конфигурация окружения
class Environment:
    APP_SECRET_KEY = 'your_app_secret_key'  # Замените 'your_app_secret_key' на ваше значение
    APP_API_KEY = 'your_app_api_key'  # Замените 'your_app_api_key' на ваше значение


storage = Storage()
environment = Environment()


def emit_sign_auth():
    # Получение имени пользователя и ключа
    username = storage.get_data_field('username')
    key = (environment.APP_SECRET_KEY + storage.get_data_field('token')).encode('utf-8')

    # Создание подписи HMAC и кодирование в Base64
    signature = hmac.new(key, username.encode('utf-8'), hashlib.sha256).digest()
    signature_base64 = base64.b64encode(signature).decode('utf-8')

    # Формирование JSON-объекта для отправки
    object_json = {
        'username': username,
        'signature': signature_base64,
        'apikey': environment.APP_API_KEY
    }

    # Отправка события signAuth
    sio.emit('signAuth', object_json)

    # Обработчик события message
    @sio.event
    def message(data):
        message = json.loads(data)
        if not message.get('sts'):
            # Обработка сообщения по необходимости
            pass

    # Обработчик события change
    @sio.event
    def change(data):
        # Обработка события change по необходимости
        pass


# Подключение к серверу WebSocket
sio.connect('http://your_server_address')  # Замените 'http://your_server_address' на адрес вашего сервера

# Отправка события signAuth
emit_sign_auth()

# Начало прослушивания событий
sio.wait()

