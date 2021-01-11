#Create groups for football or Sports clubs
from random import shuffle
teams = ['Real madrid','Chelsea','Dynamo Kiev','AC Milan','Porto','Arsenal','Barcelona',
'Olympiakos','Manchester City','Dortmund','Zenith','Liverpool','Athletico Madrid',
'Tottenham','Inter Milan','Marseille','Athletico Bilbao','PSG','Shaktar Donetsk','Schalke 04',
'Salzburg','Fenebache','Wolves','Lyon']
groupings = []
shuffle(teams)
print(teams)
print('\n'*4)
for i in range(0,len(teams),4):
    groupings.append([teams[i],teams[i+1],teams[i+2],teams[i+3]])

print(groupings)
