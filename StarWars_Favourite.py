voters = open("VotersLIST.txt").read()
voter = input("Hello voter! Please enter your full name to vote: ")
if voter in voters:
    print("You have already voted. Thanks see you next time! ")
else:
    import requests

    url = "https://swapi.dev/api/people"
    response = requests.get(url)
    charlist = response.json()
    char = []
    print("'''''''List of all Star Wars Characters''''''''''''''\n")
    m = 0
    for i in range(0, len(charlist["results"])):
        name = charlist["results"][i]["name"]
        char.append(name)
        m = m + 1

        print("\t\t\t", m, char[i])

    dic_char = {item: char.index(item) + 1 for item in char}
    x = (list(dic_char.values()))
    votecount = 0


    vote = eval(input("Vote your favourite Star Wars character, use serial - (4 for Darth Vader): "))

    if isinstance(vote, int) and vote in x:
        votecount = votecount + 1
        myvote = [key for key in dic_char if dic_char[key] == vote]
        myvote = ''.join(myvote)
        print("You have voted for", myvote)
        print("Voting completed")
        newline = voter + "\t" + myvote + " \n"
        with open("VotersLIST.txt",'a') as f:
            f.write("\n")
            f.write(newline)
        f.close()










