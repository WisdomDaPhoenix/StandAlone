
import socket
dest = input("Please enter the destination language: ")
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",5557))
server.listen(5)
print("Listening now...")
client_conn, address = server.accept()
print("Connection established from {}".format(address))

while True:
    newmsg = input("Enter some text to translate: ")
    if newmsg == "" or newmsg == 'q':
        print("Quitting program...")
        client_conn.close()
        break
    client_conn.send(f"{dest}:{newmsg}".encode())


    # client_conn.send(f"{dest}:We are in the class right now".encode())
