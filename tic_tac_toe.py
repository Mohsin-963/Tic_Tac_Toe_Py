# Display the board
def display_board(board):
    clear_output()
    print('_________')
    for i in range(0,9,3):
        print(board[i+1],'|',board[i+2],'|',board[i+3])
    print("---------")
    pass

# Take player position
def p_position(board, p):
    choice = False
    while choice == False:
        c = input(p+" Choose a location (1 - 9):")
        if c.isdigit():
            c = int(c)
            if c >0 and c <10:
                if board[c]==' ' :
                    choice = True
                    pc = c
                else:
                    print("This Place is not empty! Choose an other.")
            else :
                print("Invalid! Position should be between(1-9)")
        else :
            print('Invalid Choice! Try again')
    return pc

# Function:
def place_marker(board,marker,location):
        board[location] = marker

# Win Check
def win_check(board,mark):
    if board[1]==board[2]==board[3]==mark:
        print(mark,' Wins')
        return True
    elif board[4]==board[5]==board[6]==mark:
        print(mark,' Wins')
        return True
    elif board[7]==board[8]==board[9]==mark:
        print(mark,' Wins')
        return True
    
    elif board[1]==board[4]==board[7]==mark:
        print(mark,' Wins')
        return True
    elif board[2]==board[5]==board[8]==mark:
        print(mark,' Wins')
        return True
    elif board[3]==board[6]==board[9]==mark:
        print(mark,' Wins')
        return True
    
    elif board[1]==board[5]==board[9]==mark:
        print(mark,' Wins')
        return True
    elif board[3]==board[5]==board[7]==mark:
        print(mark,' Wins')
        return True
    else:
        return False
        

# Board FUll
def board_full(board):
    for i in board:
        if i == ' ':
            return False
    else:
        print('Sorry! no one wins, The match is draw.')
        return True




######### Game tic tac toe #########

from IPython.display import clear_output


# Veriables here
p1m = 'X'
p2m = 'O'
p1_loc = 0
p2_loc = 0
board = [' ']*10
board[0]=1
X_win = False
O_win = False
Board_Full = False

# visual representation
    # Display a 3X3 board
'''for i in range(10):
    board.append(' ')'''
display_board(board)

# Game here 

while True:
# Function
    # if the board has been filled
    Board_Full = board_full(board)
    if Board_Full == True:
        break

# User input
    # Plaer 1 Turn
    p1_loc = p_position(board, p1m)
    place_marker(board,p1m,p1_loc)
    display_board(board)
    X_win = win_check(board,p1m)
    if X_win == True:
        break
    
    # if the board has been filled
    Board_Full = board_full(board)
    if Board_Full == True:
        break

    # Plaer 2 Turn
    p2_loc = p_position(board, p2m)
    place_marker(board,p2m,p2_loc)
    display_board(board)
    O_win = win_check(board,p2m)
    if O_win == True:
        break

    # if the board has been filled
    Board_Full = board_full(board)
    if Board_Full == True:
        break