#Nicholas Rodriguez - 2/5/2026 - PS5P5

#input
lastName = input("Enter your Last Name: ")
salary = float(input("Enter your current Salary: "))
jobLvl = int(input("Enter your Job Level: "))

#process
if jobLvl >= 10:
    bonusRate = 0.25
elif jobLvl >= 5 and jobLvl <=9:
    bonusRate = 0.20
else: bonusRate = 0.10

finalBonus = salary * bonusRate

#output
print("Employee Last Name: ", lastName)
print("Congrats! Your Bonus is: $", finalBonus)