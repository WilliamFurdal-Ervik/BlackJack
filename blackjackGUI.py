import random
import time
H2 = ["H2 ", 2]      ;D2= ["D2 ", 2]      ;C2= ["C2 ", 2]      ;    S2= ["S2 ", 2]
H3 = ["H3 ", 3]      ;D3= ["D3 ", 3]      ;C3= ["C3 ", 3]      ;    S3= ["S3 ", 3]
H4= ["H4 ", 4]       ;D4= ["D4 ", 4]      ;C4= ["C4 ", 4]      ;    S4= ["S4 ", 4]
H5= ["H5 ", 5]       ;D5= ["D5 ", 5]      ;C5= ["C5 ", 5]      ;    S5= ["S5 ", 5]
H6= ["H6 ", 6]       ;D6= ["D6 ", 6]      ;C6= ["C6 ", 6]      ;    S6= ["S6 ", 6]
H7= ["H7 ", 7]       ;D7= ["D7 ", 7]      ;C7= ["C7 ", 7]      ;    S7= ["S7 ", 7]
H8= ["H8 ", 8]       ;D8= ["D8 ", 8]      ;C8= ["C8 ", 8]      ;    S8= ["S8 ", 8]
H9= ["H9 ", 9]       ;D9= ["D9 ", 9]      ;C9= ["C9 ", 9]      ;    S9= ["S9 ", 9]
H10= ["H10 ", 10]    ;D10= ["D10 ", 10]   ;C10= ["C10 ", 10]   ;    S10= ["S10 ", 10]
HJ= ["HJ ", 10]      ;DJ= ["DJ ", 10]     ;CJ= ["CJ ", 10]     ;    SJ= ["SJ ", 10]
HQ= ["HQ ", 10]      ;DQ= ["DQ ", 10]     ;CQ= ["CQ ", 10]     ;    SQ= ["SQ ", 10]
HK= ["HK ", 10]      ;DK= ["DK ", 10]     ;CK= ["CK ", 10]     ;    SK= ["SK ", 10]
HA= ["HA", 1]      ;DA= ["DA", 1]     ;CA= ["CA", 1]     ;    SA= ["SA", 1]
Heart =  [H2  , H3  , H4  , H5  , H6  , H7  , H8  , H9  , H10  , HJ  , HQ  , HK  , HA]          
Diamond = [D2  , D3  , D4  , D5  , D6  , D7  , D8  , D9  , D10  , DJ  , DQ  , DK  , DA]
Club =  [C2  , C3  , C4  , C5  , C6  , C7  , C8  , C9  , C10  , CJ  , CQ  , CK  , CA]
Spade =  [S2  , S3  , S4  , S5  , S6  , S7  , S8  , S9  , S10  , SJ  , SQ  , SK  , SA]

Aces = ['SA', 'DA', 'CA', 'HA']

Suit = [Heart, Diamond, Club, Spade]


screen_width = 593
screen_height = 899






def HandCard():
    CardSuit = random.choice(Suit)

    Card = random.choice(CardSuit)

    CardSuit.remove(Card)
    
    return Card



PlayerHand = ""
PlayerHand = HandCard() 
PlayerValue = str(PlayerHand[1])
DealerHand = ""
DealerHand = HandCard() 
DealerValue = str(DealerHand[1])


def Hit(variabel):
    NewCard = HandCard()
    NewCardName = NewCard[0]
    NewCardValue = NewCard[1]
    variabel.append(NewCardName)
    variabel[1] = variabel[1] + NewCardValue

    
    return variabel 








#if Play != "yes":    
    #time.sleep(0.5)
   # print("WHAT THE ACTUAL ####")
  #  time.sleep(1)
 #   print("I am sure you do")
#    time.sleep(0.5)
 #   while Play != "yes":
  #      Play = input("Wanna play Blackjack : ")

# if Play == "yes":
  #  time.sleep(0.5)
   # print("Good")
    #time.sleep(0.5)

PlayerHand = Hit(PlayerHand) ; PlayerValue = str(PlayerHand[1])



print(f"""Your hand: {PlayerHand}""" )
print(f"""dealers hand: {DealerHand}""" )
# Players turn to paly 
Play = True 
while Play == True :
    AceInHand = False
    for A in Aces :
        if A in PlayerHand :
             AceInHand = True
             print("true")
    if AceInHand == True:
         if PlayerHand[1] == 11 :
              PlayerHand[1] = 21
              PlayerValue = "21"
              print(PlayerValue)
         elif PlayerHand[1] < 11 :
              PlayerValue = f"""{PlayerHand[1]} | {PlayerHand[1] + 10} """
              print(PlayerValue)
         elif PlayerHand[1] > 11 :
              PlayerValue = f"""{PlayerHand[1]}"""
              print(PlayerValue)
    if PlayerHand[1]  < 21 :
        Choice = input("(H)it or (S)tay: ")
        if Choice == "H":
            PlayerHand = Hit(PlayerHand) ; PlayerValue = str(PlayerHand[1])
            print(f"""Your new hand: {PlayerHand} {PlayerValue} """ )
        elif  Choice ==  "S":
            if AceInHand == True :
                if PlayerHand[1] < 11 :
                     PlayerHand[1] = PlayerHand[1] + 10 
                     PlayerValue = PlayerHand[1]                           
            Play = False 
        
        else : 
            print("not an optian" )

    elif  PlayerHand[1] > 21 :
            print("busted")
            Play = False
    elif PlayerHand[1] == 21:
            print("BLACKJACK") 
            Play = False

# Dealers turn to play 
print("Dealers turn")
Dplay  = True 
while Dplay == True: 
    print(DealerHand)
    AceInHand = False
    for A in Aces :
        if A in DealerHand :
             AceInHand = True
             print("true")
    if AceInHand == True:
         if DealerHand[1] == 11 :
              DealerHand[1] = 21
              DealerValue = "21"
              print(DealerValue)
         elif DealerHand[1] < 11 :
              DealerValue = f"""{DealerHand[1]} | {DealerHand[1] + 10} """
              print(DealerValue)
         elif DealerHand[1] > 11 :
              DealerValue = f"""{DealerHand[1]}"""
              print(DealerValue)
    if DealerHand[1] <= 16 :   # Dealer hit 
            print("Dealer Hit")
            DealerHand = Hit(DealerHand)
            time.sleep(1)
    elif DealerHand[1] > 16 and DealerHand[1] < 21:   # Dealer stay  
            print("Dealer stay")
            Dplay = False
    elif DealerHand[1] > 21:   # Dealer bust 
            time.sleep(1) 
            print("Dealer busted")
            Dplay = False
    elif DealerHand[1] == 21:  # Dealer blackjack 
            time.sleep(1)
            print("BLACKJACK") 
            Dplay = False        



        






time.sleep(1)
print(f"""Dealers Hand: {DealerHand} 
your Hand: {PlayerHand}""")




import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 593
screen_height = 899
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blackjack")

# Load board image
board_image = pygame.image.load("img/louigi card game.jpg")

# Main game loop
running = True
while running:
    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw board image
    screen.blit(board_image, (0, 0))

    # Draw other game elements and update the display
    # Place your existing game logic code here
    # For example:
    # - Drawing player and dealer hands
    # - Handling player actions (e.g., Hit, Stand)
    # - Evaluating game outcomes (e.g., Blackjack, bust)
    # - Updating game state and displaying messages

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()