#Nicholas Rodriguez - 2/26/2026 - PS8P4
#Function
def calcPayRate(jobCode):
    if jobCode == "L":
        payRate = 25.00
    elif jobCode == "A":
        payRate = 30.00
    elif jobCode == "J":
        payRate = 50.00
    else: payRate = float(input("Invalid Job Code! Please enter pay rate manually: "))
    return payRate
#Main
grossPaySum = 0
    #input
response = input("Do you want to run this gross pay program? (Yes or No)")
    #process
while response == "Yes":
    lastName = input("Enter Employee's Last Name: ")
    hoursWorked = float(input("Enter the number of hours worked: "))
    jobCode = input("Enter Job Code to get rate of pay: ")
    payRate = calcPayRate(jobCode)

    if hoursWorked > 40:
        overtimeHrs = hoursWorked - 40
        overtimePay = overtimeHrs * (payRate * 1.5)
        grossPay = (40 * payRate) + overtimePay
    else: grossPay = hoursWorked * payRate

    grossPaySum += grossPay
    print("Employee Last Name:", lastName)
    print("Employee Gross Pay: $", grossPay)
    response = input("Run this program again? (Yes or No)")
    #output
print("Total Employee Gross Pay: $", grossPaySum)