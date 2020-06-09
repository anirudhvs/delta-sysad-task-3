import socket
import select
import sys
import subprocess
import pymysql
import datetime

endedConnection = False

HOST = 'localhost'
PORT = 8888 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

print("Welcome to The Chatting Interface ")
print("Type EXITCHAT to Quit The Interface . Type PRINTCHAT to print messages")

shell_command= subprocess.Popen(['whoami'],stdout = subprocess.PIPE , stderr = subprocess.PIPE)
user , error = shell_command.communicate()
user = user[:-1]
s.sendall(user)

user = user.decode('utf-8')

rlist = [sys.stdin , s ]


print("Please Wait Until Previous Messages Are Loaded !!!")

#### GETTING LAST LOGIN TIME
currentTimestamp=datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

chats = pymysql.connect('db','root','root1234','socketchat')
cursor = chats.cursor()

sql="SELECT * FROM lastlogin WHERE `user` LIKE '%s'"%(user)

cursor.execute(sql)
result = cursor.fetchone()
if result == None:
    prev_time=datetime.datetime(datetime.MINYEAR,1,1).strftime("%Y-%m-%d %H:%M:%S")
    
    sqlinsert = "INSERT INTO lastlogin(`user`) VALUES('%s')"%(user)
    cursor.execute(sqlinsert)
    chats.commit() 

else:
    prev_time=result[1]


def category(user):
    if len(user)>=11 and (user == "ChiefCommander" or user == "ArmyGeneral" or user == "NavyMarshal" or user == "AirForceChief"):
        return user.lower()
    
    elif len(user)>=8 and user[:8]=="AirForce":
        return "airforce"
    elif user[:4]=="Navy":
        return "navy"
    elif user[:4]=="Army":
        return "army"


#### COLLECTING PREVIOUS MESSAGES
def message_collector(user , curTime):
    sqlarmy = "SELECT * FROM messages WHERE (`belongsto` LIKE 'army'\
        OR `belongsto` LIKE 'armygeneral'\
        OR `belongsto` LIKE 'chiefcommander') AND `time` > '%s' "%(curTime)
    sqlnavy = "SELECT * FROM messages WHERE (`belongsto` LIKE 'navy'\
        OR belongsto LIKE 'navymarshal'\
        OR belongsto LIKE 'chiefcommander') AND `time` > '%s' "%(curTime)
    sqlairforce = "SELECT * FROM messages WHERE (`belongsto` LIKE 'airforce'\
        OR `belongsto` LIKE 'airforcechief'\
        OR `belongsto` LIKE 'chiefcommander') AND `time` > '%s' "%(curTime)
    sqlchief = "SELECT * FROM messages WHERE `time` > '%s' "%(curTime)
    sqlarmygeneral = "SELECT * FROM messages WHERE (`belongsto` LIKE 'army'\
        OR `belongsto` LIKE 'chiefcommander'\
        OR `belongsto` LIKE 'navymarshal'\
        OR `belongsto` LIKE 'airforcechief') AND `time` > '%s' "%(curTime)
    sqlnavymarshal = "SELECT * FROM messages WHERE (`belongsto` LIKE 'navy'\
        OR `belongsto` LIKE 'chiefcommander'\
        OR `belongsto` LIKE 'armygeneral'\
        OR `belongsto` LIKE 'airforcechief') AND `time` > '%s' "%(curTime)
    sqlairforcechief = "SELECT * FROM messages WHERE (`belongsto` LIKE 'airforce'\
        OR `belongsto` LIKE 'chiefcommander'\
        OR `belongsto` LIKE 'armygeneral'\
        OR `belongsto` LIKE 'navymarshal') AND `time` > '%s' "%(curTime)

    if category(user) == 'army':
        cursor.execute(sqlarmy)
    elif category(user) == 'navy':
        cursor.execute(sqlnavy)
    elif category(user) == 'airforce':
        cursor.execute(sqlairforce)
    elif category(user) == 'armygeneral':
        cursor.execute(sqlarmygeneral)
    elif category(user) == 'navymarshal':
        cursor.execute(sqlnavymarshal)
    elif category(user) == 'airforcechief':
        cursor.execute(sqlairforcechief)
    elif category(user) == 'chiefcommander':
        cursor.execute(sqlchief)
message_collector(user,prev_time)
result = cursor.fetchall()

if result != ():
    for text in result:
        print("<" + str(text[1]) + "> : " + text[3] , end = '')

else:
    print("No previous messages") 

print("End of Previous Messages")

def chatlogger():
    file = open('chathistory.txt','w')
    oneweek = datetime.datetime.now() - datetime.timedelta(weeks=1)
    message_collector(user,oneweek.strftime("%Y-%m-%d %H:%M:%S"))
    result = cursor.fetchall()
    for text in result:
        file.write(str(text[4]) +  " <" + text[1] + "> : " + text[3] )
    file.close()

def upload_to_database(newmessage):
    sqlmessage = "INSERT INTO messages(user,belongsto,message) VALUES('%s','%s','%s')"%(user,category(user),newmessage)
    cursor.execute(sqlmessage)
    chats.commit()

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
            if message == "EXITCHAT\n":
                endedConnection = True
                continue
            if message == "PRINTCHAT\n":
                chatlogger()
                print("Successfully Saved Text. Check chathistory.txt")
                continue
            sys.stdout.write("<Me> : ")
            sys.stdout.write(message)
            sys.stdout.flush()
            upload_to_database(message)
            b = message.encode('utf-8')
            s.sendall(b)
    
    if endedConnection:
        break

s.close()

sql = "UPDATE lastlogin SET time = CURRENT_TIMESTAMP WHERE user = '%s'"%(user)

try:
    print("Updating Login Time. Bye!!!")
    cursor.execute(sql)
    chats.commit()
except:
    print("Couldnt Update Login")
    chats.rollback()

chats.close()