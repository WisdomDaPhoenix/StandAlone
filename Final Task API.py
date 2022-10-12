# TASK - STATES AND LGAS

from flask import Flask
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homeCities():
    country = {"name":"Nigeria"}
    return f"Homepage for cities and LGAs in {country['name']}"


@app.route('/cities/', methods=['GET'])
def showCities():
    endpt_cities = {"data":[
    {"state": "Cross River",
     "zip code": 540001,
     "LGAs":['Ikom', 'Obudu']
     },
    {"state": "FCT",
      "zip code": 900001,
     "LGAs": ['Kuje', 'Bwari']
    },
    {"state": "Kano",
     "zip code": 800001,
     "LGAs": ['Garko', 'Dala']
     },
    {"state": "Lagos",
     "zip code": 100001,
     "LGAs": ['Ojo', 'Badagry']
    },
    {"state": "Plateau",
     "zip code": 930001,
     "LGAs": ['Wasa', 'Shendam']
    },
    {"state": "Rivers",
     "zip code": 500001,
     "LGAs": ['Eleme', 'Andoni']
     }
    ]}
    # Omitted line
    # Omitted line

app.run()

# QUESTIONS

# Complete the program(Omitted lines) and generate a cities
# JSON Object on port 3000

# Generate a dictionary using a program whose contents will be states
# and their zip codes

# For every state in our JSON OBJECT, output a sorted list of its LGAs. Your
# output should be a dictionary



