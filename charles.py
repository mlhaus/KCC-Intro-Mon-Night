#input
user_number = int(input("Choose a pocket for roulette! Pick any number 0-36!"))
#processes
#GREEN is 0
#RED is 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
#BLACK is 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35
if user_number == 0 :
    print("Your pocket is green!")
elif (user_number >= 1 and user_number <= 10) and user_number % 2 == 0 :
    print("Your pcket is black!")
elif (user_number >= 1 and user_number <= 10) and user_number % 2 != 0 :
    print("Your pocket is red!")
elif (user_number >= 11 and user_number <= 18) and user_number % 2 == 0 :
    print("Your pocket is red!")
elif (user_number >= 11 and user_number <= 18) and user_number % 2 != 0 :
    print("Your pocket is black!")
elif (user_number >= 19 and user_number <= 28) and user_number % 2 == 0 :
    print("Your pocket is black!")
elif (user_number >= 19 and user_number <= 28) and user_number % 2 != 0 :
    print("Your pocket is red!")
elif (user_number >= 29 and user_number <= 36) and user_number % 2 == 0 :
    print("Your pocket is red!")
elif (user_number >= 29 and user_number <= 36) and user_number % 2 != 0 :
    print("Your pocket is black!")
else : 
    print("Error! Try again! Make sure to use a number 0-36!")