colors = ['red', 'blue', 'green', 'yellow']

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __repr__(self):
        return f"{self.color}-{self.value} "

# return the list of cards
def genCards():
    # create a list of all the cards in a standard Uno deck
    cards = []

    # add number cards (0-9) for each color
    for color in colors:
        for i in range(10):
            cards.append(Card(i, color))

    for color in colors:
        for i in range(1,10):
            cards.append(Card(i, color))

    # add action cards (reverse, skip, +2) for each color
    for color in colors:
        for i in range(2):
            cards.append(Card('reverse', color))
            cards.append(Card('skip', color))
            cards.append(Card('+2', color))

    # add wild and wild +4 cards
    for i in range(4):
        cards.append(Card('blank', 'wild'))
        cards.append(Card('+4', 'wild'))

    return cards


