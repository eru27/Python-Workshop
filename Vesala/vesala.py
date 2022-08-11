import random

LIVES = 5

WORDS = "reci.txt"

def loadWords():
    with open(WORDS, 'r') as file:
        words = file.readlines() # Imaju \n na kraju

    wordsFixed = [] # Bez \n
    for word in words:
        wordsFixed.append(word.replace('\n', ''))
    
    return wordsFixed

def printStatus(word, goodLetters, badLetters, currentLives):
    for letter in word:
        if letter in goodLetters:
            print(letter, end = ' ')
        else:
            print('_', end = ' ')
    
    print()
    print("Pogodjena slova: ", goodLetters)
    print("Promasena slova: ", badLetters)
    print("Broj preostalih zivota: ", currentLives)
    print()

def main():
    random.seed()

    words = loadWords()

    chosenWord = words[random.randint(0, 10000)]
    numberOfLetters = len(chosenWord)
    numberOfLettersLeft = numberOfLetters

    goodLetters = []
    badLetters = []

    global LIVES
    currentLives = LIVES

    while numberOfLettersLeft > 0 and currentLives > 0:
        printStatus(chosenWord, goodLetters, badLetters, currentLives)

        letter = input()

        num = chosenWord.count(letter)
        if num > 0:
            goodLetters.append(letter)
            numberOfLettersLeft -= num
        else:
            badLetters.append(letter)
            currentLives -= 1

    printStatus(chosenWord, goodLetters, badLetters, currentLives)

    if numberOfLettersLeft == 0:
        print("Cestitam! :)")
    else:
        print(":( Rec je bila:", chosenWord)

main()

