WORDS = "reci.txt"

def loadWords():
    '''
    Ucitava reci iz fajla.
    '''
    with open(WORDS, 'r') as file:
        words = file.readlines() # Imaju \n na kraju

    wordsFixed = [] # Bez \n
    for word in words:
        wordsFixed.append(word.replace('\n', ''))
    
    return wordsFixed

def printStatus(word, goodLetters, badLetters, currentLives):
    '''
    Ispisivanje trenutnog stanja igre na konzolu.

    :word: Zadata rec
    :goodLetters: Pogodjena slova koja se nalaze u reci
    :badLetters: Pogdjena slova koja se _ne_ nalaze u reci
    :currentLives: Preostao broj zivota
    '''
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