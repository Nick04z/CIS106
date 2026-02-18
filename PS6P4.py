#Nicholas Rodriguez - 2/17/2026 - PS6P4
#input
response = input("Would you like to use this Program? Yes or No ")

#process - Before Loop:
grossSum = 0
empCount = 0

#process - Loop:
while response == "Yes":
    empLastName = input("Enter Employee's Last Name: ")
    hoursWorked = float(input("Enter the Number of Hours Worked: "))
    payRate = float(input("Enter Employee Pay Rate: $"))

    if hoursWorked > 40:
        overtimeHrs = hoursWorked - 40
        overtimePay = overtimeHrs * (payRate * 1.5)
        grossPay = ((hoursWorked - overtimeHrs)* payRate) + overtimePay
    else:
        grossPay = hoursWorked * payRate
    
    grossSum += grossPay
    empCount += 1 

    print("Employee Last Name: ", empLastName)
    print("Employee Gross Pay: $", grossPay)
    response = input("Run the Program Again? (Yes or No)")

avgPay = grossSum / empCount
print("Sum of all Gross Pays: $", grossSum)
print("Number of Employees: ", empCount)
print("Average Employee Pay: $",round(avgPay, 2))