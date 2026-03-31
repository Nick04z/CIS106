#Nicholas Rodriguez - 3/19/2026 - PS11P1
#Resources: https://www.w3schools.com/python/default.asp; https://www.geeksforgeeks.org/python/python-check-for-spaces-in-string/; 

#Functions
def inputFunction():
    fullName = input("Enter your full name: ")
    return fullName

def cutNameFunc(fullName):
    cutName = fullName.strip()
    return cutName

def splitFunction(cutName):
    firstName, lastName = fullName.split()
    return firstName, lastName   

def errorCheck1(fullName):
    wSpace = " " in fullName
    if wSpace == False:
        raise Exception("There was no spaces in the name, Please try again")
    
    return


def errorCheck2(firstName, lastName):
    if len(firstName) < 2  or len(lastName) < 2:
        raise Exception("Full Name not entered, please try again")
    return
   


#Main
fullName = inputFunction()
errorCheck1(fullName)
cutName = cutNameFunc(fullName)
firstName, lastName = splitFunction(cutName)
errorCheck2(firstName, lastName)
print(lastName.capitalize() + ",", firstName[0].capitalize() + ".")
