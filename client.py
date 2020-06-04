import socket
import select
import sys



HOST = '127.0.0.1'
PORT = 8888 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

print("Welcome to The Chatting Interface ")
print("Press Ctrl + C to Quit The Interface")

rlist = [sys.stdin , s ]

while True:

    read_socket , write_socket , error_socket = select.select(rlist , [] ,[])

    for sock in read_socket:
        if sock == s:
            message = s.recv(1024) 
            print (message.decode('utf-8'))
        
        else:
            message = sys.stdin.readline()
            print(f"<You>:{message}")
            b = message.encode('utf-8')
            s.sendall(b)