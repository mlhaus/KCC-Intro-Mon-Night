'''
7. Color Mixer
The colors red, blue, and yellow are known as the primary colors because they cannot be made by mising other colors. When you mix two primary colors, you get a secondary color, as shown here:
When you mix red and blue you get purple
when you mix red and yellow you get orange
when you mix blue and yellow you get green
Design a program that prompts the user to enter the names of two primary colors to mix.
If the User enters anything other then "red", "blue" or "yellow", the program should display an error message.
Otherwise, the program should display the name of the secondary color that results.
'''

color1 = input("Choose One: Blue, Red or Yellow:").lower().strip()
if color1 != "red" and color1 != "blue" and color1 != "yellow":
    print("That was not an option.")
color2 = input("Choose a Second One: Blue, Red or Yellow:").lower().strip()
if color2 != "red" and color2 != "blue" and color2 != "yellow":
    print("That was not an option.")
if color1 == "red" and color2 == "red":
    print("There is no secondary color.")
elif color1 == "blue" and color2 == "blue":
    print("There is no secondary color.")
elif color1 == "yellow" and color2 == "yellow":
    print("There is no secondary color.")
elif color1 == "red" and color2 == "blue" or  color1 == "blue" and color2 == "red":
    print("Those together make Purple.")
elif color1 == "yellow" and color2 == "red" or color1 == "red" and color2 == "yellow":
    print("Those together make Orange")
elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue":
    print("Those together make Green.")
else:
    print("Those two colors are not apart of this program.")