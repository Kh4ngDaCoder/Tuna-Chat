
import socket, threading, os

os.system("title TunaChat")
os.system("cls")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization

IP_address = str(input("(Radmin/LAN) IP: ")) 
Port = int(input("PORT: ")) 

client.connect((IP_address, Port))                             #connecting client to server

os.system("cls")

print("Connect Successful!, Welcome To TunaChat!")
print("""
=========================================================================
=========================================================================
████████╗██╗   ██╗███╗   ██╗ █████╗      ██████╗██╗  ██╗ █████╗ ████████╗
╚══██╔══╝██║   ██║████╗  ██║██╔══██╗    ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
   ██║   ██║   ██║██╔██╗ ██║███████║    ██║     ███████║███████║   ██║   
   ██║   ██║   ██║██║╚██╗██║██╔══██║    ██║     ██╔══██║██╔══██║   ██║   
   ██║   ╚██████╔╝██║ ╚████║██║  ██║    ╚██████╗██║  ██║██║  ██║   ██║   
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
=========================================================================
                            LAN Chatroom made by gknguyen in python!
      """)
nickname = input("Choose your nickname: ")
print('\033[1A' + '\033[K', end= '\r')

def receive():
    while True:                                                 #making valid connection
        try:
            message = client.recv(1024).decode('UTF-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('UTF-8'))
            else:
                print(message)
        except:                                                 #case on wrong ip/port details
            print("An error occured!")
            client.close()
            break
def write():
    while True:                                                 #message layout
        messagecontent = input('')
        print('\033[1A' + '\033[K', end= '\r')
        message = '{}: {}'.format(nickname, messagecontent)
        client.send(message.encode("UTF-8"))
        

receive_thread = threading.Thread(target=receive)               #receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write)                   #sending messages 
write_thread.start()