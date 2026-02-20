#Nicholas Rodriguez - 2/19/2026 - PS7P4
#input
file = open("PS7P4_data.txt", "r")
#process
orderCount = 0
exPriceSum = 0 
item = str(file.readline().rstrip('\n'))

while item != "":
    quantity = float(file.readline())
    itemPrice = float(file.readline())

    extendPrice = quantity * itemPrice
    exPriceSum += extendPrice
    orderCount += 1

    print("Item:", item, "  Quantity:", quantity, "  Price:$", itemPrice, "  Extended Price:$", extendPrice)
    item = str(file.readline().rstrip('\n'))

avgOrder = exPriceSum / orderCount
print("Extended Price Sum: ", exPriceSum)
print("Number of Orders: ", orderCount)
print("Average Cost of Orders: $", avgOrder)

