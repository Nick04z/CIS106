#Nicholas Rodriguez - 3/5/2026 - PS9P2
#Function
def calcRoomSqFt(roomLength, roomWidth, roomHeight):
    roomSqFt = (2 * roomLength * roomWidth) + (2 * roomLength * roomHeight) + (2 * roomWidth * roomHeight)
    return roomSqFt
#Main
    #input
response = input("Ready to see how much paint you need to paint your room? (Yes or No): ")
    #process
while response == "Yes":
    roomLength = float(input("Enter the Length of the room: "))
    roomWidth = float(input("Enter the Width of the room: "))
    roomHeight = float(input("Enter the Height of the room: "))
    roomSqFt = calcRoomSqFt(roomLength, roomWidth, roomHeight)

    paintGallons = roomSqFt / 50
    print(paintGallons, "gallons of paint are needed to paint this room")
    response = input("Do the calculation again? (Yes or No): ")
print("Happy Painting!")