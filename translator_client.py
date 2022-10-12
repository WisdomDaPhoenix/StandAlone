import socket
from translate import Translator
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",5557))
print("Socket created on 5557...")

while True:
    message = client.recv(1024).decode()
    dest = message[:message.index(':')]
    translator = Translator(from_lang='fr',to_lang=dest)
    actualmsg = message[3:]
    translation = translator.translate(actualmsg)
    print(translation) 





