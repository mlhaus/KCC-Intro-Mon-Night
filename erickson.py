print("This program will determine the color of the pocket number entered.")

pocket = int(input("Enter pocket number (0 - 36): "))
if(pocket == 0):
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