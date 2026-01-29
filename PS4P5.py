#Nicholas Rodriguez - 1/29/2026 - PS4P5

#inputs
lastName = input("Enter your Last Name: ")
dependents = float(input("Enter your Number of Dependents: "))
grossIncome = float(input("Enter your Gross Income: "))

#process
adjGrossIncome = (grossIncome - dependents)*12000

if adjGrossIncome > 50000:
    taxRate = 0.20
else: taxRate = 0.10

incomeTax = adjGrossIncome * taxRate
if incomeTax < 0:
    incomeTax = 100


#outputs
print("Last Name: ", lastName)
print("Number of Dependents: ", dependents)
print("Adjusted Gross Income: $", adjGrossIncome)
print("Income Tax: $", incomeTax)