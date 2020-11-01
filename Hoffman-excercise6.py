from helpers import getNum
from random import randint

def randomNumber(number):
	result = []
	for i in range(number):
		rand = randint(0, 100)
		result.append(rand)
	return result

def largerThan(arr, int):
    result = []
    for number in arr:
    	if(number > int):
    		if(number not in result):
    			result.append(number)
    print("List of numbers: " + str(arr))
    print("Numbers that are greater than", int, str(result))


def main():
  howMany = getNum("Enter a number between 10 and 20: ", 10, 20, float("inf"), True)
  list = randomNumber(howMany)
  n = getNum("Enter a number between 0 and 100: ", 0, 100, float("inf"), True)
  largerThan(list, n)

main()