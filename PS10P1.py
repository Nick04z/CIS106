#Nicholas Rodriguez - 3/12/2026 - PS10P1
#Function
def discountCalc(itemQty, itemPrice, discRate):
    extendPrice = itemQty * itemPrice
    discAmt = extendPrice * discRate
    discPrice = extendPrice - discAmt
    return discAmt, discPrice

#Main
    #input
itemQty = float(input("Enter the quantity of items: "))
itemPrice = float(input("Enter the price of the item: "))
discRate = float(input("Enter the discount rate as a decimal: "))
    #process
discAmt, discPrice = discountCalc(itemQty, itemPrice, discRate)
    #output
print("Item Quantity:", itemQty)
print("Item Price: $", itemPrice)
print("Discount Amount: $", format(discAmt, '.2f'))
print("Discounted Price: $", format(discPrice, '.2f'))