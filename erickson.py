# 1. define a function
# 2. convert all inputs into parameters
# 3. indent remaining code so that it's part of function
# 4. call the function, passing appropriate values
# 5. obtain values using helpers

print("This program will determine the color of the Roulette pocket number entered.")

from helpers import getNum
def pocketPicker(pocket = 0):   # 1, 2           # 5 vvv
    pocket = getNum("", 0, 36, float("inf"), convertToInt=True, invalidMsg="That is not a Roulette pocket number.")
    if(pocket == 0):        # 3
        print("Pocket", pocket, "is Green.")
    elif(1 <= pocket <= 10):
        if((pocket % 2) == 0):
            print("Pocket", pocket, "is Black.")
        else: print("Pocket", pocket, "is Red.")
    elif(11 <= pocket <= 18):
        if((pocket % 2) == 0):
            print("Pocket", pocket, "is Red.")
        else: print("Pocket", pocket, "is Black.")
    elif(19 <= pocket <= 28):
        if((pocket % 2) == 0):
            print("Pocket", pocket, "is Black.")
        else: print("Pocket", pocket, "is Red.")
    elif(29 <= pocket <= 36):
        if((pocket % 2) == 0):
            print("Pocket", pocket, "is Red.")
        else: print("Pocket", pocket, "is Black.")
    else: print(pocket, "is not a valid pocket number.")

pocketPicker(-5)             # 4
pocketPicker(34)
pocketPicker(8)
pocketPicker(50)
