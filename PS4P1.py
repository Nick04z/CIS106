#Nicholas Rodriguez - 1/29/2026 - PS4P1

#inputs
quantity = float(input("Enter Quantity of Item: "))
#process
if quantity >= 1000:
    unitPrice = 3.00
else: unitPrice = 5.00

extendPrice = quantity * unitPrice
taxAmount = round(extendPrice * 0.07, 2)
totalPrice = extendPrice + taxAmount

#outputs
print("Quantity of Items: ", quantity)
print("Unit Price: $", unitPrice)
print("Extended Price: $", extendPrice)
print("Tax: $", taxAmount)
print("Total Price: $", totalPrice)