#Nicholas Rodriguez - 2/19/2026 - PS7P3
#input
file = open("PS7P3_data.txt", "r")
#process
sumBonus = 0
lastName = str(file.readline().rstrip('\n'))

while lastName != "":
    salary = float(file.readline())

    if salary >= 100000:
        bonusRate = .20
    elif salary == 50000:
        bonusRate = .15
    else: bonusRate = .10

    bonus = salary * bonusRate
    sumBonus += bonus

    print("Employee Last Name: ", lastName, "   Salary: $", salary, "   Bonus: $", bonus)
    lastName = str(file.readline().rstrip('\n'))

print("Sum of all bonuses: $", sumBonus)