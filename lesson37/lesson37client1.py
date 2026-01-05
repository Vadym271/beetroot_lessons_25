import socket
import threading

nickname = input("Choose your nickname: ")

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 6543  # Port to listen on (non-privileged ports are > 1023)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(nickname.encode())
            else:
                print(message)
        except:
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input("print your message:")}"
        client.send(message.encode())

receive_threads = threading.Thread(target= receive)
receive_threads.start()

write_thread = threading.Thread(target= write)
write_thread.start()