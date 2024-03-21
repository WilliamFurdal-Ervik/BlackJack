import pygame 
import sys



from const import *
from game import Game


class Main:
    
    def __init__(self):
        self.Game = Game()

    def mainloop(self):
        
       # Screen = self.screen
        Game = self.Game 

        while True:
            
            Game.DrawBackground()

            for event in pygame.event.get():  # This is in every pygamecode. it checks if the game is being closed. 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if   Game.StartButtonRect.collidepoint(event.pos):
                            Game.StartGame()
                    elif Game.HitButtonRect.collidepoint(event.pos):
                            Game.PlayerHit()
                    elif Game.StayButtonRect.collidepoint(event.pos):
                            Game.PlayerStay()



            pygame.display.update()

main = Main()
main.mainloop()