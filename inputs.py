from random import randint

def random_moves(request:dict) -> dict :
    pos = None

    pieces = ["BDEC", "BDEP", "BDFC", "BDFP", "BLEC", "BLEP", 
              "BLFC", "BLFP", "SDEC", "SDEP", "SDFC", "SDFP", 
                "SLEC", "SLEP", "SLFC", "SLFP"]
    for i in request["state"]["board"] :
        if i != None :
            for x in pieces:
                if all(elements in x for elements in i[:4]):
                    pieces.remove(x)
    if request["state"]["piece"] in pieces:
        pieces.remove(request["state"]["piece"])
    while True:
        num = randint(0,15)

        if request["state"]["board"][num] == None:
            pos = num
            break
    if len(pieces) == 0 :
        oppenent_piece = None

    else:
        oppenent_piece = pieces[randint(0,len(pieces)-1)]

    

    response = {
       "response": "move",
       "move": {"pos" : pos, "piece": oppenent_piece},
       "message": "Fun message"
    }

    return response

request = {'request': 'play', 'lives': 1, 
 'errors': "ucu", 
'state': {'players': ['LOCALHOST', 'KALTAR'], 'current': 0, 
          'board': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 'piece': None}} 

print(random_moves(request))