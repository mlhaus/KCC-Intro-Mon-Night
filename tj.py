from helpers import *



def colors(primaryColor1, primaryColor2):


    if (primaryColor1 == "red" and primaryColor2 == "blue") or \
        (primaryColor1 == "blue" and primaryColor2 == "red"):
        print( "When you mix " + primaryColor1 + " with " + primaryColor2 + " you get purple!")
    elif (primaryColor1 == "red" and primaryColor2 == "yellow") or \
        (primaryColor1 == "yellow" and primaryColor2 == "red"):
        print( "When you mix " + primaryColor1 + " with " + primaryColor2 + " you get orange!")
    elif (primaryColor1 == "yellow" and primaryColor2 == "blue") or \
        (primaryColor1 == "blue" and primaryColor2 == "yellow"):
        print( "When you mix " + primaryColor1 + " with " + primaryColor2 + " you get green!")
    else:
        print("You entered a color that is not primary")

primaryColor1 = validateUserString("Choose a color", ["red", "yellow", "blue"], True, 3, "Please choose red, yellow, or blue")
primaryColor2 = validateUserString("Choose a second color", ["red", "yellow", "blue"], True, 3, "Please choose red, yellow, or blue")

colors(primaryColor1, primaryColor2)
