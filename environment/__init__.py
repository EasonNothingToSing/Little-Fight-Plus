import os
import xml.etree.ElementTree as ET
from typing import Any

import pygame
from pygame.locals import *


__all__ = ["Env"]

CUR_FILE_PATH = os.path.join("Little-Fight-Plus")
SRC_FILE_PATH = os.path.join("Little-Fight-Plus", "image")


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y, width, height):
        super(Ground, self).__init__()
        # self.image = pygame.image.load(os.path.relpath(os.path.join(SRC_FILE_PATH, "ground", image), CUR_FILE_PATH))\
        #     .convert_alpha()
        # self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.rect.Rect(pos_x, pos_y, width, height)

    def update(self, *args: Any, **kwargs: Any) -> None:
        # kwargs["surface"].blit(self.image, self.rect)
        pygame.draw.rect(kwargs["surface"], (0, 0, 255), self.rect, 1)


class Grounds(pygame.sprite.Group):
    def __init__(self, _env, desc_file):
        super(Grounds, self).__init__()
        self.env = _env
        self.tree = ET.parse(desc_file)
        self.root = self.tree.getroot()
        for i in self.root.iter(tag="Ground"):
            self.add(Ground(i.find("image").text, int(i.find("x").text), self.env.height - int(i.find("y").text),
                            int(i.find("width").text), int(i.find("height").text)))

    def update(self, *args: Any, **kwargs: Any) -> None:
        super(Grounds, self).update(surface=kwargs["surface"])


class Env(pygame.sprite.Group):
    def __init__(self, surface, gra, width, height):
        super(Env, self).__init__()
        self.surface = surface
        self.gravity = gra
        self.width = width
        self.height = height
        self.grounds = Grounds(self, "grounds_desc_file.xml")

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.grounds.update(surface=self.surface)
        

if __name__ == "__main__":
    HEIGHT = 350
    WIDTH = 700
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    env = Env(displaysurface, 0.5, WIDTH, HEIGHT)
    while True:
        displaysurface.fill((255, 255, 255), (0, 0, WIDTH, HEIGHT))
        env.update()
        pygame.display.update()
