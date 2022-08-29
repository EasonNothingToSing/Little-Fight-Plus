import pygame
from pygame.locals import *
import sys
import os
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, env, load_images, images_para):
        super(Player, self).__init__()
        self.env = env
        self.load_images = load_images
        self.images_para = images_para
        self.scale_width = self.load_images[0].get_width()/self.images_para[0][0]
        self.scale_height = self.load_images[0].get_height()/self.images_para[0][1]

        # Base attribute
        self.rect = pygame.Rect(0, 0, self.scale_width, self.scale_height)
        self.acc = pygame.math.Vector2(0, self.env.gravity)
        self.vel = pygame.math.Vector2(0, 0)
        self.image = None
        self.direction = "RIGHT"
        self.status = "originate"
        self.jumping = False


if __name__ == "__main__":
    pygame.init()
