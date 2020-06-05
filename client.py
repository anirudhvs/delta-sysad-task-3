import socket
import select
import sys
import subprocess


HOST = '127.0.0.1'
PORT = 8888 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

print("Welcome to The Chatting Interface ")
print("Press Ctrl + C to Quit The Interface")

shell_command= subprocess.Popen(['whoami'],stdout = subprocess.PIPE , stderr = subprocess.PIPE)
belongsTo , error = shell_command.communicate()
b=belongsTo.encode('utf-8')
s.sendall(b)


rlist = [sys.stdin , s ]


while True:

    read_socket , write_socket , error_socket = select.select(rlist , [] ,[])

    for sock in read_socket:
        if sock == s:
            message = s.recv(1024) 
            sys.stdout.write(message.decode('utf-8'))
            sys.stdout.flush()
        
        else:
            message = sys.stdin.readline()
            sys.stdout.write("<Me> : ")
            sys.stdout.write(message)
            sys.stdout.flush()
            b = message.encode('utf-8')
            s.sendall(b)

s.close()