from board import create_empty_board, set_player, get_player, is_occupied
from constants import PLAYER_O, PLAYER_X

board_state = int(1)
current_player = str(PLAYER_X)
winner = None

board_state = set_player(1,1,1,PLAYER_O )
    
                       


################################### Plot Board ######################################        
  
def board_pos(board_state):
    pos_1 = get_player(board_state,1,1)
    pos_2 = get_player(board_state,1,2)
    pos_3 = get_player(board_state,1,3)
    pos_4 = get_player(board_state,2,1)
    pos_5 = get_player(board_state,2,2)
    pos_6 = get_player(board_state,2,3)
    pos_7 = get_player(board_state,3,1)
    pos_8 = get_player(board_state,3,2)
    pos_9 = get_player(board_state,3,3)

    return [pos_1,pos_2,pos_3,pos_4,pos_5,pos_6,pos_7,pos_8,pos_9]
# returns the player which sits on which cell as a list


def print_board(board_state):
    board_positionen= board_pos(board_state)

    for i in range(len(board_positionen)):
        if board_positionen[i] == None:
            board_positionen[i] = " "

    print( board_positionen[0], "|"  ,board_positionen[1],"|", board_positionen[2])
    print("--+---+---")
    print( board_positionen[3], "|"  ,board_positionen[4],"|", board_positionen[5])
    print("--+---+---")
    print( board_positionen[6], "|"  ,board_positionen[7],"|", board_positionen[8])
# plots the board state


################################### switch Player ###################################

def next_player(current_player):
    
    if current_player == PLAYER_O:
        current_player = PLAYER_X
    else:
        current_player = PLAYER_O
    print("der nächste spieler ist", current_player)
    return current_player

current_player = next_player(current_player)


