import websocket
import json

class WebSocketClient:
    def __init__(self):
        self.socket = None

    def open_connection(self, address):
        def on_open(ws):
            self.set_socket(ws)
            print("WebSocket connected")

        def on_close(ws, close_code, close_reason):
            self.close_connection()
            print("WebSocket closed")

        def on_error(ws, error):
            self.close_connection()
            print('Connection error')

        self.socket = websocket.WebSocketApp('ws://' + address + ':5557',
                                             on_open=on_open,
                                             on_close=on_close,
                                             on_error=on_error)
        self.socket.run_forever()

    def set_socket(self, ws):
        self.socket = ws

    def push_location_to_websocket(self, lat, lng, acc):
        if self.socket is None:
            print("WebSocket is not connected")
            return

        packet = {
            "version": 1,
            "lat": float(lat),
            "lng": float(lng),
            "acc": float(acc)
        }

        # Преобразование в JSON и отправка пакета
        self.socket.send(json.dumps(packet))

    def close_connection(self):
        if self.socket is not None:
            self.socket.close()
        self.socket = None

# Пример использования из другого файла
address = '192.168.2.30'

# Создание экземпляра клиента WebSocket
client = WebSocketClient()

# Открытие соединения
client.open_connection(address)

# Вызываем push_location_to_websocket() с координатами
latitude = 42.123456
longitude = -71.987654
accuracy = 10.5
client.push_location_to_websocket(latitude, longitude, accuracy)

# Закрываем соединение
client.close_connection()
