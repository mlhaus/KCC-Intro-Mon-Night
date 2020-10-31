from helpers import getNum
def shipping_charges(weightofPackage):
    if weightofPackage < 0.1:
        print("Sorry bad input")
    elif weightofPackage <= 2:
        shippingCharges = weightofPackage * 1.50
        print("This is the charges for shipping: $",shippingCharges)
    elif weightofPackage > 2 and weightofPackage <= 6:
        shippingCharges = weightofPackage * 3
        print("This is the charges for shipping: $",shippingCharges)
    elif weightofPackage > 6 and weightofPackage <=10:
        shippingCharges = weightofPackage * 4
        print("This is the charges for shipping: $",shippingCharges)
    else:
        shippingCharges = weightofPackage * 4.75
        print("This is the charges for shipping: $",shippingCharges)

userWeight = getNum("What is the weight of the package?", 0.1, 150, 3, False, "Invalid weight")
shipping_charges(userWeight)