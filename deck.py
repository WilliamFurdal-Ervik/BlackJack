import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            card_value = values[rank]
            card_image = f"src/Img/PNG-cards-1.3/{rank.lower()}_of_{suit.lower()}.png"
            deck.append([card_value, card_image])
    return deck 

deck1 = create_deck()



def Hit():
    Card = random.choice(deck1)
    deck1.remove(Card)
    
    return Card
Card = Hit()




