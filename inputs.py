from random import randint

def random_moves(request:dict) -> dict :
    '''Inputs random move based on the state off the game, does not make BAD MOVES'''

    pos = None
    pieces = ["BDEC", "BDEP", "BDFC", "BDFP", "BLEC", "BLEP", 
              "BLFC", "BLFP", "SDEC", "SDEP", "SDFC", "SDFP", 
                "SLEC", "SLEP", "SLFC", "SLFP"]
    
    #removes pieces from the list[pieces] based on the state. Removes all the pieces who are already on the board
    for i in request["state"]["board"] :
        if i != None :
            for x in pieces:
                if all(elements in x for elements in i[:4]):
                    pieces.remove(x)

    #removes the pieces the player will be playing in this round.
    if request["state"]["piece"] in pieces:
        pieces.remove(request["state"]["piece"])
    
    #makes a Random move
    while True:
        num = randint(0,15)

        if request["state"]["board"][num] == None:
            pos = num
            break

    #checks if pieces are still availabe for the opponent
    
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
