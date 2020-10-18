from helpers import getNum

# STEP 3 - Define a function named drawBoard that takes an array (board) as a parameter. 
    # STEP 4 - Print the values of the board array parameter. Format them as a tic-tac-toe board.
    # 1 | 2 | 3
    #-----------
    # 4 | 5 | 6
    #-----------
    # 7 | 8 | 9

# STEP 13 - Define a function named checkWinner that accepts an array (board) and string (currentPlayer) as parameters.
    # STEP 14a - Create a variable named result and assign it False.
    # STEP 15 - Write an if statement to check if there are 3 matching board values. For example, if board array indexes 0, 1, and 2 are all equal we have a winner. There are 8 different combinations to win: [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7, [2, 5 8], [0, 4, 8], and [2, 4, 6].
    
        # STEP 16 - If true, print a message to congratulate the current player and assign True to the result variable.
        
    # STEP 14b - Return the result variable.
    

# STEP 6 - Define a function named switchPlayer that accepts a string (currentPlayer) as a parameter.
    # STEP 7 - Write an if-else statement (or ternary operator) to change the currentPlayer from "X" to "O", and vice versa. 
    
    # STEP 8 - Print a message indicating who the current player is and return the currentPlayer variable.
    

def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    currentPlayer = "O"
    gameOver = False
    # STEP 1 - Using the gameOver variable, write a while a loop that will run continuously if the game is not over.
    
        # STEP 2 - Call a function named drawBoard. Pass the array to the function. No value will be returned.
        
        # STEP 5 - Call a function named switchPlayer, passing the currentPlayer variable as the argument. The result returned from the function will be assigned back to the currentPlayer variable.
        
        # STEP 9 - Prompt the current player for a number between 1 and 9. Give them an infinite amount of attempts. Convert the numerical input to an integer. Assign the player's response a variable named choice.
        # getNum(prompt, minValue, maxValue, totalAttempts, convertToInt, invalidMsg)
        
        # STEP 11 - Using the choice variable, write a while loop that checks the board array if an "X" or "O" is currently located at the index the player chose. If true, prompt the user for another choice using the same getNum function as Step 9.
        
        # STEP 10 - Assign the currentPlayer variable to location the player chose in the board array. Note: if the user chooses 1, we need to assign the value to index 0.
        
        # STEP 12 - Call a function named checkWinner. Pass the board array and the currentPlayer variables to the function. Assign the value returned to a gameOver variable.
        

main()​