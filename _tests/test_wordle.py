import unittest
import sys
#needed paths
sys.path.append("../")
sys.path.append("../word_bank")
import wordle
import diction

class Test_Wordle(unittest.TestCase):
    def testWordComparison(self):
        #Test
        print("Testing match check functionality.")
        word1 = "wired"
        word2 = word1
        self.assertEqual(wordle.checkForMatch(word1, word2), True)

        #Test
        print("Testing correctness of mismatch catching.")
        word1 = "wires"
        self.assertEqual(wordle.checkForMatch(word1, word2), False)


if __name__ == "__main__":
    unittest.main()