import socket, threading, sys                                                #Libraries import

if len(sys.argv) != 2: 
    print ("Correct usage: script, IP address, port number")
    exit() 
#IP_address = str(sys.argv[1]) 
Port = int(sys.argv[1])                                                         #Choosing unreserved port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              #socket initialization
server.bind(('', Port))                                               #binding host and port to socket
server.listen()

print("Running...")

clients = []
nicknames = []

def broadcast(message):                                                 #broadcast function declaration
    for client in clients:
        client.send(message)

def handle(client):                                         
    while True:
        try:                                                            #recieving valid messages from client
            message = client.recv(1024)
            broadcast(message)
        except:                                                         #removing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('UTF-8'))
            nicknames.remove(nickname)
            break

def receive():                                                          #accepting multiple clients
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address))) 
        client.send('NICKNAME'.encode('UTF-8'))
        nickname = client.recv(1024).decode('UTF-8')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname is {}".format(nickname))
        broadcast("{} joined! \n".format(nickname).encode('UTF-8'))
        client.send('Connected to server! \n'.encode('UTF-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()