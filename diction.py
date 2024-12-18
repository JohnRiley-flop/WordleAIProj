#file to get word bank and accepted guesses
import random
import os
from typing import List

words = []

def initBank():
    dir = 'word_bank/'
    for rfile in os.listdir(dir):
        wordSource = 'word_bank/' + rfile
        file = open(wordSource, 'r')
        fileContent = file.read()
        for word in fileContent.split('\n'):
            words.append(word)
            words.sort()



def pickRandomWord() -> str:
    if len(words) == 0:
        initBank()
    range = len(words) - 1
    return words[random.randint(0, range)]

def getWordBank() -> List[str]:
    if len(words) == 0:
        initBank()
    return words