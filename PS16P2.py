#Nicholas Rodriguez - 4/30/2026 - PS16P2
#Class
class Car:
    def __init__(self, make, model, stickPrice):
        self.make = make
        self.model = model
        self.stickPrice = stickPrice
        self.discPrice = stickPrice * .90
        self.price = stickPrice - self.discPrice

class Sport(Car):
    def __init__(self, make, model, stickPrice, wheel, engine, interior):
        super().__init__(make, model, stickPrice)
        self.wheel = wheel
        self.engine = engine
        self.interior = interior
    
    def option1(self): 
        if self.wheel == "Y":
            wheelPrice = 1000.00
        else: wheelPrice = 0
        return wheelPrice

    def option2(self):
        if self.engine == "Y":
            enginePrice = 3000.00
        else: enginePrice = 0
        return enginePrice
        
    def option3(self):
        if self.interior == "Y":
            interiorPrice = 2000.00
        else: interiorPrice = 0
        return interiorPrice

    def priceWithOptions(self):
        return (self.price) + self.option1() + self.option2() + self.option3()
    

class Luxury(Car):
    def __init__(self, make, model, stickPrice, gps, selfDrive):
        super().__init__(make, model, stickPrice, )
        self.gps = gps
        self.selfDrive = selfDrive

    def option1(self):
        if self.gps == "Y":
            gpsPrice = 5000.00
        else: gpsPrice = 0
        return gpsPrice
    
    def option2(self):
        if self.selfDrive == "Y":
            selfDrivePrice = 10000.00
        else: selfDrivePrice = 0
        return selfDrivePrice
    
    def option3(self):
        return 0
    
    def priceWithOptions(self):
        return (self.price) + self.option1() + self.option2()
    
       



#Main
car_1 = Sport('Honda', 'Civic', 25000, 'Y', 'N', 'N')
car_2 = Luxury('Toyota', 'SUV', 67000, 'N', 'Y')
car_3 = Car('Lexus', 'NT', 45000)


print(car_3.make)
print(car_3.model)
print("Sticker Price:$", car_3.stickPrice)
print("Discount Price:$", car_3.discPrice)
print("Final Price:$", car_3.price)
print("\n")
print(car_1.make)
print(car_1.model)
print("Sticker Price:$", car_1.stickPrice)
print("Discount Price:$", car_1.discPrice)
print(" Wheels:$", car_1.option1(),"\n", "Engine:$", car_1.option2(), "\n", "Interior:$", car_1.option3())
print("Final Price:$", car_1.priceWithOptions())
print("\n")
print(car_2.make)
print(car_2.model)
print("Sticker Price:$", car_2.stickPrice)
print("Discount Price:$", car_2.discPrice)
print(" GPS:$", car_2.option1(), "\n", "Self-Driving:$", car_2.option2())
print("Final Price:$", car_2.priceWithOptions())