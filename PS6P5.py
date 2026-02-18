#Nicholas Rodriguez - 2/18/2026 - PS6P5
#input
response = input("Would you like to use this program? (Yes or No) ")

#process - Before Loop
discountSum = 0

#process - Loop:
while response == "Yes":
    itemQty = float(input("Enter the quantity of items to order: "))
    itemPrice = float(input("Enter the price of the item: $"))
    extendPrice = itemQty * itemPrice

    if extendPrice > 10000:
        discount = 0.25
    else:
        discount = 0.10

    discountAmt = extendPrice * discount
    totalPrice = extendPrice - discountAmt
    discountSum += discountAmt

    print("Extended Price: $", round(extendPrice, 2))
    print("Amount Discounted: $", round(discountAmt, 2))
    print("Total Price of order: $", round(totalPrice, 2))
    response = input("Run the program again? (Yes or No) ")
print("Sum of all discounts: $", round(discountSum, 2))