import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print("server is running...")

data, address = server.recvfrom(1024)
print("Received:", data.decode(), "from", address)
server.sendto(b"Hello from UDP server", address)

