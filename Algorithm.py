import math

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
    
    empty_positions = available_squares(state)
    available_pieces_list = available_pieces(state)
    
    moves = []

    for pos in empty_positions:
        if len(available_pieces_list)== 0:
            moves.append((pos,None))
        
        else:
            for placing in available_pieces_list:
                    piece_place = ""
                    for i in placing:
                        piece_place += i 
                    moves.append((pos, piece_place))
        
    return moves 

def apply_move(state, move):
    '''Returns new state after applying move (position, piece_to_give)'''
    new_state = {
        "players": state["players"],
        "current": 1 - state["current"],  # Switch player
        "board": state["board"],
        "piece": move[1]  # The piece we're giving to opponent
    }
    # Place the current piece on the board
    new_state["board"][move[0]] = state["piece"]
    return new_state

        

def winning_line(line, board):
    pieces = [board[i] for i in line]
    for i in range(len(pieces)):
        if pieces[i] != None:
            pieces[i] = set(pieces[i])

    for i in pieces:
        if i == None:
            return False
        
    
    commun= set.intersection(*pieces)

    return len(commun) >= 1  # True if ≥1 shared trait


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


def negamax(state, depth, alpha, beta, color):
    """
    Negamax with Alpha-Beta pruning for Quarto.
    
    Args:
        state: Current game state (dict with 'board' and 'piece')
        depth: Search depth remaining
        alpha: Best score for maximizer
        beta: Best score for minimizer
        color: 1 (maximizing player) or -1 (minimizing)
        
    Returns:
        Best score for current player
    """
    # Base case: Terminal node or max depth reached
    if winning_board(state['board']) or depth == 0:
        return color * heuristic(state)
    
    best_score = -math.inf

    for move in generate_moves(state):
        # Apply the move and recurse
        new_state = apply_move(state, move)
        score = -negamax(new_state, depth-1, -beta, -alpha, -color)
        
        # Update best score and alpha
        best_score = max(best_score, score)
        alpha = max(alpha, score)
        
        # Alpha-beta pruning
        if alpha >= beta:
            break
    
    return best_score

def get_best_move(state, depth=3):
    """Wrapper to find the best move using Negamax"""
    best_score = -math.inf
    best_move = None
    
    print("ICI")
    for move in generate_moves(state):
        new_state = apply_move(state, move)
        score = -negamax(new_state, depth-1, -math.inf, math.inf, -1)
        
        if score > best_score:
            best_score = score
            best_move = move
    print(best_move)
    return best_move  # Returns (position, piece_to_give)


