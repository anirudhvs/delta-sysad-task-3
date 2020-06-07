import socket

import _thread as thread

import sys

f= open('/dev/null','w')
sys.stdout=f

HOST = 'localhost'
PORT = 8888

print("Server Started!!")

ARMY  = []
NAVY = []
AIRFORCE = []
HIGHERUPS = []

def category(user):
    if len(user)>=11 and (user == "ChiefCommander" or user == "ArmyGeneral" or user == "NavyMarshal" or user == "AirForceChief"):
        return user.lower()
    
    elif len(user)>=8 and user[:8]=="AirForce":
        return "airforce"
    elif user[:4]=="Navy":
        return "navy"
    elif user[:4]=="Army":
        return "army"


def armybroadcast(user,message,conn):
    print("Army Broadcast Called : ")
    for member in ARMY:
        if(member!=conn):
            print(f"Sending message to {member}")
            member.sendall(message)
            
def navybroadcast(user,message,conn):
    print("Navy Broadcast Called : ")
    for member in NAVY:
        if(member!=conn):
            print(f"Sending message to {member}")
            member.sendall(message)
            
def airforcebroadcast(user,message,conn):
    print("AirForce Broadcast Called : ")
    for member in AIRFORCE:
        if(member!=conn):
            print(f"Sending message to {member}")
            member.sendall(message)

def higherbroadcast(user,message,conn):
    print("HigherUp BroadCast Called")
    for member in HIGHERUPS:
        if(member!=conn):
            print(f"Sending message to {member}")
            member.sendall(message)

    if category(user) == "armygeneral" or category(user)=="chiefcommander":
        armybroadcast(user,message,conn)
    elif category(user) == "navymarshal" or category(user)=="chiefcommander":
        navybroadcast(user,message,conn)
    elif category(user) == "airforcechief" or category(user)=="chiefcommander":
        airforcebroadcast(user,message,conn)

def client_thread(conn, addr , belongsTo , user):
    conn.sendall(b'SuccessFully  Connected To Server')

    while True:
        try:
            message = conn.recv(1024)

            print(f"Message recieved from {addr} : {belongsTo}")
            print(f"Message is : {message}")

            if message == b'':
                if belongsTo == "army":
                    conn.close()
                    ARMY.remove(conn)
                elif belongsTo == "navy":
                    conn.close()
                    NAVY.remove(conn)
                elif belongsTo == "airforce":
                    conn.close()
                    AIRFORCE.remove(conn)
                elif belongsTo == "armygeneral":
                    conn.close()
                    ARMY.remove(conn)
                    HIGHERUPS.remove(conn)
                elif belongsTo == "navymarshal":
                    conn.close()
                    NAVY.remove(conn)
                    HIGHERUPS.remove(conn)
                elif belongsTo == "airforcechief":
                    conn.close()
                    AIRFORCE.remove(conn)
                    HIGHERUPS.remove(conn)
                elif belongsTo == "chiefcommander":
                    conn.close()
                    ARMY.remove(conn)
                    NAVY.remove(conn)
                    AIRFORCE.remove(conn)
                
                break

                   
                            
            if message != b'':
                message = b"<" + user.encode('utf-8') + b"> : " + message
                if belongsTo == "army" :
                    armybroadcast(user,message,conn)
                elif belongsTo == "navy" :
                    navybroadcast(user,message,conn)
                elif belongsTo == "airforce" :
                    airforcebroadcast(user,message,conn)
                else :
                    higherbroadcast(user,message,conn)
                    

        except:
            pass




with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST,PORT))
    s.listen()

    while True:
        conn , addr = s.accept()

        b = conn.recv(1024)
        user = b.decode('utf-8')
        belongsTo = category(user)

        print(f"{user} belongs To : {belongsTo}")
        
        if belongsTo == "army" or belongsTo == "armygeneral" or belongsTo=="chiefcommander":
            ARMY.append(conn)
            print(ARMY)
        
        if belongsTo == "navy" or belongsTo == "navymarshal" or belongsTo=="chiefcommander" :
            NAVY.append(conn)
            print(NAVY)

        if belongsTo == "airforce" or belongsTo == "airforcechief" or belongsTo=="chiefcommander" :
            AIRFORCE.append(conn)
            print(AIRFORCE)
        if belongsTo=="armygeneral" or belongsTo == "navymarshal" or belongsTo == "airforcechief":
            HIGHERUPS.append(conn)

        print(f"Client {addr} Connected")
        thread.start_new_thread(client_thread,(conn,addr, belongsTo,user))