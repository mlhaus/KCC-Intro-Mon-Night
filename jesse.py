from helpers import *
def get_pocket_color(pocket_number):
    		
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

entered_number = getNum("Enter a pocket number ", 0, 36, 3, True, "This is an invalid number")
get_pocket_color(entered_number)


