#Nicholas Rodriguez - 2/12/2026 - PS6P3

#input
response = input("Do you want to use this program? (Yes or No) ")

#process - Before Loop:
stuCount = 0 
#process - Loop:
while response == "Yes":
    lastName = input("Enter student's Last Name: ")
    examScore1 = float(input("Enter their First Exam Score: "))
    examScore2 = float(input("Enter their Second Exam Score: "))
    avgScore = (examScore1 + examScore2) / 2
    print("Student Last Name: ", lastName)
    print("Average Score: ", avgScore)
    stuCount += 1
    response = input("Do you want to use this program again? (Yes or No) ")

print("Number of Students who entered data: ", stuCount)
