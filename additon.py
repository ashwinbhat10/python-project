import os
import unittest

def addition (a,b) :
    return a+b

class test_addition(unittest.TestCase) :

    def test_add(self):
        self.assertEqual(5,addition(2,3))



if __name__ == '__main__' :
   print "testing"
   unittest.main()



