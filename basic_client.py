# BASIC CLIENT
# greeting = "Hi"
# print(f"{greeting}")
# print(type(greeting))  # Returns str
# print('-----------------------------------------')
# encoded = greeting.encode()
# print(type(encoded))
# input()
#
# print('------------------------------------')
# print(bytes(greeting,"utf-8"))  # Encoding Hi string
# print(type(bytes(greeting,"utf-8")))  # Returns bytes
# print(len(bytes("","utf-8")))  # Encoding an empty string

import socket
host = socket.gethostname()
port = 4041
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
# msg = s.recv(1024)
# print(msg.decode("utf-8"))
full_msg = ""
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        print("No message")
        break
    full_msg = full_msg + msg.decode("utf-8")
print(full_msg)


