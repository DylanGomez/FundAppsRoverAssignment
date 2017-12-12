"""
    Test 1: Rover moves forward 1 step to show it will move

    Input: FR

    Output: Rover is at position: 1,0 facing East
"""

xAxis = 0
yAxis = 0
facingDirection = "North"

command = input("What does the Rover need to do?: ")

for letter in command:
    if(letter == "F"):
        xAxis += 1
    elif(letter == "R" and facingDirection == "North"):
        facingDirection = "East"


print("Rover is at position:", xAxis, ",", yAxis ,"facing", facingDirection )