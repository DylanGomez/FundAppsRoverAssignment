from random import randint

# Generally used variables
startYAxis = 0
startXAxis = 0
facingDirection = "North"

command = input("What does the Rover need to do?: ").upper()

"""
    Test 1: Rover moves forward 1 step to show it will move

    Input: FR

    Output: Rover is at position: 1,0 facing East
    
    Unit test: test_moveForward
    expected return result: 1, 0, "North"
    
    Test Succeeded on: 14-12-2017
 
"""

def moveForward(commandInput, placeY, placeX, currentDirection):

    for letter in commandInput:
        if(letter == "F"):
            placeY += 1
        elif(letter == "R" and currentDirection == "North"):
            currentDirection = "East"


    print('Rover is at position:', placeY, placeX ,'facing', currentDirection)

    result = placeY, placeX, currentDirection
    return result

# moveForward(command, yAxis, xAxis, facingDirection)

"""
    Test 2: Rover moves 4 forward and 3 steps East
    
    Input: FFFFRFFF
    
    Output: Rover is at position 4, 3 facing East
    
    Unit test: test_checkMovementInTwoDirections
    expected return result: 4, 3, "East"
    
    Test Succeeded on: 14-12-2017
    
"""
# Is getting a bit crazy with every elif, need to find better fix next test/ iteration
# Test does succeed, so yay for now.
def moveForwardInTwoDirections(commandInput, placeY, placeX, currentDirection):

    for letter in commandInput:
        if(letter == "F" and currentDirection == "North"):
            placeY += 1
        elif(letter == "R" and currentDirection == "North"):
            currentDirection = "East"
        elif(letter == "F" and currentDirection == "East"):
            placeX += 1
        elif (letter == "F" and currentDirection == "South"):
            placeY -= 1
        elif (letter == "F" and currentDirection == "West"):
            placeX -= 1


    print('Rover is at position:', placeY, placeX ,'facing', currentDirection)
    result = placeY, placeX, currentDirection
    return result

"""
    Test 3: check where the borders are in the grid and check if code continues correctly
    
    Input: BRFFR
    
    Output: "Oops, you can't go here, you are set back to your previous location"
    Output: Rover is at position 0 , 2 facing East
    
    Unit test name: test_checkIfBorderMovementIsIgnored()
    expected output: 0, 2, "East"
    

        Test Succeeded on: 14-12-2017
    
"""
def checkForBorders(commandInput, placeY, placeX, currentDirection):

    for letter in commandInput:

        if(letter == "B" and placeY == 0 or letter == "F" and placeX == 100):
            print("Oops, you can't go here, you are set back to your previous location")

        else:
            if(letter == "F" and currentDirection == "North"):
                placeY += 1

            elif(letter == "R" and currentDirection == "North"):
                currentDirection = "East"

            elif(letter == "F" and currentDirection == "East"):
                placeX += 1

            elif (letter == "F" and currentDirection == "South"):
                placeY -= 1

            elif (letter == "F" and currentDirection == "West"):
                placeY -= 1

    print("Rover is at position:", placeY, ",", placeX ,"facing", currentDirection)
    result = placeY, placeX, currentDirection
    return result

"""
    Test 4: Add command "B" to movement of rover

    Input: FFFBB

    Output: Rover is at position 1 , 0 facing North
    
    Unit test name: test_checkForBackwardsMovement()
    expected output for unit test: 1, 0, "North"
    
    test succeeded: 14-12-2017

"""
def newBackwardsMovement(commandInput, placeY, placeX, currentDirection):

    for letter in commandInput:


        if (letter == "B" and placeY == 0 or letter == "F" and placeY == 100):
            print("Oops, you can't go here, you are set back to your previous location")
        else:
            # Movement with command F
            if (letter == "F" and currentDirection == "North"):
                placeY += 1
            elif (letter == "F" and currentDirection == "East"):
                placeX += 1

            elif (letter == "F" and currentDirection == "South"):
                placeY -= 1

            elif (letter == "F" and currentDirection == "West"):
                placeX -= 1

            # Movement with command B
            elif (letter == "B" and currentDirection == "North"):
                placeY -= 1
            elif (letter == "B" and currentDirection == "East"):
                placeX -= 1

            elif (letter == "B" and currentDirection == "South"):
                placeY += 1

            elif (letter == "B" and currentDirection == "West"):
                placeX += 1

            # Changing directions with command: R
            elif (letter == "R" and currentDirection == "North"):
                currentDirection = "East"
            elif (letter == "R" and currentDirection == "East"):
                currentDirection = "South"
            elif (letter == "R" and currentDirection == "South"):
                currentDirection = "West"
            elif (letter == "R" and currentDirection == "West"):
                currentDirection = "North"

            # Changing directions with command: L
            elif (letter == "L" and currentDirection == "North"):
                currentDirection = "West"
            elif (letter == "R" and currentDirection == "East"):
                currentDirection = "North"
            elif (letter == "R" and currentDirection == "South"):
                currentDirection = "East"
            elif (letter == "R" and currentDirection == "West"):
                currentDirection = "South"

    print("Rover is at position:", placeY, ",", placeX, "facing", currentDirection)
    result = placeY, placeX, currentDirection
    return result


""" 
    Test 5: Add obstacles and detect them
    
    Input: FF
    
    Output: "Obstacle detected moving back to previous position"
    
    Unit test name: test_checkIfRoverHitsAnObstacle() and test_obstacleHitTest()
    
    Expected output: 1,0 "North"
    
    For the test there has been put an obstacle on 2,0 
    
    test succeeded: 14-12-2017

"""

#Making obstacles
obstacleYAxis = [2, 5, 6]
obstacleXAxis = [0, 3, 9]

#Adding random obstacles to the grid
amountObstacles = randint(0,100)

# Location of the obstacles
# Check if i is uneven or even to spread the obstacles around the grid
#  In future iteration this can get changed.
#  Currently not used since it is really annoying for consistent testing

def addingObstaclesToGridRandomized():

    for i in range (0, amountObstacles):

        if(i % 2 == 0):
            obstacleXAxis.append(randint(0,100))
        else:
            obstacleYAxis.append(randint(0,100))

# This method checks if there is an obstacle on the given position
# If so, it returns true so that the other part of the code knows that an obstacle has been discovered.

def checkForObstacle(positionY, positionX):

    if(positionY in obstacleYAxis and positionX in obstacleXAxis):
        print("Obstacle discovered, Going back to previous location")
        return True
    else:
        return False

#Check every command that is given
def movementForRoverWithObstacles(commandInput, placeY, placeX, currentDirection):

    for letter in commandInput:
        #TODO this fix will not work for every side of the grid fixing in test 6
        if (letter == "B" and placeY == 0 or letter == "F" and placeY == 100):
            print("Oops, you can't go here, you are set back to your previous location")
        else:
            # Movement with command F
            if (letter == "F"):
                if(currentDirection == "North"):
                    placeY += 1
                    if(checkForObstacle(placeY, placeX)):
                        placeY -= 1
                elif (currentDirection == "East"):
                    placeX += 1
                    if (checkForObstacle(placeY, placeX)):
                        placeX -= 1
                elif (currentDirection == "South"):
                    placeY -= 1
                    if (checkForObstacle(placeY, placeX)):
                        placeY +=1
                elif (currentDirection == "West"):
                    placeX -= 1
                    if (checkForObstacle(placeY, placeX)):
                        placeX += 1

            # Movement with command B
            elif (letter == "B"):
                if (currentDirection == "North"):
                    placeY -= 1
                    if (checkForObstacle(placeY, placeX)):
                        placeY -= 1
                elif (currentDirection == "East"):
                    placeX -= 1
                    if (checkForObstacle(placeY, placeX)):
                        placeX -=1
                elif (currentDirection == "South"):
                    placeY += 1
                    if (checkForObstacle(placeY, placeX)):
                        placeY -=1
                elif (currentDirection == "West"):
                    placeX += 1
                    if (checkForObstacle(placeY, placeX)):
                        placeX += 1


            # Changing directions with command: R
            elif (letter == "R"):
                if(currentDirection == "North"):
                    currentDirection = "East"
                elif ( currentDirection == "East"):
                    currentDirection = "South"
                elif (currentDirection == "South"):
                    currentDirection = "West"
                elif (currentDirection == "West"):
                    currentDirection = "North"

            # Changing directions with command: L
            elif (letter == "L"):
                if(currentDirection == "North"):
                    currentDirection = "West"
                elif (currentDirection == "East"):
                    currentDirection = "North"
                elif (currentDirection == "South"):
                    currentDirection = "East"
                elif (currentDirection == "West"):
                    currentDirection = "South"


    print("Rover is at position:", placeY, ",", placeX, "facing", currentDirection)
    result = placeY, placeX, currentDirection
    return result



""" 
    Test 5: Making all borders collidable

    Input: FLF

    Output in console: "Border detected, going back"

    Unit test name: test_checkIfRoverHitsAnObstacle() and test_obstacleHitTest()

    Expected output: 1,0 "North"

    For the test there has been put an obstacle on 2,0 
    
    test succeeded: 14-12-2017
"""


#Making obstacles
obstacleYAxis = [2, 5, 6]
obstacleXAxis = [0, 3, 9]

#Adding random obstacles to the grid
amountObstacles = randint(0,100)

# Location of the obstacles
# Check if i is uneven or even to spread the obstacles around the grid
#  In future iteration this can get changed.
#  Currently not used since it is really annoying for consistent testing

def addingObstaclesToGridRandomized():

    for i in range (0, amountObstacles):

        if(i % 2 == 0):
            obstacleXAxis.append(randint(0,100))
        else:
            obstacleYAxis.append(randint(0,100))

# This method checks if there is an obstacle on the given position
# If so, it returns true so that the other part of the code knows that an obstacle has been discovered.
#Added grid detection to obstacle detection
def checkForObstacleOrEdge(positionY, positionX):

    if(positionY in obstacleYAxis and positionX in obstacleXAxis):
        print("Obstacle discovered, Going back to previous location")
        return True
    elif(positionY == 101 or positionY  == -1  or positionX == 101 or positionX == -1 ):
        print("Border detected, going back to previous location")
        return True
    else:
        return False


#Check every command that is given
def movementForRoverWithBorderCheck(commandInput, placeY, placeX, currentDirection):
    for letter in commandInput:
        # Movement with command F
        if (letter == "F"):
            if(currentDirection == "North"):
                placeY += 1
                if(checkForObstacleOrEdge(placeY, placeX) ):
                    placeY -= 1
            elif (currentDirection == "East"):
                placeX += 1
                if (checkForObstacleOrEdge(placeY, placeX)):
                    placeX -= 1
            elif (currentDirection == "South"):
                placeY -= 1
                if (checkForObstacleOrEdge(placeY, placeX)):
                    placeY +=1
            elif (currentDirection == "East"):
                placeX -= 1
                if (checkForObstacleOrEdge(placeY, placeX)):
                    placeX += 1


        # Movement with command B
        elif (letter == "B"):
            if (currentDirection == "North"):
                placeY -= 1
                if (checkForObstacleOrEdge(placeY, placeX)):
                    placeY += 1
            elif (currentDirection == "East"):
                placeX -= 1
                if (checkForObstacleOrEdge(placeY, placeX)):
                    placeX +=1
            elif (currentDirection == "South"):
                placeY += 1
                if (checkForObstacleOrEdge(placeY, placeX)):
                    placeY -=1
            elif (currentDirection == "West"):
                placeX += 1
                if (checkForObstacleOrEdge(placeY, placeX)):
                    placeX += 1

        # Changing directions with command: R

        elif (letter == "R"):
            if(currentDirection == "North"):
                currentDirection = "East"
            elif ( currentDirection == "East"):
                currentDirection = "South"
            elif (currentDirection == "South"):
                currentDirection = "West"
            elif (currentDirection == "West"):
                currentDirection = "North"

        # Changing directions with command: L

        elif (letter == "L"):
            if(currentDirection == "North"):
                currentDirection = "West"
            elif (currentDirection == "East"):
                currentDirection = "North"
            elif (currentDirection == "South"):
                currentDirection = "East"
            elif (currentDirection == "West"):
                currentDirection = "South"


    print("Rover is at position:", placeY, ",", placeX, "facing", currentDirection)
    result = placeY, placeX, currentDirection
    return result
