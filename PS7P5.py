#Nicholas Rodriguez - 2/19/2026 - PS7P5
#input
file = open("PS7P5_data.txt", "r")
#process
tuitionSum = 0
studentCount = 0 
lastName = str(file.readline().rstrip('\n'))

while lastName != "":
    disCode = str(file.readline())
    creditsTaken = float(file.readline())

    if disCode == "I":
        costPerCredit = 250.00
    else: costPerCredit = 500.00

    tuition = creditsTaken * costPerCredit
    tuitionSum += tuition
    studentCount += 1

    print("Student Last Name:", lastName, "|Credits Taken:", creditsTaken, "|Tuition: $", tuition)
    lastName = str(file.readline().rstrip('\n'))

#output
print("Sum of Tuition:$",tuitionSum)
print("Number of Students:", studentCount)