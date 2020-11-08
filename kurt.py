primaryColor1 = input( "Enter primary color 1: ")
primaryColor2 = input( "Enter primary color 2: ")

if ( primaryColor1 == "red" and primaryColor2 == "blue" ) or \
   ( primaryColor1 == "blue" and primaryColor2 == "red" ):
    print( primaryColor1 + " mixed with " + primaryColor2 + " is purple" )
elif ( primaryColor1 == "red" and primaryColor2 == "yellow" ) or \
   ( primaryColor1 == "yellow" and primaryColor2 == "red" ):
    print( primaryColor1 + " mixed with " + primaryColor2 + " is orange" )
elif ( primaryColor1 == "yellow" and primaryColor2 == "blue" ) or \
   ( primaryColor1 == "blue" and primaryColor2 == "yellow" ):
    print( primaryColor1 + " mixed with " + primaryColor2 + " is green" )
else:
    print( "One of your colors, " + primaryColor1 + " or " + \
        primaryColor2 + " is not a primaryColor" )