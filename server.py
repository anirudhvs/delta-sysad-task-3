import socket

import _thread as thread

HOST = '127.0.0.1'
PORT = 8888

def client_thread(conn, addr):
    conn.sendall(b'SuccessFully  Connected To Server')

    while True:
        try:
            message = conn.recv(1024)
            prompt= b'Server Recieved msg and sending Reply'
            conn.sendall(prompt)
            conn.sendall(message)
        except:
            pass

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST,PORT))
    s.listen()

    while True:
        conn , addr = s.accept()
        print(type(conn))

        print(f"Client {addr} Connected")
        thread.start_new_thread(client_thread,(conn,addr))

        
