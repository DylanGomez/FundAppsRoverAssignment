import unittest
from Rover import *

class TestUM(unittest.TestCase):

    def test_setUp(self):
        pass


    # Test 1

    # def test_checkForForwardMovement(self):
    #     self.assertEqual(moveForward("F", 0, 0, "North"), (1, 0, "North"))

    # Test 2

    # def test_checkMovementInTwoDirections(self):
    #     self.assertEqual(moveForwardInTwoDirections("FFFFRFFF", 0, 0, "North"), (4, 3, "East"))

    # Test 3

    # def test_checkIfBorderMovementIsIgnored(self):
    #     self.assertEqual(checkForBorders("BRFFR", 0, 0, "North"), (0, 2, "East"))

    #Test 4

    # def test_checkForBackwardsMovement(self):
    #     self.assertEqual(newBackwarsMovement("FFFBB", 0, 0, "North"), (1, 0, "North"))

    # Test 5

    def test_checkIfRoverHitsAnObstacle(self):
        self.assertEqual(movementForRoverWithObstacles("FF", 0, 0, "North"), (1,0, "North"))

    def test_obstacleHitTest(self):
        self.assertTrue(checkForObstacle(2, 0))

if __name__ == '__main__':
    unittest.main()
