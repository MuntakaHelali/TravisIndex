import unittest

import myFunctions

class TestMyFunc(unittest.TestCase):

    def setUp(self):
        pass

    def testSquareFunc_1(self):
        self.assertEqual( myFunctions.sqaureFunc(-2), 4)
   
    def testSquareFunc_2(self):
        self.assertEqual( myFunctions.sqaureFunc(9), 81)

    def testAddFour1(self):
        self.assertEqual( myFunctions.addFour(400), 404)
        
    def testAddFour2(self):
        self.assertEqual( myFunctions.addFour(0), 4)
        
    def testStrLen1(self):
        self.assertEqual( myFunctions.stringLen("Test"), 4)
    
    def testStrLen2(self):
        self.assertEqual( myFunctions.stringLen("Function !"), 10)     

    def testStrLen3(self):
        self.assertEqual( myFunctions.stringLen("Update "), 7)          

if __name__ == '__main__':
    unittest.main()