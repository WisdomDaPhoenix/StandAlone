# BASIC SERVER
import socket
host = socket.gethostname()
port = 4041
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print("Listening...")
while True:
    newconn,address = s.accept()
    print("Connection established with client")
    print("Client socket details: {}".format(address))
    newconn.send(bytes("Sockets are very interesting!","utf-8"))
    newconn.close()