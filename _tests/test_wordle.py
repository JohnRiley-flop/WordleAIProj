import unittest
import sys
#needed paths
sys.path.append("../")
import wordle


class Test_Diction(unittest.TestCase):
    def testEnv(self):
        print("hi")