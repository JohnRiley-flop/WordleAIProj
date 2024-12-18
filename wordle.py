import diction

import WordleBot

#Gets word guess and makes sure it is in the list of acceptable words.
def promptForWord() -> str:
    acceptedWord = "*****"
    bank = diction.getWordBank()
    while not (acceptedWord in bank):
        acceptedWord = input("Please enter a valid word: ")
    return acceptedWord

#
def checkForMatch(guess: str, real: str) -> bool:
    if guess.lower() == real.lower():
        return True
    return False

#Provides a hint based on the input and the answer.
def hintString(guess: str, real: str) -> str:
    guessChars = list(guess)
    realChars = list(real)
    hintStr = ["-", "-", "-", "-", "-"]
    #check for direct matches
    for i in range(len(guessChars)):
        if guessChars[i] == realChars[i]:
            hintStr[i] = guessChars[i]
        elif guessChars[i] in realChars:
            hintStr[i] = "*"
            realChars[realChars.index(guessChars[i])] = None
    
    hintStr = ''.join(hintStr)
    return hintStr

#Method to play a round of wordle. Returns the number of points gotten from a round, with points being equal to [6 - guesses].
def playRound() -> int:
    ans = diction.pickRandomWord()
    #print("Psst! Word is ... " + ans)
    print("Wordle sim started! Have fun!")
    guessed = False
    wordGuesses = 0
    hints = []
    while not guessed and wordGuesses < 6:
        print("Guesses remaining: " + str(6 - wordGuesses))
        newGuess = promptForWord()
        #AI makes guess
        guessed = checkForMatch(newGuess, ans)
        hints.append([hintString(newGuess, ans), newGuess])
        for hint in hints:
            print(hint[0] + " : " + hint[1])
        wordGuesses += 1

    score = 6 - (wordGuesses + 1)
    if score > 0:
        print("Solved! It took " + str(wordGuesses) + " guess(es)!")
    else:
        print("Ooh, better luck next time! The word was: " + str(ans))

    return score
    



if __name__ == "__main__":
    
    #numGames = int(input("How many games should the AI play? "))
    numGames = 1
    for i in range(numGames):
        playRound()