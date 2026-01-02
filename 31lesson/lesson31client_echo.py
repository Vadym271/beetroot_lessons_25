import socket
import json

def ceasar_cypher(data, shift):
    result = ""
    for i in data:
        if i == " ":
            result += " "
        elif i.isupper():
            result += chr((ord(i) + shift-65) % 26 + 65)
        else:
            result += chr((ord(i) + shift - 97) % 26 + 97)

    return result

if __name__ == "__main__":

    n = 3

    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 6543  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = ("we are going up up up, it's our moment", n)
        payload = json.dumps(data).encode()
        s.sendall(payload)
        data = s.recv(1024)
        data = ceasar_cypher(data.decode(), n)

    print(f"Received {data}")
