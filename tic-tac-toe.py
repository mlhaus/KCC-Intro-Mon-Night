from helpers import getNum

def drawBoard(board):
    print("", board[0], "|", board[1], "|", board[2])
    print("-----------")
    print("", board[3], "|", board[4], "|", board[5])
    print("-----------")
    print("", board[6], "|", board[7], "|", board[8])

def switchPlayer(currentPlayer):
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    print("Player "+ currentPlayer +", it's your turn." )
    return currentPlayer

def checkWinner(board, currentPlayer, turns):
    result = False
    if turns == 9:
        drawBoard(board)
        result = True
        print("Game end in a tie. No winner.")
    elif ( 
      board[0] == board[1] and board[1] == board[2] or
      board[3] == board[4] and board[4] == board[5] or
      board[6] == board[7] and board[7] == board[8] or
      board[0] == board[3] and board[3] == board[6] or
      board[1] == board[4] and board[4] == board[7] or
      board[2] == board[5] and board[5] == board[8] or
      board[0] == board[4] and board[4] == board[8] or
      board[2] == board[4] and board[4] == board[6] ):
        drawBoard(board)
        result = True
<<<<<<< HEAD
        print("Player " + currentPlayer + " WINS!")
=======
        drawBoard(board)
        print("Congratulations ", currentPlayer + ", you won!")
>>>>>>> 9c7d0a222af0e4d6332910c5e46674cec20bdf9d
    return result

def main():
    turns = 0
    currentPlayer = "O"
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gameOver = False
    count = 0
    while(not gameOver):
        drawBoard(board)
        currentPlayer = switchPlayer(currentPlayer)
        turns += 1
        choice = getNum("Player " + currentPlayer + ",", 1, len(board), float("inf"), True)
        while (board[choice-1] == "X" or board[choice-1] == "O"):
            choice = getNum("That spot is taken, try again:", 1, len(board), float("inf"), True)
        board[choice - 1] = currentPlayer
<<<<<<< HEAD
        gameOver = checkWinner(board,currentPlayer,turns)
=======
        count += 1
        gameOver = checkWinner(board,currentPlayer)
        if(count == 9):
            gameOver = True
            drawBoard(board)
            print("It's a tie folks!")
          
    
        
>>>>>>> 9c7d0a222af0e4d6332910c5e46674cec20bdf9d

main()
