import unittest
import sys
#needed paths
sys.path.append("../")
import diction
import word_bank


class Test_Diction(unittest.TestCase):

    def test_Units(self):
        #Test
        print("Testing for empty bank.")
        diction.initBank()
        self.assertEqual(len(diction.words), 0)
        
        #Test
        print("Testing for non-empty bank after initialization.")
        diction.getWordBank("../word_bank/")
        self.assertNotEqual(len(diction.words), 0)
    

        #Test
        print("Test getRandomWordFunctions")
        diction.getWordBank("../word_bank/")
        test_word = diction.pickRandomWord()
        self.assertIn(test_word, diction.words)

        
    

if __name__ == "__main__":
    unittest.main()
