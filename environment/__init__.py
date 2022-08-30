import os
from typing import Any

import pygame
from pygame.locals import *


CUR_FILE_PATH = os.path.join("Little-Fight-Plus", "environment")
SRC_FILE_PATH = os.path.join("Little-Fight-Plus", "image")


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y, width, height):
        super(Ground, self).__init__()
        self.image = pygame.image.load(os.path.relpath(os.path.join(SRC_FILE_PATH, "ground", image), CUR_FILE_PATH))\
            .convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.rect.Rect(pos_x, pos_y, width, height)

    def update(self, *args: Any, **kwargs: Any) -> None:
        kwargs["surface"].blit(self.image, self.rect)


class Grounds(pygame.sprite.Group):
    def __init__(self):
        super(Grounds, self).__init__()
        self.add(Ground("ground0.png", 0, 310, 50, 50))
        self.add(Ground("ground0.png", 50, 310, 50, 50))
        self.add(Ground("ground0.png", 100, 300, 50, 75))
        self.add(Ground("ground0.png", 150, 290, 50, 85))
        self.add(Ground("ground0.png", 200, 280, 50, 95))
        self.add(Ground("ground0.png", 250, 270, 50, 105))
        self.add(Ground("ground0.png", 300, 270, 50, 105))
        self.add(Ground("ground0.png", 350, 270, 50, 105))
        self.add(Ground("ground0.png", 400, 270, 50, 105))
        self.add(Ground("ground0.png", 450, 270, 50, 105))
        self.add(Ground("ground0.png", 500, 270, 50, 105))
        self.add(Ground("ground0.png", 550, 270, 50, 105))
        self.add(Ground("ground0.png", 600, 270, 50, 105))
        self.add(Ground("ground0.png", 650, 270, 50, 105))

    def update(self, *args: Any, **kwargs: Any) -> None:
        super(Grounds, self).update(surface=kwargs["surface"])


class Env(pygame.sprite.Group):
    def __init__(self, surface, gra):
        super(Env, self).__init__()
        self.surface = surface
        self.gravity = gra
        self.grounds = Grounds()

    def update(self, *args: Any, **kwargs: Any) -> None:
        # super(Env, self).update(surface=self.surface)
        self.grounds.update(surface=self.surface)
        

if __name__ == "__main__":
    HEIGHT = 350
    WIDTH = 700
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    env = Env(displaysurface, 0.5)
    while True:
        env.update()
        pygame.display.update()
