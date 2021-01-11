# This is the decryptor program
# From a file, pass string into class with a decrypt method
# Decrypt method extracts each integer value per word, creates a list and converts to string message
tron = open('tronmessage.txt').read()
T = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = []
class Tronix:
    def __init__(self, t):
        self.t = t
    def decryptor(self):
        numstring = ''

        for i in range(0,len(self.t)-1):
            if self.t[i].isdigit() and self.t[i+1].isdigit():
                numstring = self.t[i] + self.t[i+1]
                n.append(numstring)
            elif self.t[i-1].isalpha() and self.t[i].isdigit() and self.t[i+1].isalpha():
                n.append(self.t[i])

        t_words = [int(x)-1 for x in n]
        # print(t_words)
        hidden_message = [T[i] for i in t_words]
        hidden_message = ''.join(hidden_message)
        hidden_message = hidden_message[0].upper() + hidden_message[1:]
        return hidden_message

w = Tronix(tron)
g = open('decryptedmessage.txt','w')
print(w.decryptor(), file=g)
g.close()
print("You decrypted or hidden message contents are in the file named \'decryptedmessage.txt\'")
















