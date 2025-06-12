import pygame
import gamesettings as gs
from assets import Assets #Class Assets from the file assets

class BomberMan:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((gs.SCREENWEIGHT, gs.SCREENHEIGHT))
        pygame.display.set_caption("BomberMan")
        
        self.ASSETS = Assets()
        self.FPS = pygame.time.Clock()
        
        self.run = True
     
#-----Main Sections-----#
        
    #Input method    
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                
    #Update method
    def update(self):
        self.FPS.tick(gs.FPS)
        
    #Draw method    
    def draw(self, window):
        window.fill(gs.BLACK)
        pygame.display.update()
        
        
        
    def rungame(self):
        while self.run == True: #While the game is running, execute the input, update and draw method
            self.input()
            self.update()
            self.draw(self.screen)
            
            
if __name__=="__main__": #Only execute if the file from where it's being executed is the main
    game = BomberMan()
    game.rungame()
    pygame.quit()