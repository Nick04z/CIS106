#Nicholas Rodriguez - 4/22/2026 - PS14P1

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


emp_1 = Employee('Corey', 'Schafer', 50000, 0.10)
emp_2 = Employee('Test', 'User', 60000, 0.25)

#print(emp_1)
#print(emp_2)


print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(emp_2.fullname())
print(emp_1.empBonus())
print(emp_2.empBonus())