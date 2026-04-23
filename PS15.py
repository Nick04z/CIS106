#Nicholas Rodriguez - 4/23/2026 - PS15
#Class
class Employee:
    
    def __init__(self, first, last, pay, bonus):
        self.first = first
        self.last = last
        self.pay = pay
        self.bonus = bonus
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def empBonus(self):
        return self.bonus * self.pay
    
    def totalPay(self):
        return self.pay + self.empBonus()

#Main

emp_1 = Employee('Corey', 'Schafer', 50000, 0.10)
emp_2 = Employee('Test', 'User', 60000, 0.25)


print(emp_1.fullname())
print("Pay:$", emp_1.pay,"-- Bonus Rate:", emp_1.bonus)
print("Bonus Pay:$", emp_1.empBonus(), "-- Total Pay:$", emp_1.totalPay())
print("\n")
print(emp_2.fullname())
print("Pay:$", emp_2.pay,"-- Bonus Rate:", emp_2.bonus)
print("Bonus Pay:$", emp_2.empBonus(), "-- Total Pay:$", emp_2.totalPay())