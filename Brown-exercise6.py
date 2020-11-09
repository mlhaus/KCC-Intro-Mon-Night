from helpers import getNum
from random import randint
import random


# STEP 3: Define a randomNumbers function that takes a number as a parameter.
def randomNumbers(number):
    # STEP 4a: Create an empty array called result
    result = []
    # STEP 5: Create a loop that runs n times
    for i in range(number):
        # STEP 6: Generate a random number between 0 and 100. Add the number to the result array.  
        result.append(random.randint(0, 100))
    # STEP 4b: Return the result array variable
    return result

# STEP 9: Define a largerThan function that takes an array of numbers and a single number as parameters.                    
def largerThan(numberList, number):
    # STEP 10: Create an empty array called result
    result = []
    # STEP 11: Create a loop that runs once for each item in the list/array parameter
    for i in numberList:
    # STEP 12: Write an if statement to test if the current value in the list is greater than the number parameter   
        if i > number:
            # STEP 14: If true, add the current value in the list to the result array
            if i not in result:
                result.append(i)
    # STEP 15: Print the list array variable. Label it "List of numbers".
    print("List of numbers: ", str(numberList))
    # STEP 16: Sort the result array variable and print it. Label it "Numbers that are greater than [n]"
    result.sort()
    print("Numbers that are greater than ", number, ":", str(result))
    return result      
                  
def main():
  # STEP 1: Prompt the user for a number between 10 and 20. Assign the user's response to a variable called howMany.    
    howMany = getNum("Please enter a number between 10 and 20", 10, 20, float("inf"), True, "Invalid number.")
    # STEP 2: Call a randomNumbers function, passing the howMany variable as an argument. Assign the result to a variable called list.
    list = randomNumbers(howMany)
    # STEP 7: Prompt the user for a number between 0 and 100. Assign the user's response to a variable called n.
    n = getNum("Please enter a number between 0 and 100", 0, 100, float("inf"), True, "Invalid number.")
     # STEP 8: Call a largerThan function, passing the list and n variables as arguments.
    largerThan(list, n)
          
main()

