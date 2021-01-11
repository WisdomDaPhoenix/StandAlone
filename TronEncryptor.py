# Create Dictionary with each letter representing a string of alphanumerics
# Make string text using letter's values with each letter of the intended word as key
from string import punctuation
basic_dic = {'a': 'pf1w','b': 'a2qu','c': 'ty3s','d': 'ze4h','e': 'o5lv','f': 'ix6n','g': 'nb7m',
         'h': 'q8jr','i': 'kc9d','j': 'pt10','k': 'g11x','l': '12if','m': 'ns13','n': 'l14z',
             'o': 'ym15','p': '16ku','q': 'x17v','r': 'en18','s': 'i19y','t': '20gt',
             'u': 'lj21','v': 'br22','w': 'h23m','x': '24sj','y': 'wk25','z': 'uh26', ' ': ' '}

message = input('Enter your message here: ')
for c in punctuation:
    message = message.replace(c,'')
message = message.lower()
g = list(message)
t = [basic_dic[m] for m in g]
tron = ''.join(t)
f = open('tronmessage.txt','w')
print('Tron hidden message says: \n',
      tron, file=f)

f.close()
print("You hidden message contents are in the file named \'tronmessage.txt\'")