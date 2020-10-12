packageWeight = float(input("Please enter the weigh of your package: "))
if(packageWeight >= 0):

    if (packageWeight <= 2):
        shipCharge = packageWeight * 1.5

    elif (packageWeight <= 6):
        shipCharge = packageWeight * 3.0

    elif (packageWeight <= 10):
        shipCharge = packageWeight * 4.0

    elif (packageWeight > 10):
        shipCharge = packageWeight * 4.75

    print("Your shipping charge is $" + format(shipCharge, "5.2f") + ".")

else:
    print("Invalid weight")