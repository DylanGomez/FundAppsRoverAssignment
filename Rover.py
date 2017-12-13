from random import randint
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
# Test does succeed, so yay for now.

# for letter in command:
#     if(letter == "F" and facingDirection == "North"):
#         xAxis += 1
#     elif(letter == "R" and facingDirection == "North"):
#         facingDirection = "East"
#     elif(letter == "F" and facingDirection == "East"):
#         yAxis += 1
#     elif (letter == "F" and facingDirection == "South"):
#         xAxis -= 1
#     elif (letter == "F" and facingDirection == "East"):
#         yAxis -= 1
#
#
# print("Rover is at position:", xAxis, ",", yAxis ,"facing", facingDirection )
#

"""
    Test 4: check where the borders are in the grid and check if code continues correctly
    
    Input: BRFFR
    
    Output: "Oops, you can't go here, you are set back to your previous location"
    Output: Rover is at position 0 , 2 facing East
    
"""

# for letter in command:
#
#     if(letter == "B" and xAxis == 0 or letter == "F" and xAxis == 100):
#         print("Oops, you can't go here, you are set back to your previous location")
#
#     else:
#         if(letter == "F" and facingDirection == "North"):
#             xAxis += 1
#
#         elif(letter == "R" and facingDirection == "North"):
#             facingDirection = "East"
#
#         elif(letter == "F" and facingDirection == "East"):
#             yAxis += 1
#
#         elif (letter == "F" and facingDirection == "South"):
#             xAxis -= 1
#
#         elif (letter == "F" and facingDirection == "East"):
#             yAxis -= 1
#
# print("Rover is at position:", xAxis, ",", yAxis ,"facing", facingDirection)


"""
    Test 5: Add command "B" to movement of rover

    Input: FFFBB

    Output: Rover is at position 0 , 1 facing North

"""
for letter in command:


    if (letter == "B" and xAxis == 0 or letter == "F" and xAxis == 100):
        print("Oops, you can't go here, you are set back to your previous location")
    elif():
        print("")
    else:
        # Movement with command F
        if (letter == "F" and facingDirection == "North"):
            xAxis += 1
        elif (letter == "F" and facingDirection == "East"):
            yAxis += 1

        elif (letter == "F" and facingDirection == "South"):
            xAxis -= 1

        elif (letter == "F" and facingDirection == "East"):
            yAxis -= 1

        # Movement with command B
        elif (letter == "B" and facingDirection == "North"):
            xAxis -= 1
        elif (letter == "F" and facingDirection == "East"):
            yAxis -= 1

        elif (letter == "F" and facingDirection == "South"):
            xAxis += 1

        elif (letter == "F" and facingDirection == "East"):
            yAxis += 1

        # Changing directions with command: R
        elif (letter == "R" and facingDirection == "North"):
            facingDirection = "East"
        elif (letter == "R" and facingDirection == "East"):
            facingDirection = "South"
        elif (letter == "R" and facingDirection == "South"):
            facingDirection = "West"
        elif (letter == "R" and facingDirection == "West"):
            facingDirection = "North"

        # Changing directions with command: L
        elif (letter == "L" and facingDirection == "North"):
            facingDirection = "West"
        elif (letter == "R" and facingDirection == "East"):
            facingDirection = "North"
        elif (letter == "R" and facingDirection == "South"):
            facingDirection = "East"
        elif (letter == "R" and facingDirection == "West"):
            facingDirection = "South"



print("Rover is at position:", xAxis, ",", yAxis, "facing", facingDirection)





""" 
    Test 6: Add obstacles and detect them
    
    Input: FFFFRFFF
    
    Output: "Obstacle detected moving back to previous position"

"""

#Making obstacles
obstacleXAxis = []
obstacleYAxis = []

# Max amount of obstacles
amountObstacles = randint(0, 10)

for i in range (0, amountObstacles):
    # Location of the obstacles
    # Check if I is uneven or even to spread the obstacles around the grid
    # In future iteration this can get changed.

    if(i % 2 == 0):
        obstacleXAxis.append(randint(0,10))
    else:
        obstacleYAxis.append(randint(0,10))

#Check every command that is given

for letter in command:


    if (letter == "B" and xAxis == 0 or letter == "F" and xAxis == 100):
        print("Oops, you can't go here, you are set back to your previous location")
    elif():
        print("")
    else:
        # Movement with command F
        if (letter == "F" and facingDirection == "North"):
            xAxis += 1
        elif (letter == "F" and facingDirection == "East"):
            yAxis += 1

        elif (letter == "F" and facingDirection == "South"):
            xAxis -= 1

        elif (letter == "F" and facingDirection == "East"):
            yAxis -= 1

        # Movement with command B
        elif (letter == "B" and facingDirection == "North"):
            xAxis -= 1
        elif (letter == "F" and facingDirection == "East"):
            yAxis -= 1

        elif (letter == "F" and facingDirection == "South"):
            xAxis += 1

        elif (letter == "F" and facingDirection == "East"):
            yAxis += 1

        # Changing directions with command: R
        elif (letter == "R" and facingDirection == "North"):
            facingDirection = "East"
        elif (letter == "R" and facingDirection == "East"):
            facingDirection = "South"
        elif (letter == "R" and facingDirection == "South"):
            facingDirection = "West"
        elif (letter == "R" and facingDirection == "West"):
            facingDirection = "North"

        # Changing directions with command: L
        elif (letter == "L" and facingDirection == "North"):
            facingDirection = "West"
        elif (letter == "R" and facingDirection == "East"):
            facingDirection = "North"
        elif (letter == "R" and facingDirection == "South"):
            facingDirection = "East"
        elif (letter == "R" and facingDirection == "West"):
            facingDirection = "South"



print("Rover is at position:", xAxis, ",", yAxis, "facing", facingDirection)







