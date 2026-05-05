#Nicholas Rodriguez - 4/30/2026 - PS16P1
#Class
class Employee:
    
    bonusRate = 0.15

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def empBonus(self):
        return self.bonusRate * self.pay
    
    def totalPay(self):
        return self.pay + self.empBonus()
    
class Manager(Employee):
    def LTBonus(self):
        return self.pay * 0.40
    
class Executive(Employee):
    def executiveBonus(self):
        return self.pay * 2.00
    
    def LTBonus(self):
        return self.pay * 0.50


#Main

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
man_1 = Manager('Test', 'Manager', 500000)
exe_1 = Executive('Test', 'Executive', 1000000)

print(emp_1.bonusRate, emp_1.pay, emp_1.empBonus(), emp_1.totalPay())

print(man_1.email)
print("Manager Pay:$", man_1.pay)
print("Manager Bonus:$", man_1.LTBonus())
print("\n")
print(exe_1.email)
print("Executive Pay:$", exe_1.pay)
print("Executive Bonus:$", exe_1.executiveBonus())
print("Overide Bonus:$", exe_1.LTBonus())
