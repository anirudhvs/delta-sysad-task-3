import socket
import select
import sys
import subprocess

endedConnection = False

HOST = 'localhost'
PORT = 8888 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

print("Welcome to The Chatting Interface ")
print("Press Ctrl + C to Quit The Interface")

shell_command= subprocess.Popen(['whoami'],stdout = subprocess.PIPE , stderr = subprocess.PIPE)
belongsTo , error = shell_command.communicate()
s.sendall(belongsTo[:-1])


rlist = [sys.stdin , s ]



while True:

    read_socket , write_socket , error_socket = select.select(rlist , [] ,[])

    for sock in read_socket:
        if sock == s:
            message = s.recv(1024) 
            if message == b'':
                print("Server Ended Connection")
                endedConnection = True

            sys.stdout.write(message.decode('utf-8'))
            sys.stdout.flush()

        else:
            message = sys.stdin.readline()
            if message == "\n":
                continue
            sys.stdout.write("<Me> : ")
            sys.stdout.write(message)
            sys.stdout.flush()
            b = message.encode('utf-8')
            s.sendall(b)
    
    if endedConnection:
        break

s.close()