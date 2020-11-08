primary=input("Enter primary color:").lower()
secondary=input("Enter primary color:").lower()
if(primary=="red"):
    if(secondary=="yellow"):
        print("When you mix red and yellow, you get orange.")
    elif(secondary=="blue"):
        print("When you mix red and blue, you get purple.")
    else:
        print("You didn't input two primary colors.")
elif(primary =="blue"):
    if(secondary=="red"):
        print("When you mix blue and red, you get purple.")
    elif(secondary=="yellow"):
        print("When you mix blue and yellow, you get green.")
    else:
        print("You didn't input two primary colors.")
elif(primary=="yellow"):
    if(secondary=="red"):
        print("When you mix yellow and red, you get orange.")
    elif(secondary=="blue"):
        print("When you mix yellow and blue, you get green.")
    else:
        print("You didn't input two primary colors.")
else:
        print("You didn't input two primary colors.")