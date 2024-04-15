from board import create_empty_board, set_player, get_player, is_occupied
from constants import PLAYER_O, PLAYER_X
from test_game import game

board_state = int(1)
current_player = str(PLAYER_X)
winner = None


    
                       


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
#    print("der nächste spieler ist", current_player)
    return current_player

#current_player = next_player(current_player)

################################## input row and column #############################



def input_row():
    try_input = True
    input_row = ''
    while try_input:
        input_try_row = input("please enter a row between 1 and 3:")
        if input_try_row.isdigit():
            input_try_row = int(input_try_row)
            if 0 < input_try_row < 4:
                input_row = input_try_row
                try_input = False
            else:
                print("ups! your number is not in the range 1 to 3, please try Again ->")
        else:
            print("ups! something went wrong, please try Again ->")
    return input_row


def input_column():
    try_input = True
    input_column = ''
    while try_input:
        input_try_column = input("please enter a column between 1 and 3:")
        if input_try_column.isdigit():
            input_try_column = int(input_try_column)
            if 0 < input_try_column < 4:
                input_column = input_try_column
                try_input = False
            else:
                print("ups! your number is not in the range 1 to 3, please try Again ->")
        else:
            print("ups! something went wrong, please try Again ->")
    return input_column            

################################## check for victory #############################


def check_victory(board_state):
    winner = None
    continue_check_row = True
    continue_check_column = True
    continue_check_diagonals = True
    horizontal_checking_row = 1
    horizontal_checking_column = 1
    vertical_checking_row = 1
    vertical_checking_column = 1
    player_in_cell = "irgendwas is falsch"

    
#------------------------------------------------------checking if there is a victory in the rows
    
    while continue_check_row:
        row_in_sequence = 0
        check_this_row = True
        player_in_cell = None
#        print("while continue_check_row")
        while check_this_row:
            #check if there is a player marker in the cell
#            print("while check_this_row")
#            print(horizontal_checking_row, horizontal_checking_column)
#            print(get_player(board_state, horizontal_checking_row, horizontal_checking_column))
            if get_player(board_state, horizontal_checking_row, horizontal_checking_column):
                #check if player is the same as in the cell before that
#                print("check if player is the same as in the cell before")
                if horizontal_checking_column == 1:
                    #if the first column is checked, cheange the player_in_cell to the player
                    player_in_cell = get_player(board_state, horizontal_checking_row, horizontal_checking_column)
                    
                if player_in_cell == get_player(board_state, horizontal_checking_row, horizontal_checking_column):
                    # if its the same Player add to the counter
                    row_in_sequence = row_in_sequence +1
                    horizontal_checking_column = horizontal_checking_column +1
#                    print("player is the same as in the former cell, sequence counter", row_in_sequence)
#                    print("player in cell:", player_in_cell)
                else:
                    if horizontal_checking_row < 3:
                        horizontal_checking_row = horizontal_checking_row + 1
                        horizontal_checking_column = 1
                        row_in_sequence = 0
                        player_in_cell = None
#                        print("player not the same as in the cell before, restarting in next row")
                    else: #if there is no win in the last cell:
                        player_in_cell = None
                        check_this_row = False
#                        print("no win in the last row either :(")
                    
                    

                # if the row_in_sequence counter is at 3 the player is the winner
                if row_in_sequence == 3:
                    winner = player_in_cell
#                    print("if row in sequence is 3 player in cell is winner")
                    check_this_row = False
#                    print("the winner is :", winner)
                    
            #pass this row if there is no player marker in the cell
            
            else:
                horizontal_checking_row = horizontal_checking_row + 1
#                print("there was no player in that cell, skip to next row")
                
            
            # end while loop if all cells are checked (row 3 and column 3 are checked)
            
            if horizontal_checking_row > 3:
                check_this_row = False
                
#            print("horizontal_checking_row :" , horizontal_checking_row)
#            print("winner:" ,winner)
#            print("ende der schleife check_this_row#")
        continue_check_row = False
    
#----------------------------------------------------- checking if there is a victory in the columns
    
    if winner == None:
#        print("2")
        while continue_check_column:
                column_in_sequence = 0
                check_this_column = True
                player_in_cell = None
#                print("while continue_check_column")
                while check_this_column:
#                    print("vertical_checking_column :" , vertical_checking_column)
#                    print("vertical_checking_row :" , vertical_checking_row)
#                    print("column_in_sequence:", column_in_sequence)
#                    print("ende der schleife check_this_column")
#                    print("+++++++++++++++++++++++++++++++++++++")
                    #check if there is a player marker in the cell
                    if get_player(board_state, vertical_checking_row, vertical_checking_column):
                        #check if player is the same as in the cell before that
                        if vertical_checking_row == 1:
                            #if the first column is checked, cheange the player_in_cell to the player
                            player_in_cell = get_player(board_state, vertical_checking_row, vertical_checking_column)

                            
                        if player_in_cell == get_player(board_state, vertical_checking_row, vertical_checking_column):
                            # if its the same Player add to the counter
                            column_in_sequence = column_in_sequence +1
                            vertical_checking_row = vertical_checking_row +1
                        else:
                            if vertical_checking_column < 4:    ###########################################siehe shellscript in skirbbles#################
                                vertical_checking_column = vertical_checking_column + 1
                                vertical_checking_row = 1
                                column_in_sequence = 0
                                player_in_cell = None
                            elif vertical_checking_column > 3: #if there is no win in the last cell:
                                player_in_cell = None
                                check_this_column = False
#                                print("no win in the last row either :(")
                            
                            

                        # if the row_in_sequence counter is at 3 the player is the winner
                        if column_in_sequence == 3:
                            winner = player_in_cell
#                            print("if row in sequence is 3 player in cell is winner")
                            check_this_column = False                        
#                            print("the winner is :", winner)
                            
                    #pass this row if there is no player marker in the cell
                    
                    else:
                        vertical_checking_column = vertical_checking_column + 1
                        vertical_checking_row = 1
                        column_in_sequence = 0
#                        print("there was no player in that cell, skip to next column")
                        
                    
                    # end while loop if all cells are checked (row 3 and column 3 are checked)
                    
                    if vertical_checking_column > 3:
                        check_this_column = False
                        
#                    print("vertical_checking_column :" , vertical_checking_column)
#                    print("vertical_checking_row :" , vertical_checking_row)
#                    print("winner:" ,winner)
#                    print("column_in_sequence:", column_in_sequence)
#                    print("ende der schleife check_this_column")
#                    print("-----------------------------------")
                continue_check_column = False


#------------------------------------------------------checking if there is a victory in the diagonals

    
    if winner == None:
        player_in_cell = None
        if get_player(board_state, 1,1):
            player_in_cell = get_player(board_state,1,1)
            if get_player(board_state,2,2) == player_in_cell:
                if get_player(board_state,3,3) == player_in_cell:
                    winner = player_in_cell
                    
        if get_player(board_state,3,1):
            player_in_cell = get_player(board_state,3,1)
            if get_player(board_state,2,2) == player_in_cell:
                if get_player(board_state,1,3) == player_in_cell:
                    if winner:
                        winner = "draw"
                    else:
                        winner = player_in_cell
                    
            
                        
#-------------------------------------------------------check if there is a draw
    
    if not winner:
        check_for_occupancy = True
        check_for_occupancy_row = 1
        check_for_occupancy_column = 1
        occupied_cells = 0
        
        while check_for_occupancy:
            
            #print("column:",check_for_occupancy_column)
            #print("row:", check_for_occupancy_row)
            if get_player(board_state, check_for_occupancy_row, check_for_occupancy_column ):
                occupied_cells = occupied_cells + 1
                
            check_for_occupancy_column = check_for_occupancy_column +1    
                
                
                
            if  occupied_cells == 9:   
                winner = "draw"
                
            if check_for_occupancy_column == 4:
                check_for_occupancy_column = 1
                
                check_for_occupancy_row = check_for_occupancy_row +1
                if check_for_occupancy_row == 4:
                    check_for_occupancy = False



               
    return winner

#------------------------------------------------game

def game():
    game_constants = True
    
    while game_constants: # keep constans and restart game after finish
        game_on = True
        board_state = create_empty_board()
        print_board(board_state)
        player_X = input("please put in the Name of the first player:")
        player_0 = input("please put in the Name of the second player:")
        current_player = str(PLAYER_X)
        winner = None
        while game_on :
            if not winner:
                current_player = next_player(current_player)
                
                player = None
                if current_player == PLAYER_X :
                    player = player_0
                else:
                    player = player_X

                print("it's ", player, "'s turn:")
                selecting = True
                while selecting:
                    selected_row = input_row()
                    print("selected row:", selected_row)
                    selected_column = input_column()
                    print("selected column", selected_column)
                    if not is_occupied(board_state, selected_row, selected_column):
                        set_row = selected_row
                        set_column = selected_column
                        selecting = False
                    else:
                        print("that cell is occupied, please select another one ->")
                board_state = set_player(board_state, set_row, set_column, current_player)
                print_board(board_state)
                winner = check_victory(board_state)

            if winner == "draw":
                print("es ist ein unentschieden")
                game_on = False
                
            if winner == PLAYER_X or winner == PLAYER_O:
                print(winner)
                player_winner = ""
                if winner == PLAYER_X :
                    player_winner = "Second player:"
                elif winner == PLAYER_O:
                    player_winner = "First player:"
                print("gewonnen hat:", player_winner)
                game_on = False
                        
        
        continue_game = input("Do you want to start a new game ? Y/N")
        if continue_game == "N" or continue_game == "n":
            game_constants = False





