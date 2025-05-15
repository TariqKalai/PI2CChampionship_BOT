

lines = [
    #Horiziontal
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15],
    
    #Vertical
    [0,4,8,12],
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    
    #Diagonal
    [0,5,10,15],
    [2,6,8,12],
]


def available_pieces(state)-> list:
    '''Checks available pieces inputs must be the state of the play'''
    
    set_pieces = []
    List_pieces = ["BDEC", "BDEP", "BDFC", "BDFP", "BLEC", "BLEP", 
              "BLFC", "BLFP", "SDEC", "SDEP", "SDFC", "SDFP", 
                "SLEC", "SLEP", "SLFC", "SLFP"]
    
    for i in List_pieces:
        set_pieces.append(set(i))

    
    #removes pieces from the list[pieces] based on the state. Removes all the pieces who are already on the board
    for i in state["board"] :
        if i != None :
            for x in set_pieces:
                if x == set(i):
                    set_pieces.remove(set(x))

    #removes the pieces the player will be playing in this round. if the player starts and request["state"]["piece"] == None 
    #it make a TypeError so we pass
    try:
        if set(state["piece"]) in set_pieces:
            set_pieces.remove(set(state["piece"]))
    except TypeError:
        pass
    return set_pieces

def available_squares(state):

    Nonelist = []
    for i in range(16):
        if state["board"][i] == None :

            Nonelist.append(i)

    return Nonelist


def generate_moves(state):

    board = state["board"]
    piece_to_place = state["piece"]
    
    empty_positions = available_squares(board)
    available_pieces_list = available_pieces(board)
    
    moves = []

    for pos in empty_positions:
        for placing in available_pieces_list:
                moves.append((pos, placing))
    
    return moves 

        

def winning_line(line, board):
    pieces = [board[i] for i in line]

    for i in pieces:
        if i == None:
            return False
    
    for charcteristic in range(4):

        commun = [p[charcteristic] for p in pieces]
        if all(t == commun[0] for t in commun):
            return True
    return False


def winning_board(board):
    
    for line in lines :
        if winning_line(line, board) == True:
            return True
        
    return False
   
   # return any(is_winning_line(line, board) for line in WINNING_LINES)

def heuristic(state):

    
    board = state["board"]
    if winning_board(board):
        return 100  # strong win

    score = 0
    for line in lines:
        pieces = [board[i] for i in line if board[i] is not None]
        if len(pieces) == 3:
            # * unpack les elements pour donner 3 set separé
            common = set.intersection(*(set(p) for p in pieces))
            if len(common) >= 1:
                score += 10  # 3 pieces affilé attention presque victoire

        elif len(pieces) == 2:
            common = set.intersection(*(set(p) for p in pieces))

            if len(common) >= 2:
                score += 3  # possible setup

    return score


thing = {
  "players": ["LUR", "FKY"],
  "current": 0,
  "board": [
    None,
    "BDEC",
    None,
    "SDFP",
    None,
    None,
    None,
    None,
    None,
    "SLFC",
    None,
    None,
    "BLFP",
    "BLEC",
    None,
    None
  ], 
  "piece": "BLEP"
}

            
