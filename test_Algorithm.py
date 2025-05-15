import Algorithm
state = {
  "players": ["LUR", "FKY"],
  "current": 0,
  "board": [
    None, None, None, None,
    "BDEC", "SDFC", None, None,
    None, None, None, None,
    "BLEP", None, "SLFC", None
  ],
  "piece": "SDEP"
   }

state2 = {
  "players": ["LUR", "FKY"],
  "current": 0,
  "board": [
    "SDEC", "SDEP", "SDFC", "SDFP", 
    None, None, None, None,
    None, None, None, None,
    None, None, None, None
  ],
  "piece": "BLEP"
}

state3 = {
  "players": ["LUR", "FKY"],
  "current": 0,
  "board": [
    "BDEC", "BDEP", "BDFC", "BDFP",
    "BLEC", "BLFC", "BLFP", "BLEP",
    "SDEC", "SDEP", "SDFC", "SDFP",
    "SLEC", "SLEP", "SLFC", None
  ],
  "piece": "SLFP"
}

state4 ={
  "players": ["LUR", "FKY"],
  "current": 0,
  "board": [
    "BDEC", "BDEP", "BDFC", None,
    "BLEC", "BLEP", "BLFC", "BLFP",
    "SDEC", "SDEP", "SDFC", "SDFP",
    None,     "SLEP", "SLFC", "SLFP"
  ],
  "piece": "SLEC"
}




def test_available_pieces():
    
    
    
    Dispo = [
  {"B", "D", "E", "P"},
  {"B", "D", "F", "C"},
  {"B", "D", "F", "P"},
  {"B", "L", "E", "C"},
  {"B", "L", "F", "C"},
  {"B", "L", "F", "P"},
  {"S", "D", "E", "C"},
  {"S", "D", "F", "P"},
  {"S", "L", "E", "C"},
  {"S", "L", "E", "P"},
  {"S", "L", "F", "P"}]
    for piece in Dispo:
        assert piece in Algorithm.available_pieces(state)





def test_available_squares():

    Cases = [0,1,2,3,6,7,8,9,10,11,13,15]

    for i in Cases:
        assert i in Algorithm.available_squares(state)




def test_generate_moves():
    
    assert Algorithm.generate_moves(state3) == [(15, None)]
    #Multiple etape car dans le code j utilise des ensemble mais pour le move je le retransforme
    #en string, donc c'est aleatoir l ordre des lettres et je ne peux pas comparer la list ou les tuples
    #directement
    assert Algorithm.generate_moves(state4)[0][0] == 3
    assert Algorithm.generate_moves(state4)[1][0] == 12
    assert set(Algorithm.generate_moves(state4)[0][1]) == set("BDFP")
    assert set(Algorithm.generate_moves(state4)[1][1]) == set("BDFP")



def test_apply_move():

    border =  [
    None, "SDEP", None, None,
    "BDEC", "SDFC", None, None,
    None, None, None, None,
    "BLEP", None, "SLFC", None
    ]

    new_state = {
        "players": ["LUR", "FKY"],
        "current": 1,  # Switch player
        "board": border,
        "piece": "SDEC"  # The piece we're giving to opponent
    }

    assert Algorithm.apply_move(state,(1, "SDEC")) == new_state



def test_winning_line():

    assert Algorithm.winning_line([0,1,2,3], state["board"]) == False

    assert  Algorithm.winning_line([4,5,6,7], state["board"]) == False

    assert  Algorithm.winning_line([0,1,2,3], state2["board"]) == True




def test_winning_board():
    
    assert Algorithm.winning_board(state["board"]) == False
    assert Algorithm.winning_board(state2["board"]) == True



def test_heuristic():
    
    assert Algorithm.heuristic(state2) == 100
    assert Algorithm.heuristic(state3) == 100
    assert Algorithm.heuristic(state) == 6



#def test_negamax():
#    pass
#
#
#def test_get_best_move():
#    pass
#
