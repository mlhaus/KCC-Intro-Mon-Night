from helpers import *

def shippingCharger(packageWeight):
    if (packageWeight > 10):
        shippingCharges = packageWeight * 4.75
        print("Your shipping charges are $" + format(shippingCharges, ".2f"))
    elif(packageWeight <= 10 and packageWeight > 6):
        shippingCharges = packageWeight * 4.00
        print("Your shipping charges are $" + format(shippingCharges, ".2f"))
    elif(packageWeight <= 6 and packageWeight > 2):
        shippingCharges = packageWeight * 3.00
        print("Your shipping charges are $" + format(shippingCharges, ".2f"))
    elif(packageWeight <= 2 and packageWeight > 0):
        shippingCharges = packageWeight * 1.50
        print("Your shipping charges are $" + format(shippingCharges, ".2f"))

packageWeight = getNum("Enter package weight: ", 0.1, 150, 3, False, "C'mon now.... get serious!" )
shippingCharger(packageWeight)