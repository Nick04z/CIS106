#Nicholas Rodriguez - 3/12/2026 - PS10P5
totalPrice = 0.0
taxAmt = 0.0

#Function
def calcTotalTax(itemQty, unitPrice):
    global totalPrice
    totalPrice = itemQty * unitPrice
    global taxAmt
    taxAmt = totalPrice * 0.07
    return 

#Main
    #input
itemQty = float(input("Enter the quantity of items: "))
unitPrice = float(input("Enter the unit price of the item: "))
    #process
calcTotalTax(itemQty, unitPrice)
    #output
print("Total Price: $", format(totalPrice, '.2f'))
print("Tax Amount: $", format(taxAmt, '.2f'))