import pygame
from pygame.locals import *


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super(Ground, self).__init__()



class Env(pygame.sprite.Group):
    def __init__(self, surface, gra):
        super(Env, self).__init__()
        self.surface = surface
        self.gravity = gra


if __name__ == "__main__":
    HEIGHT = 350
    WIDTH = 700
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    env = Env(displaysurface, 0.5)
