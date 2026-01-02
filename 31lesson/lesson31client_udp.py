import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"hello there", (HOST, PORT))
data, _ = client.recvfrom(1024)

print(data.decode())
