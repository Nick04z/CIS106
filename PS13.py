#Nicholas Rodriguez - 4/15/2026 - PS13
#P1
def getFirstList(firstList):
    numberOfItems = int(input("Number of items for your list: "))
    for numberOfItems in range(0,numberOfItems,1):
        integer = int(input("Enter an Integer: "))
        firstList.append(integer)
    return firstList

def displayFirstList(firstList):
    for item in firstList:
        print(item)
    return

#Main
firstList = []
firstList = getFirstList(firstList)
displayFirstList(firstList)

#P2
firstList.insert(1, 99)
print(firstList)

#P3
firstList[1] = 100
print(firstList)

#P4
secondList = [500, 600, 700, 800, 900]
print(secondList)
firstList.extend(secondList)
print(firstList)

#P5
firstList.remove(800)
print(firstList)

#P6
firstList.remove(firstList[2])
print(firstList)

#P7
gradeList = ["A", "B", "C", "A", "A", "C", "B", "F", "F"]
print("Grades:", gradeList)

#P8
gradeCountA = 0
for y in range(len(gradeList)):
    if gradeList[y] == "A":
        gradeCountA += 1
print("Number of A grades:", gradeCountA)

#P9
Bindex = -1
for x in range(len(gradeList)):
    if gradeList[x] == "B":
        Bindex = x
        break
if Bindex == -1:
    print("No B grade was found")
else: print("Index of first B grade:", Bindex)

#P10
Findex = -1
Fcount = 0
for f in range(len(gradeList)):
    if gradeList[f] == "F":
        Findex = f 
        Fcount += 1
    
if Findex == -1:
    print("An F grade was not found")
else: print(Fcount, "F grades were found")

#P11
secondList.clear()
print(secondList)

#P12
#del secondList
#print(secondList)

#P13
playerList = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

#P14
playerList.sort()
print(playerList)

#P15
playerList2 = playerList.copy()
print(playerList2)

#P16
playerList2.sort(reverse=True)
print("Player List 1:", playerList)
print("Player List 2:", playerList2)

