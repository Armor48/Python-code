import random
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

currentplayer = "X"
winner = None
gamerunning = True

#printing board
def printboard(board):

    print(board[0] + " || " + board[1] + " || "+board[2])
    print('============')
    print(board[3] + " || " + board[4] + " || "+board[5])
    print('============')
    print(board[6] + " || " + board[7] + " || "+board[8])
    
#taking input from user
def take_input(board):
    inp = int(input("enter no. 1-9 "))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1] = currentplayer
    else:
        print('oops! Place is occupied...')

#check input on board
def row(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def column(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
def dianogal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

#check win
def checkwin():
    global gamerunning
    if row(board) or column(board) or dianogal(board):
        print("The winner is: ",winner)
        gamerunning = False

#check for tie
def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("match tie!")
        gamerunning = False

#switch player
def switchply():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

#code for computer
def computer(board):
    while currentplayer == "O":
        position = random.randint(0,8)
        if board[position]=="-":
            board[position] = "O"
            switchply()

#loop for running game
while gamerunning:
    printboard(board)
    take_input(board)
    checkwin()
    checktie(board)
    switchply()
    computer(board)
    checkwin()
    checktie(board)