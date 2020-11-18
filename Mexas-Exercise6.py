from helpers import getNum
from random import randint
from random import randrange

'''
p403  Larger Than 'n'
'''
# ACP to my own folder, then do pull request.

def randomNumbers(num):
	result = [] 
	for i in range(0, num): 
		result.append(randrange(0, 101)) 
	return result 

def largerThan(arr, num):
    result = []
    for item in arr:
    	if item > num: 
    		if item not in result: 
    			result.append(item) 
    result.sort()
    print("Our list of numbers:", arr) 
    print("Numbers that are greater than [" + str(num) + "]:", result)