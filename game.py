import pygame
import random
import time
pygame.init()

from const import *

from deck import *

Start = False 

FontName = pygame.font.match_font("arial") 
YELLOW = (255, 255, 0)
def DrawText(surf, text, size, x, y):
    font = pygame.font.Font(FontName, size)
    TextSurface = font.render(text, True, YELLOW) 
    TextRect = TextSurface.get_rect()
    TextRect.midtop = (x, y)
    surf.blit(TextSurface, TextRect) 
 
class Game:
    def __init__(self):
        self.State = "Startscreen"
        self.Turn = ""
        self.PlayerHand = Hit()
        self.NumOfCardsInPH = 1
        self.DealerHand = Hit()
        


        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption( ('Blackjack') )

        # Load background image 
        self.BackgroundImage = pygame.image.load("src/Img/louigi card game.jpg")

        # Load buttons images 

        self.StayButton = pygame.image.load("src/Img/stay.png")
        self.HitButton = pygame.image.load("src/Img/hit.png")
        self.StartButton = pygame.image.load("src/Img/Start.png")
        self.StayButtonRect = self.StayButton.get_rect(topleft=(400, 850))
        self.HitButtonRect = self.HitButton.get_rect(topleft=(150, 850))
        self.StartButtonRect = self.StartButton.get_rect(topleft=(275, 850))




    def StartGame(self):
        self.State =  "Play"
        self.Turn = "Player"


    def PlayerHit(self):
        self.NewCard = Hit()
        self.NewCardValue = self.NewCard[0] 
        self.NewCardImg = self.NewCard[1]
        self.PlayerHand[0] = self.PlayerHand[0] + self.NewCardValue
        self.PlayerHand.append(self.NewCardImg) 
        #self.NumOfCardsInPH = self.NumOfCardsInPH + 1 
        print(self.PlayerHand)
    
    def DealerHit(self):
        self.NewCard = Hit()
        self.NewCardValue = self.NewCard[0] 
        self.NewCardImg = self.NewCard[1]
        self.DealerHand[0] = self.DealerHand[0] + self.NewCardValue
        self.DealerHand.append(self.NewCardImg) 
        #self.NumOfCardsInPH = self.NumOfCardsInPH + 1 
        print(self.DealerHand)
    

    def DealersTurn(self): 
        pass

    def PlayerStay(self):
        self.Turn = "Dealer"

    def DrawCard (self, hand, StartPosition ):
        
        Spacing = -20 
        for index, card in enumerate(hand[1:], start=1):
            x_position = StartPosition[0] + (CWIDTH + Spacing) * (index - 1)
            y_position = StartPosition[1]
            
            CardsInHand = pygame.image.load(card)
            CardsInHand = pygame.transform.scale(CardsInHand, (CWIDTH, CHEIGHT))
            self.screen.blit(CardsInHand, (x_position, y_position))

    def CheckAce(self, Hand):
        self.HasAce = any('ace' in card for card in Hand[1:])




    def CalculateScore(self):
        if self.Turn == "Player":
            if self.PlayerHand[0] > 21 :
                self.PlayerHand[0] = "busted"
                self.Turn = "Dealer"
            elif self.PlayerHand[0] == 21: 
                self.PlayerHand[0] = "Blackjack"
                self.Turn = "Dealer"
            
        if self.Turn == "Dealer":
            time.sleep(1)
            if self.DealerHand[0] > 16:
                self.Turn = "end"
            elif self.DealerHand[0] <= 16:
                self.DealerHit()
            if self.DealerHand[0] > 21:
                self.DealerHand[0] = "busted"
                self.Turn = "end"
            elif self.DealerHand[0] == 21: 
                self.DealerHand[0] = "Blackjack" 
                self.Turn = "end" 

    # show methods 
    def DrawBackground(self):
        self.screen.blit(self.BackgroundImage, (0, 0))

        if self.State == "Play": 
            self.DrawCard(self.PlayerHand, (150, 700 ))
            self.DrawCard(self.DealerHand, (150, 450 ))
            self.CalculateScore()
                
            # draw the score text
            DrawText(self.screen, str(self.PlayerHand[0]), 40, WIDTH / 2, 800)
            DrawText(self.screen, str(self.DealerHand[0]), 40, WIDTH / 2, 550)

        if self.State == "Startscreen" :  
            self.screen.blit(self.StartButton, (275, 850))

        elif self.Turn == "Player" : 
            self.screen.blit(self.StayButton, (400, 850))
            self.screen.blit(self.HitButton, (150, 850))
        






