import socket

import _thread as thread

HOST = '127.0.0.1'
PORT = 8888

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
    for member in ARMY:
        if(member!=conn):
            try:
                member.sendall("<"+user+"> : "+message)
            except:
                member.close()
                ARMY.remove(member)
def navybroadcast(user,message,conn):
    for member in NAVY:
        if(member!=conn):
            try:
                member.sendall("<"+user+"> : "+message)
            except:
                member.close()
                NAVY.remove(member)

def airforcebroadcast(user,message,conn):
    for member in AIRFORCE:
        if(member!=conn):
            try:
                member.sendall("<"+user+"> : "+message)
            except:
                member.close()
                AIRFORCE.remove(member)

def higherbroadcast(user,message,conn):
    for member in HIGHERUPS:
        if(member!=conn):
            try:
                member.sendall("<"+user+"> : "+message)
            except:
                member.close()
                if member in HIGHERUPS:
                    HIGHERUPS.remove(member)
    if category(user) == "armygeneral":
        pass

def client_thread(conn, addr , belongsTo , user):
    conn.sendall(b'SuccessFully  Connected To Server')

    while True:
        try:
            message = conn.recv(1024)

            print(f"Message recieved from {addr} : {belongsTo}")
            print(f"Message is : {message}")

            if message == b'':
                if belongsTo == "army" or belongsTo =="armygeneral" or belongsTo == "chiefcommander":
                    conn.close()
                    ARMY.remove(conn)
                    break
                elif belongsTo == "navy" or belongsTo =="navymarshal" or belongsTo == "chiefcommander":
                    conn.close()
                    NAVY.remove(conn)
                    break
                elif belongsTo == "airforce" or belongsTo =="airforcechief" or belongsTo == "chiefcommander":
                    conn.close()
                    AIRFORCE.remove(conn)
                    break
                   
                            
            if message != b'':
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

        print(f"The connected one belongs To : {user}")
        
        if belongsTo == "army" or belongsTo == "armygeneral" or belongsTo=="chiefcommander":
            ARMY.append(conn)
            print(ARMY)
        
        if belongsTo == "navy" or belongsTo == "navymarshal" or belongsTo=="chiefcommander" :
            NAVY.append(conn)
            print(NAVY)

        if belongsTo == "airforce" or belongsTo == "airforcechief" or belongsTo=="chiefcommander" :
            AIRFORCE.append(conn)
            print(AIRFORCE)
        if belongsTo == "chiefcommander" or belongsTo=="armygeneral" or belongsTo == "navymarshal" or belongsTo == "airforcechief":
            HIGHERUPS.append(conn)

        print(f"Client {addr} Connected")
        thread.start_new_thread(client_thread,(conn,addr, belongsTo,user))