# JUMIA SERVER COMMUNICATION AND RESPONSE
import socket
target_host = '104.16.206.107'
target_port = 80
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target_host,target_port))
query = bytes("buy shoes","utf-8")
s.send(query)
data = s.recv(8192)
print(data)          # Encoded response
print("Data: ",data.decode("utf-8"))  # Decoded response
print(len(data))  # Length of encoded response
print('Closing socket...')
s.close()
print('Socket closed!')

# BASIC SERVER
# import socket
# host = socket.gethostname()
# port = 4040
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((host,port))
# s.listen(4)
# print("Listening...")
# while True:   # While incoming connection from the client
#     myconn,addr = s.accept()  # Accept connection object and client's socket info
#     print("Connection established from address {}".format(addr))
#     myconn.send(bytes("Sockets are interesting!","utf-8"))
#     myconn.close()
"""
# BASIC CLIENT
import socket
host = socket.gethostname()
port = 4040
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
full_msg = ""
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        print("No message sent")
        break
    else:
        full_msg = full_msg + msg.decode("utf-8")
print(full_msg)




input()


# print(type("Hi"))
# print(type(bytes("Hi","utf-8")))  # Encoding the Hi string
# print(type(bytes("","utf-8")))    # Encoding an empty string
# print(type(bytes("Hi","utf-8").decode("utf-8"))) # Decoded string

# input()















# BASIC SERVER

# import socket
# host = socket.gethostname()
# port = 4040
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((host,port))
# s.listen(5)
# while True:
#     conn,addr = s.accept()
#     print("Connection established with client")
#     print("Client details: {}".format(addr))
#     conn.send(bytes("Sockets are very interesting!","utf-8"))
#     s.close()

# BASIC CLIENT
# import socket
# host = socket.gethostname()
# port = 4040
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((host,port))
# msg = s.recv(1024)
# print(msg.decode("utf-8"))



"""
