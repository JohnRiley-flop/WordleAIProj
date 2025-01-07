#code for wordle ai to play games and update game data based on performance.
#The AI uses Q reinforcement learning to become good at the game.
import random
import json
import diction

class WordleBot():
    def __init__(self):
        self.data_file = 'ai_game_data.json'
        self.qTable = self.loadTable()

    #Training variables
    learningRate = 0.2
    futureChoiceDiscount = 0.9
    explorationRate = 0.2
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
    
    def updateTable(self, state, action, reward, nextState):
        if state not in self.qTable:
            self.qTable[state] = {word: 0.0 for word in self.wordOptions}
        if nextState not in self.qTable:
            self.qTable[nextState] = {word: 0.0 for word in self.wordOptions}
        bestNextAction = max(self.qTable[state], key=self.qTable[nextState].get)
        self.qTable[state][action] = (self.qTable[state][action] + self.learningRate * (reward + self.futureChoiceDiscount * self.qTable[nextState][bestNextAction] - self.qTable[state][action]))

    def bestNextGuess(self, state) -> str:
        return max(self.qTable[state], key=self.qTable[state].get)
        

    #Gameplay operations
    def guessWord(self, currState) -> str:
        if random.uniform(0,1) > self.explorationRate:
            return self.bestNextGuess(currState)
        else:
            return self.wordOptions[random.randint(0, len(self.wordOptions) - 1)]

           