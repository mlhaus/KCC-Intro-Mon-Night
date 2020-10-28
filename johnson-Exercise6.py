from helpers import getNum
import random

def randomNumber(number):
  result = []
  for i in range(number):
    rand = random.randint(0, 100)
    result.append(rand)
  return result

def largerThan(arr, int):
  result = []
  for number in arr:
    if(number > int):
      if(number not in result):
        result.append(number)
  print("List of numbers: " + str(arr))
  result.sort()
  print("Numbers that are greater than", int, str(result))


def main():
  howMany = getNum("How many random numbers?", 10, 20, float("inf"), True)
  list = randomNumber(howMany)
  n = getNum("Enter smallest desired number.", 0, 100, float("inf"), True)
  largerThan(list, n)
  
main()