import socket

HOST = '127.0.0.1'
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        message = input("Enter a message: ")
        s.sendall(message.encode())
