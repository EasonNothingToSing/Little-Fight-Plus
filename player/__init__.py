from typing import Any
from environment import *
import pygame
from pygame.locals import *
import sys
import os
import random


__all__ = ["Player"]


class Player(pygame.sprite.Sprite):
    def __init__(self, _env, load_images, images_para):
        super(Player, self).__init__()
        self.env = _env
        self.load_images = load_images
        self.images_para = images_para
        self.scale_width = self.load_images[0].get_width()/self.images_para[0][0]
        self.scale_height = self.load_images[0].get_height()/self.images_para[0][1]
        self.sub_rect = pygame.Rect(0, 0, self.scale_width*1, self.scale_height*1)
        self.image = self.load_images[0].subsurface(self.sub_rect)
        self.image.set_colorkey((0, 0, 0))

        # Base attribute
        self.rect = pygame.Rect(90, 0, self.scale_width-20, self.scale_height)
        self.acc = pygame.math.Vector2(0, self.env.gravity)
        self.vel = pygame.math.Vector2(0, 0)
        self.direction = False  # False->Right    True->Left
        self.status = "originate"
        self.jump_status = False
        self.stair_threshold = 15

        self.frame_point = 0
        self.frame_count = 0

        self.stand_lst = [[(0, 0), 15], [(1, 0), 15], [(2, 0), 15], [(3, 0), 10]]
        self.move_lst = [[(4, 0), 5], [(5, 0), 5], [(6, 0), 5], [(7, 0), 5], [(5, 0), 5], [(4, 0), 5]]
        self.jump_lst = [[(2, 6), 1], [(1, 6), 5], [(0, 6), 5]]

    def move(self, dir):
        if self.status == "stand":
            self.status = "move"
            self.direction = dir
            if dir:
                self.vel.x += -1
            else:
                self.vel.x += 1
            self.frame_point = 0
            self.frame_count = 0
        elif self.status == "jump" or self.jump_status is True:
            self.direction = dir
            if dir == 0:
                self.vel.x += 1
            else:
                self.vel.x += -1

    def moving(self):
        self.sub_rect.x = self.scale_width * self.move_lst[self.frame_point][0][0]
        self.sub_rect.y = self.scale_height * self.move_lst[self.frame_point][0][1]

        self.image = self.load_images[0].subsurface(self.sub_rect)
        self.image.set_colorkey((0, 0, 0))

        if self.frame_count < self.move_lst[self.frame_point][1]:
            self.frame_count += 1
        else:
            self.frame_count = 0
            self.frame_point += 1

            if self.frame_point > len(self.move_lst) - 1:
                self.stand()

    def stand(self):
        self.status = "stand"
        self.vel.x = 0
        self.frame_point = 0
        self.frame_count = 0

    def standing(self):
        self.sub_rect.x = self.scale_width * self.stand_lst[self.frame_point][0][0]
        self.sub_rect.y = self.scale_height * self.stand_lst[self.frame_point][0][1]

        self.image = self.load_images[0].subsurface(self.sub_rect)
        self.image.set_colorkey((0, 0, 0))

        if self.frame_count < self.stand_lst[self.frame_point][1]:
            self.frame_count += 1
        else:
            self.frame_count = 0
            self.frame_point += 1

            if self.frame_point > len(self.stand_lst) - 1:
                self.stand()

    def jump(self):
        if self.status != "jump" and not self.jump_status:
            self.rect.y += -1
            self.vel.y = -5
            self.acc.y = self.env.gravity
            self.status = "jump"
            self.jump_status = True
            self.frame_point = 0
            self.frame_count = 0

    def jumping(self, ret):
        self.sub_rect.x = self.scale_width * self.jump_lst[self.frame_point][0][0]
        self.sub_rect.y = self.scale_height * self.jump_lst[self.frame_point][0][1]

        self.image = self.load_images[0].subsurface(self.sub_rect)
        self.image.set_colorkey((0, 0, 0))

        if ret:
            if self.frame_count < self.jump_lst[self.frame_point][1]:
                self.frame_count += 1
            else:
                self.frame_count = 0
                self.frame_point += 1

                if self.frame_point > len(self.jump_lst) - 1:
                    self.jump_status = False
                    self.stand()
        else:
            pass

    def check_gravity(self):
        ret = pygame.sprite.spritecollide(self, self.env.grounds, False)
        if ret:
            pass
        # In the space
        else:
            pass

    def update(self, *args: Any, **kwargs: Any) -> None:
        # ret = pygame.sprite.spritecollide(self, self.env.grounds, False)
        # if ret:
        #     for r in ret:
        #         if abs(r.rect.midtop[1] - self.rect.midbottom[1]) <= self.stair_threshold:
        #             self.acc.y = 0
        #             self.vel.y = 0
        #             self.rect.midbottom = (self.rect.midbottom[0], r.rect.midtop[1] + 1)
        #         else:
        #             # Right collide
        #             if r.rect.midright[0] > self.rect.midright[0] >= r.rect.midleft[0]:
        #                 if self.acc.x > 0:
        #                     self.acc.x = 0
        #                 if self.vel.x > 0:
        #                     self.vel.x = 0
        #             # Left collide
        #             elif r.rect.midleft[0] < self.rect.midleft[0] <= r.rect.midright[0]:
        #                 if self.acc.x < 0:
        #                     self.acc.x = 0
        #                 if self.vel.x < 0:
        #                     self.vel.x = 0
        # else:
        #     self.acc.y = self.env.gravity
        #
        # self.vel += self.acc
        # self.rect.x += self.vel.x
        # self.rect.y += self.vel.y

        if self.status == "originate":
            ret = pygame.sprite.spritecollide(self, self.env.grounds, False)
            if ret:
                self.status = "stand"
            else:
                pass
        elif self.status == "stand":
            self.standing()
        elif self.status == "jump":
            self.jumping(ret)
        elif self.status == "move":
            self.moving()

        print(self.status, "Dir->", self.direction)
        print(self.rect.midtop, self.rect.midleft, self.rect.midbottom, self.rect.midright)
        self.image = pygame.transform.flip(self.image, self.direction, False)
        self.env.surface.blit(self.image, self.rect)
        pygame.draw.rect(self.env.surface, (255, 0, 0), self.rect, 1)
        pygame.draw.rect(self.env.surface, (0, 255, 0), pygame.rect.Rect(self.rect.x, self.rect.y, self.sub_rect.width, self.sub_rect.height), 1)


if __name__ == "__main__":
    HEIGHT = 350
    WIDTH = 700
    FPS = 60
    FPS_CLOCK = pygame.time.Clock()
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    env = Env(displaysurface, 0.2, WIDTH, HEIGHT)
    p1 = Player(env, [pygame.image.load("../image/player/davis_0.bmp").convert_alpha()], [(10, 7)])
    while True:
        displaysurface.fill((0, 0, 0), (0, 0, WIDTH, HEIGHT))
        env.update()
        for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key[pygame.K_k]:
                    p1.jump()
                if key[pygame.K_a]:
                    p1.move(True)
                if key[pygame.K_d]:
                    p1.move(False)
        p1.update()
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
