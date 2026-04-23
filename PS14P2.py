#Nicholas Rodriguez - 4/23/2026 - P14P2
#Class/Functions
class Student:
    def __init__(self, first, last, code, credits):
        self.first = first
        self.last = last
        self.code = code
        self.credits = credits

    def fullName(self):
        return "{} {}".format(self.first, self.last)
    
    def tuitionCalc(self):
        if self.code == "I":
            return 250.00 * self.credits
        else: return 500.00 * self.credits
#Main

student1 = Student('Nicholas', 'Rodriguez', 'I', 12)
student2 = Student('Harsh', 'Desai', "O", 15)

print("Full Name:", student1.fullName())
print("District Code:", student1.code)
print("Credits:", student1.credits)
print("Tuition:$", student1.tuitionCalc())

print("\n")

print("Full Name:", student2.fullName())
print("District Code:", student2.code)
print("Credits:", student2.credits)
print("Tuition:$", student2.tuitionCalc())
