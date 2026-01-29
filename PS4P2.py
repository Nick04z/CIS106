#Nicholas Rodriguez - 1/29/2026 - PS4P2

#inputs
itemName = input("Name of Item: ")
quantity = float(input("Quantity of Item: "))

#process
if itemName == "A":
    unitPrice = 10.00
else: unitPrice = 20.00

extendPrice = quantity * unitPrice

#outputs
print("Item: ", itemName)
print("Unit Price: $", unitPrice)
print("Extended Price: $", extendPrice)
