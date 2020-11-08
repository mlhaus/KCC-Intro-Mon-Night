# Shipping charges
# Rate per pounds
RATE_PER_POUND_2LBS_OR_LESS = 1.50
RATE_PER_POUND_OVER2LBS_NOTMORE_THAN6 = 3.00
RATE_PER_POUND_OVER6LBS_NOTMORE_THAN10 = 4.00
RATE_PER_POUND_OVER10LBS = 4.75
# Ask for weight of package
weightofPackage = float(input("Weight of the package in pounds: "))
# Calculate the shipping charges
if weightofPackage <= 2:
    shippingCharges = weightofPackage * RATE_PER_POUND_2LBS_OR_LESS
    print("This is the charges for shipping: $",shippingCharges)
elif weightofPackage > 2 and weightofPackage <= 6:
    shippingCharges = weightofPackage * RATE_PER_POUND_OVER2LBS_NOTMORE_THAN6
    print("This is the charges for shipping: $",shippingCharges)
elif weightofPackage > 6 and weightofPackage <=10:
    shippingCharges = weightofPackage * RATE_PER_POUND_OVER6LBS_NOTMORE_THAN10
    print("This is the charges for shipping: $",shippingCharges)
else:
    shippingCharges = weightofPackage * RATE_PER_POUND_OVER10LBS
    print("This is the charges for shipping: $",shippingCharges)