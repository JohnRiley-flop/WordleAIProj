#file to get word bank and accepted guesses
import random
import os
from typing import List

words = []

def initBank():
    words = []



def pickRandomWord() -> str:
    if len(words) == 0:
        initBank()
    range = len(words) - 1
    return words[random.randint(0, range)]

def getWordBank(bank_folder) -> List[str]:
    if len(words) == 0:
        for rfile in os.listdir(bank_folder):
            wordSource = bank_folder + rfile
            file = open(wordSource, 'r')
            fileContent = file.read()
            for word in fileContent.split('\n'):
                words.append(word)
            file.close()
    return words