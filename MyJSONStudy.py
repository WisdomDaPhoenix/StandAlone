import json
from pprint import pprint


# DOUBLE-LOADING AS FILE AND AS STRING
f = open("food.txt",encoding="utf-8").read()
myjson = f[f.index("{"):f.index("}")+1]
print(myjson)
print(type(myjson))
finaljson = json.loads(myjson)
print(f"{finaljson}\n\n{type(finaljson)}")









# WRITING A JSON OBJECT(DICT) TO A FILE USING THE DUMP METHOD

city = {}
city["coach"] = "Pep Guardiola"
city["trophies"] = 6
city["rivals"] = "Man United"
city["stats"] = {"Wins":10,"Losses":None}
city["players"] = ["Foden","De Bruyne","Cancelo"]

c = open("city.txt","w",encoding="utf-8")
json.dump(city,c,ensure_ascii=False)
myjson = json.dumps(city,ensure_ascii=False)
c.close()
print(myjson)
print(type(myjson))





# LOADING JSON JSON DATA FROM A FILE USING LOAD METHOD.
# NOTE: STRINGS IN DATA MUST ALWAYS BE IN DOUBLE-QUOTES

b = open("barca_file.txt","r",encoding="utf-8")
barcainfo = json.load(b)
b.close()
pprint(barcainfo)

input()


# LOADING JSON JSON DATA FROM A STRING USING LOADS METHOD
# NOTE: JSON DATA THAT IS LOADED MUST BE IN JAVASCRIPT FORMAT e.g true, false, and null values
# NOTE: STRINGS IN DATA MUST ALWAYS BE IN DOUBLE-QUOTES

club = """
{
    "name": "Barcelona",
    "president": "Laporta",
    "is_awesome": true,
    "trophies": 120,
    "players": ["De jong","Depay","Pique","Lewandoski"]
     }
 """
# print(type(club))  # Returns string
barca = json.loads(club)
pprint(barca)
# print(type(barca))