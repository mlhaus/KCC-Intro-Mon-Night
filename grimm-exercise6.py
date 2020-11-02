from helpers import getNum
from random import randint

def randomNumbers(number):
  result = []
  for i in str(number):
    result.append(randint (0,100))
  return result

def largerThan(array,number):
    result = []
    for item in range (len(array)):
      if array[item] > number:
        if item not in result:
          result.append(array[item])
    print ("List of numbers:", array)
    print ("Numbers that are greater than [n]:", result)

def main():
  howMany = getNum("Enter a number between 10 and 20: " ,10,20)
  list = randomNumbers(howMany)
  n = getNum("Enter a number between 0 and 100: ",0,100)
  largerThan(list,n)
  
main()
