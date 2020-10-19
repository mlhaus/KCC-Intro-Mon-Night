from helpers import *

def primary_color(primary_color1,primary_color2): 
     

    
    if (primaryColor1 == "red" and primaryColor2 == "blue") or (primaryColor1 == "blue" and primaryColor2 == "red"):
        print (primaryColor1 + " mixed with " + primaryColor2 + " is purple")
    elif (primaryColor1 == "red" and primaryColor2 == "yellow") or (primaryColor1 == "yellow" and primaryColor2 == "red"):
        print (primaryColor1 + " mixed with " + primaryColor2 + " is orange")
    elif (primaryColor1 == "blue" and primaryColor2 == "yellow") or (primaryColor1 == "yellow" and primaryColor2 == "blue"):
        print (primaryColor1 + " mixed with " + primaryColor2 + " is green")
    else:
        print ("One color, " + primaryColor1 + " or " + primaryColor2 + " isn't a primaryColor")


primaryColor1 = validateUserString("Choose a color" ,["red","yellow","blue"],True ,3 ,"Please choose red, yellow, or blue")
primaryColor2 = validateUserString("Choose a second color" ,["red","yellow","blue"] ,True , 3, "Please choose red, yellow, or blue")

primary_color("primaryColor1, primaryColor2") 

