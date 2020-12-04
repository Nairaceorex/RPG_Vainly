import pygame
from Constants import *


class Person:
    hp = 100
    lvlAttack = 1
    lvlMagic = 1
    lvlDefence = 1
    lvlHeal = 1

    def __init__(self):
        self.state = ALIVE
        self.directon = RIGHT
        self.x=START_X
        self.y=START_Y
        self.name = 'Hero'
        self.hp=HP
        self.mp=MP
        self.image_pack = ['playerR.png','playerL.png']
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(0, 0, 580, 580))
            #i.append(temp.subsurface(580, 0, 580, 580))
            self.images.append(i)
        self.moving = [0, 0,0]

    def move(self):
        pass

    def render(self, screen):
        screen.blit(self.images[self.directon][self.state], (self.x, self.y))

    def render_ui(self, screen):
        pass
