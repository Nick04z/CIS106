#Nicholas Rodriguez - 2/5/2026 - PS5P2

#input
partNumber = int(input("Enter Part Number Here: "))
partQty = float(input("Enter the Quantity of Parts Here: "))

#process
if partNumber == 10 or partNumber == 55:
    unitCost = 1.00
elif partNumber == 99:
    unitCost = 2.00
elif partNumber == 80 or partNumber == 70:
    unitCost = 3.00
else: unitCost = 5.00

totalCost = partQty * unitCost

#output
print("Part Number: ", partNumber)
print("Unit Cost: $", unitCost)
print("Total Cost of Order: $", totalCost)