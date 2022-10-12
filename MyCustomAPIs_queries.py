import requests
import json
from pprint import pprint

response = requests.get('http://127.0.0.1:2500/letters/')
# response = requests.get('https://c6f9-102-89-22-192.eu.ngrok.io/letters/')
mydata = response.json()
evens_sequences = []
odd_sequences = []
for i in range(len(mydata['puzzle'])):
    if i % 2 == 0:
        evens_sequences.append(mydata['puzzle'][i]['letters'])
    else:
        odd_sequences.append(mydata['puzzle'][i]['letters'])


lines_even = [' '.join(item) for item in evens_sequences]
lines_odd = [' '.join(item) for item in odd_sequences]
# # print(lines_even)
# # print(lines_odd)
puzzle1 = "\n".join(lines_even)
puzzle2 = "\n".join(lines_odd)
# print("------------------Puzzle One---------------")
# print(puzzle1)
print("------------------Puzzle Two---------------")
print(puzzle2)

# print(mydata['puzzle'][0]['letters'])



# response = requests.get('http://127.0.0.1:5000/userinfo/?user=Demi&&password=bigboy')
# mydata = response.json()
# print(mydata['Password'])
# print(mydata['Page'])
# # pprint(mydata)

# GET IN ACTION
# response = requests.get('http://127.0.0.1:4300/games/')
# response = requests.get('https://7d94-102-89-22-192.eu.ngrok.io/games/')
# gamesdata = response.json()
# for games in gamesdata["data"][1]["Best Games"]:
# #     print(games)
#
# print(gamesdata['data'][0]['User'])  # Daniel
# print(gamesdata['data'][1]['User'])  # Paul
# print(gamesdata['data'][0]['Age'])
# print(gamesdata['data'][1]['Age'])
# print(gamesdata['data'][2]['Best Games'][0])

