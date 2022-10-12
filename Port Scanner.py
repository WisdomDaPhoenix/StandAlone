# print(socket.gethostbyname('www.invoice.ng'))
# print(socket.gethostbyname('www.bing.com'))
# print(socket.gethostname())
# print(socket.gethostbyaddr('204.79.197.200'))
# input()

import socket
import sys

try:
    for port in range(21,60):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex(('www.invoice.ng',port))
        if result == 0:
            print("Port  {}:\t Open".format(port))
        else:
            print("Port  {}:\t Closed".format(port))
        sock.close()
except socket.error as se:
    print("Could not establish a connection! "+str(se))
    sys.exit()


