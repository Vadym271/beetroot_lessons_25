# task 2

import socket
import threading

def handle_client(connection, address):
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break

def start_server():
    HOST = '127.0.0.1'
    PORT = 6543
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("server is listening")
        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()