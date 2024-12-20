#code for wordle ai to play games and update game data based on performance.
#The AI uses Q reinforcement learning to become good at the game.
import random
import json
import diction

class WordleBot():
    def __init__(self):
        self.qTable = self.loadTable()
        self.data_file = 'ai_game_data.json'

    #Training variables
    learningRate = 0.1
    futureChoiceDiscount = 0.9
    explorationRate = 0.1
    #List of words to work with
    wordOptions = diction.getWordBank()

    #QTable operations
    def saveTable(self):
        with open(self.data_file, 'w') as table:
            json.dump(self.qTable, table)
    
    def loadTable(self) -> dict:
        with open(self.data_file, 'r') as table:
            q = json.load(table)
        return q
    
    def updateTable():#state, action, reward, nextState):
        print('e')