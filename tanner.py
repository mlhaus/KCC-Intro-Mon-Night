from helpers import *

def package_calculator(weight):
    
    if weight > 0 and weight <= 2 :
        print("Your shipment will cost $" + str(1.5 * weight) + " at a rate of $1.50 per pound.")
    elif weight > 2 and weight <= 6 :
        print("Your shipment will cost $" + str(3 * weight) + " at a rate of $3.00 per pound.")
    elif weight > 6 and weight <= 10 :
        print("Your shipment will cost $" + str(4 * weight) + " at a rate of $4.00 per pound.")
    elif weight > 10 and weight <= 500 :
        print("Your shipment will cost $" + str(4.75 * weight) + " at a rate of $4.75 per pound.")
    elif weight > 500 :
        print("Too heavy! Keep it under 1000lbs!")
    else :
        print("Error! Invalid package weight! Try again.")

package_weight = getNum("How much does your package weigh?", .1, 500, float("inf"), False, "Error! Invalid package weight! Try again.")
package_calculator(package_weight)
