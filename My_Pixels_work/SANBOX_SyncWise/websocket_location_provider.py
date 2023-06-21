import websocket

# Здесь используются строки для представления состояний соединения
CONNECTION_STATE_CONNECTING = "connecting"
CONNECTION_STATE_CONNECTED = "connected"
CONNECTION_STATE_DISCONNECTED = "disconnected"


def open_connection(address):
    def on_open(ws):
        set_connection_state(CONNECTION_STATE_CONNECTED)

    def on_close(ws, close_code, close_reason):
        set_connection_state(CONNECTION_STATE_DISCONNECTED)

    def on_error(ws, error):
        close_connection()
        print('Connection error')

    socket = websocket.WebSocketApp('ws://' + address + ':5557',
                                    on_open=on_open,
                                    on_close=on_close,
                                    on_error=on_error)
    socket.run_forever()


def set_connection_state(state):
    # Реализуйте логику установки состояния соединения
    print(f"Connection state changed: {state}")


def close_connection():
    # Реализуйте логику закрытия соединения
    print("Closing connection")






# Пример использования
open_connection('192.168.2.30')
