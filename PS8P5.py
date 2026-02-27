#Nicholas Rodriguez - 2/27/2026 - PS8P5
#Function
def calcTuition(credHrs, distCode):
    if distCode == "I":
        credCost = 250.00
    else: credCost = 550.00
    
    owedTuition = credHrs * credCost
    return owedTuition
#Main
tuitionSum = 0
    #input
response = input("Do you want to use this program? (Yes or No)")
    #process
while response == "Yes":
    lastName = input("Enter Student Last Name: ")
    credHrs = float(input("Enter the number of credit hours: "))
    distCode = input("Enter student's District Code (I or O): ")
    owedTuition = calcTuition(credHrs, distCode)

    tuitionSum += owedTuition
    print("Student Name:", lastName)
    print("Tuition Owed: $", owedTuition)
    response = input("Run this program again? (Yes or No) ")
    #output
print("Tuition owed by all students: $", tuitionSum)