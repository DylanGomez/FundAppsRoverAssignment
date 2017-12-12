"""
    Test 1: Rover moves forward 1 step to show it will move

    Input: FR

    Output: Rover is at position: 1,0 facing East
"""
xAxis = 0
yAxis = 0
facingDirection = "North"

command = input("What does the Rover need to do?: ")
#
# for letter in command:
#     if(letter == "F"):
#         xAxis += 1
#     elif(letter == "R" and facingDirection == "North"):
#         facingDirection = "East"
#
#
# print("Rover is at position:", xAxis, ",", yAxis ,"facing", facingDirection )
#


"""
    Test 2: Rover moves 4 forward and 3 steps East
    
    Input: FFFFRFFF
    
    Output: Rover is at position 4, 3 facing East
    
"""
# Is getting a bit crazy with every elif, need to find better fix next test/ iteration
for letter in command:
    if(letter == "F" and facingDirection == "North"):
        xAxis += 1
    elif(letter == "R" and facingDirection == "North"):
        facingDirection = "East"
    elif(letter == "F" and facingDirection == "East"):
        yAxis += 1
    elif (letter == "F" and facingDirection == "South"):
        xAxis -= 1
    elif (letter == "F" and facingDirection == "East"):
        yAxis -= 1


print("Rover is at position:", xAxis, ",", yAxis ,"facing", facingDirection )





