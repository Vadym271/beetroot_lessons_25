import socket
import  json
from client_echo31 import ceasar_cypher

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 6543  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data, shift = conn.recv(1024)
            obj = tuple(json.loads(data.decode()))
            if not data:
                break

            conn.sendall(ceasar_cypher(obj[0], obj[1]))
