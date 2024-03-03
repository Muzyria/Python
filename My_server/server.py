import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))

server.listen()

while True:
    user, address = server.accept()
    #
    # print("connect")
    # user.send("connect".encode("utf-8"))

    user.send(input().encode("utf-8"))

    data = user.recv(1024)
    print(data.decode("utf-8"))
