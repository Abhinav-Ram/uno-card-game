import cardgenerator
import cardfn
import numpy as np
import random
import click

count = 7
cards = np.array(cardgenerator.genCards())
np.random.shuffle(cards)

playerDecks = []
restDeck = []
nameList = []
playerCount = int(input("Enter no of players: "))
for i in range(playerCount):
    name = input("Enter name of player-{}:".format(i+1))
    nameList.append(name)

for each in range(playerCount):
    playerDecks.append(cards[count*each:count*each+count])
restDeck = np.array(cards[playerCount * count: cards.size])


#THE ACTUAL GAME PLAY

playerIndex = 0
gameDirn = 1
currentCard = restDeck[0]
restDeck = np.delete(restDeck,0)
winOrder = []

while(1):
    click.clear()
    print("\nThe current card is", currentCard)
    print("{}'s turn.".format(nameList[playerIndex]), end=' ')
    if(len(playerDecks) == 1):
        print(nameList[playerIndex],"loses the game. Game over")
        winOrder.append(nameList[playerIndex])
        print("The order of winning is: ", winOrder)   
        exit()
    input("Press Enter to continue...")
    print(playerDecks[playerIndex])
    while(1):
        if(currentCard.value == '+4'):
            click.clear()
            for i in range(4):
                playerDecks[playerIndex] = np.append(playerDecks[playerIndex],restDeck[0])
                print("{} has drawn {}".format(nameList[playerIndex], restDeck[0]))
                restDeck = np.delete(restDeck,0)
            input("Press Enter to continue...")
            currentCard.value = 'blank'
            break
        
        elif(currentCard.value == '+2'):
            click.clear()
            for i in range(2):
                playerDecks[playerIndex] = np.append(playerDecks[playerIndex],restDeck[0])
                print("{} has drawn {}".format(nameList[playerIndex], restDeck[0]))
                restDeck = np.delete(restDeck,0)
            input("Press Enter to continue...")
            currentCard.value = 'plus2'
            break

        elif(currentCard.value == 'skip'):
            currentCard.value = 'Skip'
            break

        chosenCardIndex = ""
        while(chosenCardIndex == ""):
            chosenCardIndex = input(">> ")
        # play a card
        chosenCardIndex = int(chosenCardIndex)
        if(chosenCardIndex >=0 and chosenCardIndex < playerDecks[playerIndex].size):    
            chosenCard = playerDecks[playerIndex][chosenCardIndex]
            if(cardfn.isValid(chosenCard, currentCard)):
                currentCard = chosenCard
                playerDecks[playerIndex] = np.delete(playerDecks[playerIndex], chosenCardIndex)
                restDeck = np.append(restDeck, currentCard)
                print("{} has chosen {}".format(nameList[playerIndex], chosenCard))
                if(playerDecks[playerIndex].size == 0):
                    print(nameList[playerIndex],"beats the game")
                    winOrder.append(nameList[playerIndex])
                    del playerDecks[playerIndex]
                    del nameList[playerIndex]
                    playerCount -= 1
                input("Press Enter to continue...")
                if(currentCard.color == 'wild'):
                    print(cardgenerator.colors)
                    currentCard.color = cardgenerator.colors[int(input("pick any color index: "))]
                if(currentCard.value == 'reverse'):
                    gameDirn *= -1
                    currentCard.value = 'Reverse'
                break
        #draw a card
        elif(chosenCardIndex == -1):
            playerDecks[playerIndex] = np.append(playerDecks[playerIndex],restDeck[0])
            print("{} has drawn {}".format(nameList[playerIndex], restDeck[0]))
            input("Press Enter to continue...")
            restDeck = np.delete(restDeck,0)
            break
        
    playerIndex = (playerIndex + gameDirn) % playerCount