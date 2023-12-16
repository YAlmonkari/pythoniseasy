#Python 3 course Projekt#1 - a simple game.

"""
01234567890....
---------------    0
| | | | | | | |    1
---------------    2
| | | | | | | |    3
---------------    4
| | | | | | | |    5
---------------    6
| | | | | | | |    7
---------------    8
| | | | | | | |    9
---------------    10
| | | | | | | |    11
---------------    12
6high x 7wide board
2 players - o and x
board list containing dots: [0,1,2,...,39,40,41]
"""
board = []
player = 1
# implementation of a list of posible moves
def emptyBoard(board):
    #rows
    for i in range(5,-1,-1):
        #columns
        for j in range(7):                 #          |8 |9 |10|11|12|13|14|
            board.append(" ")              #i*7+j+1   |1 |2 |3 |4 |5 |6 |7 |
#win win
def win(player,board):
	print("Player",player,"winns!")
	board4(13,15,board)
#function drawing a connect 4 board (13 rows, 15 columns)
def board4(rows, col, board):
    column=0
    #printing (-) dashes
    for i in range(rows):
        if i%2 == 0:
            for z in range(col):
                if z!= col-1:
                    print("-", end="")
                else:
                    print("-")
        else:
            # printing | | rows
            for j in range(col):
                if j != col -1:    
                    if j%2 ==0:
                        print("|", end="")
                    else:
                        print(board[column],end="")
                        column+=1
                else:
                    if j%2==0:
                        print("|")
                    else:
                        print(" ")
#function of user input
def move(player,board):
    while True:
        if player == 1:
            print("Player", player, "(x):")
        else:
            print("Player", player, "(o):")
        try:
            x = int(input("Please specyfi which column You want place your dot (1-7): "))
        except:
            print("Wrong input.")
            x = 0
        finally:
        # check for taken places.
        #input is between 1 and 7.
            if x<=7 and x>=1:
                rows=7*5
                #chosen column is empty, dot is placed.
                if board[rows+x-1] == " ":
                    if player == 1:
                        board[rows+x-1] = "x"
                    else:
                        board[rows+x-1] = "o"
                    if check(board, x, player):
                        win(player,board)
                        break
                else:
                    while (board[rows+x-1] != " " and rows>=0):
                        rows -= 7
                        #column has an empty place for a dot.
                    if (rows>=0 and board[rows+x-1]) == " ":
                        if player == 1:
                            board[rows+x-1] = "x"
                        else:
                            board[rows+x-1] = "o"
                        if check(board, x, player):
                            win(player,board)
                            break
                    else:
                        #column is full.
                        print("Chose difrent column.")
                        move(player, board)
            elif x == 0:
                print("Try again.")
                move(player,board)
            else:    
                #input is out of range.
                print("Column index out of range.")
                move(player,board)
            #in the end player 2 makes a move.
            if player == 1:
                board4(13,15,board)
                player +=1
            #player 1 plays again
            else:
            	board4(13,15,board)
            	player -= 1
            	if check_for_tie(board):
            	   print("It is a tie!")
            	   break
#chcek for the winning move
def check(board, x, player):
    if player == 1:
        winner = "x"
    else:
        winner = "o"
    # Check for horizontal win
    for row in range(6):
        for col in range(4):
            if board[row * 7 + col] == winner and board[row * 7 + col + 1] == winner and board[row * 7 + col + 2] == winner and board[row * 7 + col + 3] == winner:
                return True
    # Check for vertical win
    for col in range(7):
        for row in range(3):
            if board[row * 7 + col] == winner and board[(row + 1) * 7 + col] == winner and board[(row + 2) * 7 + col] == winner and board[(row + 3) * 7 + col] == winner:
                return True
    # Check for diagonal win (top left to bottom right)
    for row in range(3):
        for col in range(4):
            if board[row * 7 + col] == winner and board[(row + 1) * 7 + col + 1] == winner and board[(row + 2) * 7 + col + 2] == winner and board[(row + 3) * 7 + col + 3] == winner:
                return True
    # Check for diagonal win (bottom left to top right)
    for row in range(3, 6):
        for col in range(4):
            if board[(row - 3) * 7 + col + 3] == winner and board[(row - 2) * 7 + col + 2] == winner and board[(row - 1) * 7 + col + 1] == winner and board[row * 7 + col] == winner:
                return True
def check_for_tie(board):
    for i in range(len(board)):
        if board[i] == " ":
            return False
    return True
#game starts, empty set is written to disc
emptyBoard(board)
#board is drawn
board4(13,15, board)
#player 1 starts the game
move(1,board)
