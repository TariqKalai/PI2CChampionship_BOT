from random import randint
import json

def avaiblable_pieces(request:dict)-> list:
    
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

    return set_pieces


def random_moves(request:dict) -> dict :
    '''Inputs random move based on the state off the game, does not make BAD MOVES'''

    set_pieces = avaiblable_pieces(request)
    
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


def tought_moves(request:dict)-> dict :
    #set_pieces = avaiblable_pieces(request)

    #Mathematical formulas wich converts from a list index to a grid style board
    #columns = index % 4
    #rows = index //4
    #index = rows*4 +columns

    Board = request["state"]["board"]
#   a modifier 
    for index in range(len(Board)) :
        if Board[index] != None :
            print(index)
            size = 3
            columns = index % size
            rows = index //size
            for letter in Board[index] : 
                try:
                    for y in range(rows-1, rows+2):
                        for x in range(columns-1, columns+2):
                            print( f"x : {x}    y : {y}   index = {y*size+x}")
                            

                except IndexError:
            
                    pass




def check_around(Board : list):
    positions_dico = {}
    for index in range(len(Board)) :
        if Board[index] != None :
            
            for letter in Board[index]:
                try:
                    positions_dico[letter].add(index)
                except KeyError:
                    positions_dico[letter] = set()
                    positions_dico[letter].add(index)
                    pass
            
            for key in positions_dico:
                for result in key :
                    index_list = []
                    essay_row = 0
                    essay_columns=0
                    essay_diagonal = 0
                    rand_index = positions_dico[result].pop()
                    positions_dico[result].add(rand_index)
                    row_value = int(rand_index)//4
                    columns_value = int(rand_index)%4
                    for result_2 in positions_dico[result] :
                        position = int(result_2)
                        if position//4 == row_value:
                            
                            essay_row +=1
                        if position % 4 == columns_value:
                            essay_columns +=1
                        if position//4 == row_value+1 or position//4 == row_value+2:
                            if position%4 == columns_value+1 or position%4 == columns_value+2:
                                essay_diagonal +=1
                    
                    if essay_columns == 3 :

                        print("Triples", key, "vertical")
                    if essay_diagonal ==3 :

                        print("Triples", key, "horizontal")

                    if essay_row == 3 : 

                        print("Triples", key, "diagonal")

                    

    return positions_dico


List_pieces = [ "BLEP", "BLFC", "BLFP", "SDEC",  "SDFP", 
                "SLEC", "SLEP", "SLFC", "SLFP"]
lister = ["BDEC", "SDEP", "SDFC", None, "BDFP", None, None, None, "BLEC", None, None, None ,None, None, None, None] 

check_around(lister)