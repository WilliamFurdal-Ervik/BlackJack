
from deck import Deck



class Hand:
    
    def __init__( self, row, col, card=None ): 
        self.row = row
        self.col = col
        self.card = []
    def AddCard(self, card):
        self.card.append(card)


PlayerHand = []

PlayerHand = Deck.HandCard(PlayerHand)

