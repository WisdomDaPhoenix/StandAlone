from flask import Flask, request, jsonify, json
import json
app = Flask(__name__)

@app.route('/',methods=['GET'])
def default_page():
    endpt_home = {'Page':'HomePage','Msg':'Successfully loaded homepage',
                  'HomeStatus':True}
    # json_home = json.dumps(endpt_home)
    json_home = jsonify(endpt_home)

    return json_home



@app.route('/userinfo/', methods=['GET'])
def request_page():
    username = str(request.args.get('user'))
    passdetails = str(request.args.get('password'))
    endpt_req = {'Page': 'RequestPage', 'Msg': f'Successfully loaded Request Page for {username}',
                'UserStatus': True, 'Username':username,'Password':passdetails}
    json_req = json.dumps(endpt_req)

    return json_req


@app.route('/games/', methods=['GET'])
def user_games():
    endpt_games = {"data":[
                       {'User':'Daniel',
                        'Age':32,
                        'Best Games':['Need4Speed','PES','MK','god of war']
                        },
                        {'User': 'Paul',
                        'Age': 25,
                        'Best Games': ['Devilmaycry', 'FIFA', 'PES', 'COD']
                        },
                        {'User': 'George',
                        'Age': 40,
                        'Best Games': ['Grand Theft', 'PES', 'Board chess',
                                       'Need4Speed']
                        }
                    ],
                    'statuscode':200}
    # json_games = json.dumps(endpt_games,indent=4)
    json_games = jsonify(endpt_games)

    return json_games


# @app.route('/games/', methods=['GET'])
# def user_edit():
#     newuser = str(request.args.get('newuser')) # /games/?newuser=
#     newage = str(request.args.get('age')) # /games/?age=
#     newbg = request.args.get('bg') # /games/?bg=
#
#     # /games/?newuser=korede&&age=23&&bg=['PES','Scrabble','Chess','MK']
#
#     endpt_games = {"data":[
#                        {'User':newuser,
#                         'Age':newage,
#                         'Best Games':newbg
#                         },
#                         {'User': 'Paul',
#                         'Age': 25,
#                         'Best Games': ['Devilmaycry', 'FIFA', 'PES', 'COD']
#                         },
#                         {'User': 'George',
#                         'Age': 40,
#                         'Best Games': ['Grand Theft', 'PES', 'Board chess',
#                                        'Need4Speed']
#                         }
#                     ],
#                     'statuscode':200}
#     json_games = json.dumps(endpt_games,indent=4)
#
#     return json_games

print("Starting localhost on port 4300...")
app.run(port=4300)














