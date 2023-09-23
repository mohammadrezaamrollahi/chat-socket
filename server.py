import socket

HOST = '127.0.0.1' 
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  
    s.listen()  
    print('Server started and listening for incoming connections...')
    
    con, addr = s.accept()
    print('Client connected:', addr)
    while True:
        data = con.recv(1024)  
        print(f'Received {data.decode("utf-8")} from {con.getpeername()}')
