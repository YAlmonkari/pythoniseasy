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
"""

board = []
player = 1
winner = ""
# implementation of a list of posible moves
def emptyBoard(board):
    #rows
    for i in range(5,-1,-1):
        #columns
        for j in range(7):                 #          |8 |9 |10|11|12|13|14|
            board.append(" ")              #i*7+j+1   |1 |2 |3 |4 |5 |6 |7 |
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
                        #printing x and os from set
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
                    check(board, player)
                else:
                    while (board[rows+x-1] != " " and rows>=0):
                        rows -= 7
                        #column has an empty place for a dot.
                    if (rows>=0 and board[rows+x-1]) == " ":
                        if player == 1:
                            board[rows+x-1] = "x"
                        else:
                            board[rows+x-1] = "o"
                        check(board, player)
                    else:
                        #column is full.
                        print("Chose difrent column.")
                        board4(13,15,board)
                        check(board, player)
            else:    
            #input is out of range.
                print("Column index out of range.")
                board4(13,15,board)
                move(player,board)
                #in the end player 2 makes a move.
            if check(board, player):
                board4(13,15, board)
                break
            elif player == 1:
                player += 1
            #player 1 plays again
            else:    
                player -= 1
        except:
            print("Wrong input.")
        finally:
            board4(13,15, board)
            #check(board,x,player)
#chcek for the winning move
def check(board,player):
    #chcek if 0-3 1-4 2-5 3-6 is taken
    # 36-42, 29-35, 22-28, 15-21, 8-14, 1-7
    #dimentsions of a board
    rows = 6
    cols = 7
    winner = ""
    #counter for same dots in a row
    counter = 0
    #possition set to last row
    for k in range(rows):
        possition = cols*k
        for j in range(4):
            print(board[possition+j])
            if counter < 4:
                if board[possition+j] == "x":
                    counter += 1
                else:
                    counter = 0
                    return False
                    #counter is 4
            else:
                winner = player
                print("Player",winner,"winns!")
                return True
                break
#game starts, empty set is written to disc
emptyBoard(board)
#board is drawn
board4(13,15, board)
#player 1 starts the game
move(1,board)
