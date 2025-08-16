# use Python's built-in random module to shuffle the deck of cards.
import random


# Card models a physical playing card.
class Card:
    ''' An individual card with a suit and rank. Defaults to faceup. '''

    def __init__(self, suit, rank, faceup=True):
        ''' The Card constructor.

            Args:
                suit    |   US card decks include spades, diamonds, hearts, and clubs. ♠ ♦ ♥ ♣
                rank    |   US card decks include A 2 3 4 5 6 7 8 9 10 J Q K.
                faceup  |   (optional) Cards facing up are displayed in the console.
        '''
        # Defining attributes for suit and rank.
        # For example:
        # ♠ 2
        self.suit = suit
        self.rank = rank
        # Cards can be either face up or face down in enough card games that a faceup attribute is included.
        self.faceup = faceup

    def __str__(self):
        rank = self.rank if self.faceup else '?'
        suit = self.suit if self.faceup else '?'
        return f'{rank}{suit}'

    def __repr__(self):
        return str(self)


# Deck models a standard US deck of cards.
class Deck:
    ''' A deck based on a standard US card deck.

        Consists of 13 possible card ranks from Ace to King.
        Consists of  4 possible card suits: spade, diamond, heart, club.

        Create class attributes containing suit and rank.
    '''
    suits = '♠ ♦ ♥ ♣'.split()
    ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        ''' Create a new deck consisting of one rank for each suit. '''
        self.cards = [Card(s, r) for s in self.suits for r in self.ranks]

    def shuffle(self):
        ''' Models the ability to shuffle a deck of cards.
            Uses the shuffle function from the random module.
        '''
        random.shuffle(self.cards)

    def deal(self, faceup=True):
        ''' Models the ability to deal a card. '''
        card = self.cards.pop()
        card.faceup = faceup
        return card

    def __str__(self):
        return ' '.join([f'{c.rank}{c.suit},' for c in self.cards])

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.cards)

