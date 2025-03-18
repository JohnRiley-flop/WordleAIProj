#code for wordle ai to play games and update game data based on performance.
#The AI uses Q reinforcement learning to become good at the game.
import random
import json
import diction
import os


class WordleBot():
    def __init__(self):
        self.data_folder = 'ai_game_data/'
        self.qTable = dict()
        self.loadTable()

    #Training variables
    learningRate = 0.3
    futureChoiceDiscount = 0.9
    explorationRate = 0.2
    #List of words to work with
    wordOptions = diction.getWordBank("word_bank/")
    def getRandomWord(self) -> str:
        return self.wordOptions[random.randint(0, len(self.wordOptions) - 1)]
    
    guessedWords = []
    def clearGuesses(self):
        self.guessedWords = []

    #QTable operations
    def saveTable(self):
        for state in self.qTable:
            filename = self.data_folder + state + ".json"
            with open(filename, 'w') as state_table:
                json.dump(self.qTable[state], state_table)

    def loadTable(self) -> dict:
        for file in os.listdir(self.data_folder):
            state = file.replace(".json", "")
            with open((self.data_folder + file), 'r') as state_table:
                self.qTable[state] = json.load(state_table)        

    #Python QTable operations
    def updateTable(self, state, action, reward, nextState):
        if state not in self.qTable:
            self.qTable[state] = {word: 0.0 for word in self.wordOptions}
        if nextState not in self.qTable:
            self.qTable[nextState] = {word: 0.0 for word in self.wordOptions}
        bestNextAction = max(self.qTable[state], key=self.qTable[nextState].get)
        self.qTable[state][action] = (self.qTable[state][action] + self.learningRate * (reward + self.futureChoiceDiscount * self.qTable[nextState][bestNextAction] - self.qTable[state][action]))

    def bestNextGuess(self, state) -> str:
        if state not in self.qTable:
            return self.getRandomWord()
        highVal = max(self.qTable[state], key=self.qTable[state].get)
        if highVal in self.guessedWords:
            return self.getRandomWord()
        else:
            return highVal
        

    #Gameplay operations
    def guessWord(self, currState) -> str:
        guess = ""
        if random.uniform(0,1) > self.explorationRate:
            guess = self.bestNextGuess(currState)
        else:
            guess = self.getRandomWord()
        self.guessedWords.append(guess)
        return guess
           