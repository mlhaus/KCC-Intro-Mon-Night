''' 
Chapter 3, Exercise  9
Input: pocket_number, int, 0 -36
Process: Determine what color the roulette pocket number is, by using boolean
         and logical operators to determine if the pocket number is odd.
         The color may be either black or red
Output: Color of the roulette pocket number entered, print(string) 
        ('The color of the roulette pocket is red', for example)
'''


# Get the user input (roulette pocket number)

pocket_number = int(input("Enter a pocket number:"))
	
if pocket_number == 0:
	print("The color of the pocket is green.")
elif (pocket_number >= 1 and pocket_number <= 10) or (pocket_number >= 19 and pocket_number <= 28):
	if pocket_number % 2 == 0:
		print("The color of the pocket is black.")
	else:
		print("The color of the pocket is red.")
elif (pocket_number >= 11 and pocket_number <= 18) or (pocket_number >= 29 and pocket_number <= 36):
	if pocket_number % 2 == 0:
		print("The color of the pocket is red.")
	else:
		print("The color of the pocket is black.")
else:
	print("Please enter a number, 0 - 36")