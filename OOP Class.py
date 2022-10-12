from books import Books
from copy import copy

class Wordplay():
    def __init__(self, wordlist):
        self.wordlist = wordlist

    def words_with_length(self,n):
        n_words = [word for word in self.wordlist if len(word) == n]
        print(f"Words with length {n}:  {n_words}")

    def starts_with(self,s):
        s_words = [word for word in self.wordlist if word.startswith(s) == True]
        print(f"Words starting with {s}: {s_words}")

    def ends_with(self,s):
        e_words = [word for word in self.wordlist if word.endswith(s) == True]
        print(f"Words ending with {s}: {e_words}")

    def palindromes(self):
        pal_words = [word for word in self.wordlist if word == word[ : :-1]]
        print(f"Palindromes: {pal_words}")

    def only(self,L):
        # CHECKS ALL LETTERS IN L
        L_words = []
        for item in L:
            for word in self.wordlist:
                if item in word:
                    L_words.append(word)
        print(f"{L} words: {list(set(L_words))}")


m = Wordplay(['hi','hello','welcome','go','mango'])
m.words_with_length(2)
m.starts_with('h')
m.ends_with('o')
m.only(['e','i','o'])




# CHECKS SINGLE LETTER IN L
        # letter = choice(L)
        # L_words = [word for word in self.wordlist
        #            if word.__contains__(letter) == True]
        # print(f"\"{letter}\" words: {L_words}")


input()



mystorybook = Books()
mystorybook.displayPageSize()

storybook2 = copy(mystorybook)
storybook2.title = "The Little Mermaid"
print(storybook2.title)

input()
class MyAndroid:
    def __init__(self, name, color, model, memory_size, phonenum):
        self.name = name
        self.color = color
        self.model = model
        self.memory_size = memory_size
        self.phonenum = phonenum

    def call(self):
        print(f'Calling {self.phonenum}...')

    def text(self):
        print(f'Sending message...to {self.phonenum}...')

    def deleteNumber(self):
        contacts.pop(contacts.index(self.phonenum))
        print(contacts)
        return "PhoneNumber deleted"

contacts = ['08138515927', '09017636418', '08147003870', '09015023264']
class Android:
    def __init__(self, name, color, model, memory_size):
        self.name = name
        self.color = color
        self.model = model
        self.memory_size = memory_size

    def call(self,s):
        print(f'Calling {s}...')

    def text(self,s):
        print(f'Sending message...to {s}...')

    def deleteNumber(self,s):
        contacts.pop(contacts.index(s))
        print(contacts)
        return "PhoneNumber deleted"


joshua = MyAndroid('Samsung','Blue','A12',64,'07087621155')
print(joshua.name)
joshua.gps = True
joshua.campixelsize = "12MP"
print(joshua.gps)
print(joshua.campixelsize)
input()




femi = MyAndroid('Tecno','Purple','Camon 12',8,'09027992420')
# print(femi.phonenum)
femi2 = MyAndroid('Tecno','Purple','Camon 12',8,'07031029304')
# print(femi2.phonenum)

danphone = Android('Samsung','White','A10',32)
danphone.call(femi.phonenum)
input()

# danphone = Android('Huawei','Phantom',4)








# infinix = Android('Gold', 'Hot 8', 4)

# infinix.call(contacts[0])
print('--------------------------------------------')
# infinix.text(contacts[1])
print('--------------------------------------------')
# print(infinix.deleteNumber(contacts[-1]))


input()


from random import choice

input()


class Books():
    def __init__(self):
        self.minpagesize = 2
        self.minchaptersize = 1

    def displayPageSize(self):
        print(f"Total number of pages in this book: {self.minpagesize} ")

    def displayChapterSize(self):
        print(f"Number of chapters in the book: {self.minchaptersize} ")


class Storybook(Books):
    def __init__(self,n):
        super().__init__()
        self.sheetsnum = 8
        self.n = n

    # OVERRIDING PARENT CLASS METHODS
    def displayPageSize(self):
        print(f"Total number of pages in this book: {self.minpagesize * self.sheetsnum} ")

    def displayChapterSize(self):
        print(f"Number of chapters in the book: {self.n * self.minchaptersize} ")

# STORYBOOK OBJECT
pirates = Storybook(3)

# ACCESS TO PARENT CLASS VARIABLES -  INHERITANCE
print(pirates.minpagesize) # Returns 2
print(pirates.minchaptersize) # Returns 1
pirates.displayPageSize()
pirates.displayChapterSize()



input()





class Fruit():
    pass


myfruit = Fruit()
print(type(myfruit))  # Fruit
print(isinstance(myfruit, Fruit))  # Returns True