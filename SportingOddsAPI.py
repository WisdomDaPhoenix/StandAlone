import requests
from pprint import pprint


# url = "https://api.the-odds-api.com/v4/sports/?apiKey"
url = "https://api.the-odds-api.com/v4/sports/soccer_uefa_champs_league/odds/?apiKey=a6c2dadc264866ec2843d61fcdc6b302&regions=eu"
response = requests.get(url)
print(response.status_code)
full = response.json()
# pprint(full[0])
bookmakers_names = [full[0]['bookmakers'][i]['title'] for i in range(len(full[0]['bookmakers']))]
# print(bookmakers_names)
allcityodds = [full[0]['bookmakers'][i]['markets'][0]['outcomes'] for i in range(len(full[0]['bookmakers']))]
# print(allcityodds)

bmplusodds = list(zip(bookmakers_names,allcityodds))
# pprint(bmplusodds)
# print(len(bmplusodds))



just_odds = [x[1] for x in bmplusodds]
# pprint(just_odds)
cop_odds = []
city_odds = []
for i in range(len(just_odds)):
    for j in range(len(just_odds[i])):
        if just_odds[i][j]['name'] == "Manchester City":
            city_odds.append(just_odds[i][j]['price'])
        elif just_odds[i][j]['name'] == "FC Copenhagen":
            cop_odds.append(just_odds[i][j]['price'])

# print(cop_odds)
# print(city_odds)
bmfinal = {bookmakers_names[i] : [cop_odds[i],city_odds[i]] for i in range(len(bookmakers_names))}
# print(bmfinal)
highestbms_cop = [(key,bmfinal[key][0]) for key in bmfinal]
highestbms_city = [(key,bmfinal[key][1]) for key in bmfinal]
dicthbcop = dict(highestbms_cop)
dicthbcity = dict(highestbms_city)

finalcop = dict(sorted(dicthbcop.items(),key=lambda item: item[1]))
lfcop = list(finalcop.items())
finalcity = dict(sorted(dicthbcity.items(),key=lambda item: item[1]))
lfcity = list(finalcity.items())

top3bms_cop = lfcop[-3:]
top3bms_cop.sort()

top3bms_city = lfcity[-3:]
top3bms_city.sort()
print("Top 3 bookmakers and Odds for Manchester City")
for (x,y) in top3bms_city:
    print("Bookmaker: ",x, '  -----------   ',"Odds: ",y)


print('-----------------------------------------------------')

print("Top 3 bookmakers and Odds for FC Copenhagen")
for (m,n) in top3bms_cop:
    print("Bookmaker: ",m, '  -----------   ',"Odds: ",n)







