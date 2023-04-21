import cardgenerator

def isValid(inputCard, currentCard):
    if(inputCard.value == '+2' and currentCard.value == 'plus2'):
        return True
    if(inputCard.value == 'skip' and currentCard.value == 'Skip'):
        return True
    if(inputCard.value == 'reverse' and currentCard.value == 'Reverse'):
        return True
    elif(inputCard.color == currentCard.color or inputCard.value == currentCard.value or inputCard.color == 'wild' or currentCard.color == 'wild'):
        return True
    else:
        return False