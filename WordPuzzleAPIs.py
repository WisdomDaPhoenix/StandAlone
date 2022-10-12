from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def puzzleHome():
    return "Welcome to the Puzzle home page"

@app.route('/letters/',methods=['GET'])
def puzzleletters():
    endpt_pzletters = {'puzzle':
                        [{'id':0,
                        'name':'row zero',
                        'letters':['T','I','N','R','M','C','B']
                         },
                        {'id': 1,
                         'name': 'row one',
                         'letters':['A','C','P','S','C','T','R']
                         },
                        {'id':2,
                        'name':'row two',
                        'letters':['V','O','S','K','U','E','X']
                         },
                        {'id': 3,
                       'name': 'row three',
                       'letters': ['Z','L','A','M','N','W','F']
                        },
                        {'id': 4,
                         'name': 'row four',
                         'letters': ['W','U','P','D','G','Y','N']
                         },
                        {'id': 5,
                         'name': 'row five',
                         'letters': ['K','B','E','R','H','O','I']
                         },
                         {'id': 6,
                          'name': 'row six',
                          'letters': ['N','R','A','U','V','I','I']
                          },
                         {'id': 7,
                          'name': 'row seven',
                          'letters': ['Z','J','W','I','E','D','P']
                          },
                         {'id': 8,
                          'name': 'row eight',
                          'letters': ['C','B','A','B','I','A','P']
                          },
                         {'id': 9,
                          'name': 'row nine',
                          'letters': ['J','O','E','S','M','L','Q']
                          }
                         ]
                       }

    letters_json = jsonify(endpt_pzletters)
    return letters_json
print("Starting localhost on port 2500...")
app.run(port=2500)
