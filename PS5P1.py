#Nicholas Rodriguez - 2/5/2026 - PS5P1

#input
widgetQty = float(input("Enter Quantity of Widgets: "))

#process
if widgetQty > 10000:
    itemPrice = 10
elif widgetQty >= 5000 and widgetQty <= 10000:
    itemPrice = 20
else: itemPrice = 30

extendPrice = widgetQty * itemPrice
taxAmount = extendPrice * 0.07
totalPrice = extendPrice + taxAmount

#output
print("Extended Price: $", extendPrice)
print("Tax Amount: $", taxAmount)
print("Total Price of Widget: $", totalPrice)