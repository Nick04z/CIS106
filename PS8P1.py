#Nicholas Rodriguez - 2/26/2026 - PS8P1
#Function
def compExtPrice(itemQty, unitPrice):
    extPrice = itemQty * unitPrice

    if extPrice > 10000.00:
        disountAmt = extPrice * 0.10
    else: disountAmt = 0

    finalExtPrice = extPrice - disountAmt
    return finalExtPrice
#Main
exPriceSum = 0
    #Input
response = input("Do you want to use this Program? (Yes or No)")
    #Process
while response == "Yes":
    itemQty = float(input("Enter the quantity of items: "))
    unitPrice = float(input("Enter the price of the item: "))
    extPrice = compExtPrice(itemQty, unitPrice)

    print("Item Quantity:", itemQty)
    print("Unit Price: $", unitPrice)
    print("Extended Price: $", round(extPrice, 2))

    exPriceSum += extPrice
    response = input("Do you want to run this program again? (Yes or No)")

print("Sum of Extended Prices: $",exPriceSum)

