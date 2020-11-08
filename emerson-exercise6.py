from helpers import getNum
from random import randint

# STEP 3: Define a randomNumbers function that takes a number as a parameter.
def randomNumbers(number):
	# STEP 4a: Create an empty array called result
  result = []
	# STEP 5: Create a loop that runs n times
  for i in range(number):
		# STEP 6: Generate a random number between 0 and 100. Add the number to the result array.
      randomNumber = randint(0, 100)
      result.append(randomNumber)
	# STEP 4b: Return the result array variable
  return result

# STEP 9: Define a largerThan function that takes an array of numbers and a single number as parameters.
def largerThan(array, number):
    # STEP 10: Create an empty array called result
  result = []
    # STEP 11: Create a loop that runs once for each item in the list/array parameter
  for num in array:
    	# STEP 12: Write an if statement to test if the current value in the list is greater than the number parameter
      if num > number:
    		# STEP 13: If true, write another if statement to test if the current value in the list is not already in the result array
        if num not in result:
    			# STEP 14: If true, add the current value in the list to the result array
          result.append(num)
    # STEP 15: Print the list array variable. Label it "List of numbers".
  print("List of numbers", array)
    # STEP 16: Sort the result array variable and print it. Label it "Numbers that are greater than [n]"
  result.sort()
  print("Numbers that are greater than", number, result)

def main():
  # STEP 1: Prompt the user for a number between 10 and 20. Assign the user's response to a variable called howMany.
  howMany = getNum("Please give a num between 10 and 20", 10, 20, float("inf"), True, "Numbers between 10 and 20 please")
  # STEP 2: Call a randomNumbers function, passing the howMany variable as an argument. Assign the result to a variable called list.
  list = randomNumbers(howMany)
  # STEP 7: Prompt the user for a number between 0 and 100. Assign the user's response to a variable called n.
  n = getNum("Please give a num between 0 and 100", 0, 100, float("inf"), True, "Numbers between 0 and 100")
  # STEP 8: Call a largerThan function, passing the list and n variables as arguments.
  largerThan(list, n)
  
main()