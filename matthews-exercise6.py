from helpers import *
import random

def createList(length):
    numList = []
    for i in range(length):
        ranNum = random.randint(0,100)
        numList.append(ranNum)
        numList.sort()
    return numList

greaterThanList = []
def largerTest(listNum, givenNum):
    if listNum > givenNum:
        greaterThanList.append(listNum)
        greaterThanList.sort()

def main():
    length = getInt('How many numbers do you want in the list: [Enter a Number greater than 0]')
    while length < 1:
        print('\nInvalid input. Try again...') 
        length = getInt('How many numbers do you want in the list: [Enter a Number greater than 0]')  
    givenNum = getNum('Give me a number: ')
    numList = createList(length)
    for i in numList:
        largerTest(i,givenNum)
    print('Your list was ' + str(numList))
    print('The greater numbers were ' + str(greaterThanList))

main()
     