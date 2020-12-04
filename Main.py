import  pygame
from Constants import  *
class Main:
    def __init__(self,screen):
        self.screen=screen
        self.background=pygame.image.load('Old-Dungeon.jpg')
        self.running =True
        self.main_loop()
        pass
    def render(self):
        self.screen.blit(self.background,(0,0))
        pygame.display.flip()
        pass
    def main_loop(self):
        while self.running==True:
            self.render()
    def handl_events(self):
        pass

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIGHT,SCREEN_HEIGHT))
game = Main(screen)