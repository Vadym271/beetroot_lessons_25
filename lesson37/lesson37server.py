import socket
import threading

def handle(connection, address):
    connection.send("NICK".encode())
    nickname = connection.recv(1024).decode()
    clients[connection] = nickname

    while True:
        message = connection.recv(1024).decode()
        if not message:
            break
        broadcast(f"\n{message}", connection)

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            client.send(message.encode())

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 6543
clients = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

while True:
    conn, add = server.accept()
    thread = threading.Thread(target=handle, args=(conn, add))
    thread.start()
