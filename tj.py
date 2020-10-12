primaryColor1 = input( "Please enter a primary color: ")
primaryColor2 = input( "Please enter a second primary color: ")

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