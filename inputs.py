from random import randint

def random_moves(request:dict) -> dict :
    '''Inputs random move based on the state off the game, does not make BAD MOVES'''

    pos = None
    set_pieces = []
    List_pieces = ["BDEC", "BDEP", "BDFC", "BDFP", "BLEC", "BLEP", 
              "BLFC", "BLFP", "SDEC", "SDEP", "SDFC", "SDFP", 
                "SLEC", "SLEP", "SLFC", "SLFP"]
    
    for i in List_pieces:
        set_pieces.append(set(i))

    
    #removes pieces from the list[pieces] based on the state. Removes all the pieces who are already on the board
    for i in request["state"]["board"] :
        if i != None :
            for x in set_pieces:
                if x == set(i):
                    set_pieces.remove(set(x))

    
    #removes the pieces the player will be playing in this round. if the player starts and request["state"]["piece"] == None 
    #it make a TypeError so we pass
    try:
        if set(request["state"]["piece"]) in set_pieces:
            set_pieces.remove(set(request["state"]["piece"]))
    except TypeError:
        pass
    
    #makes a Random move
    while True:
        num = randint(0,15)

        if request["state"]["board"][num] == None:
            pos = num
            break

    #checks if pieces are still availabe for the opponent
    
    if len(set_pieces) == 0 :
        oppenent_piece = None

    else:
        oppenent_piece_set = set_pieces[randint(0,len(set_pieces)-1)]
        oppenent_piece = ""

        for i in oppenent_piece_set :
            oppenent_piece += i


    

    response = {
       "response": "move",
       "move": {"pos" : pos, "piece": oppenent_piece},
       "message": "Fun message"
    }

    return response

