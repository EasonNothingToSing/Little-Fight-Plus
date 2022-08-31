# coding = utf-8
import pygame
from pygame.locals import *
from player import *
from environment import *

#
# pygame.init()
#
# HEIGHT = 350
# WIDTH = 700
# ACC = 0.5
# FRIC = -0.10
# FPS = 60
# FPS_CLOCK = pygame.time.Clock()
# COUNT = 0
#
# displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Little-Fight")
#
#
# class Background(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Background, self).__init__()
#         self.bgimage = pygame.image.load(os.path.join("image", "background", "Background.png"))
#         self.bgrect = self.bgimage.get_rect()
#
#     def render(self):
#         displaysurface.blit(self.bgimage, self.bgrect)
#
#
# class Ground(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Ground, self).__init__()
#         self.gimage_lvl0 = pygame.image.load(os.path.join("image", "ground", "ground0.png"))
#         self.gimage_lvl0 = pygame.transform.scale(self.gimage_lvl0, (700, 50))
#         self.rect = self.gimage_lvl0.get_rect(center=(350, 330))
#
#     def render(self):
#         displaysurface.blit(self.gimage_lvl0, self.rect)
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self, ground):
#         super(Player, self).__init__()
#         self.image = pygame.image.load(os.path.join("image", "player", "davis_0.bmp")).convert()
#         self.scale_width = self.image.get_width()/10
#         self.scale_height = self.image.get_height()/7
#         self.image.set_colorkey((0, 0, 0))
#
#         self.rect = pygame.Rect(0, 0, self.scale_width, self.scale_height)
#         self.subrect = pygame.Rect(0, 0, self.scale_width, self.scale_height)
#
#         self.display_image = None
#         self.ground = ground
#
#         self.vel = pygame.math.Vector2(0, 0)
#         self.acc = pygame.math.Vector2(0, 0.5)
#
#         self.direction = "RIGHT"
#
#         self.status = "stand"
#         self.updating = True
#         self.fps_count = 0
#         self.frame_point = 0
#
#         self.jumping = False
#         # self.standing = False
#         # self.moving = False
#         # self.running = False
#         # self.attacking = False
#         # self.defending = False
#
#         self.stand_lst = [[(0, 0), 15], [(1, 0), 15], [(2, 0), 15], [(3, 0), 10]]
#         self.move_lst = [[(4, 0), 5], [(5, 0), 5], [(6, 0), 5], [(7, 0), 5], [(5, 0), 5], [(4, 0), 5]]
#         self.random_attack_lst = None
#         self.attack_lst_0 = [[(0, 1), 15], [(1, 1), 15], [(2, 1), 15], [(3, 1), 10]]
#         self.attack_lst_1 = [[(4, 1), 15], [(5, 1), 15], [(6, 1), 15], [(7, 1), 10]]
#
#     def update(self):
#         hits = pygame.sprite.spritecollide(self, self.ground, False)
#         if not hits:
#             self.rect.y += self.vel.y
#             self.vel += self.acc
#         else:
#             self.vel.y = 0
#             self.jumping = False
#
#         key = pygame.key.get_pressed()
#         if key[pygame.K_SPACE]:
#             if not self.jumping:
#                 self.jumping = True
#                 self.updating = True
#         if key[pygame.K_k]:
#             if self.status != "defend":
#                 self.status = "defend"
#                 self.updating = True
#         elif key[pygame.K_j]:
#             if self.status != "attack":
#                 self.status = "attack"
#                 self.updating = True
#         elif key[pygame.K_a]:
#             if self.status != "move" or self.direction != "LEFT":
#                 self.direction = "LEFT"
#                 self.status = "move"
#                 self.updating = True
#         elif key[pygame.K_d]:
#             if self.status != "move" or self.direction != "RIGHT":
#                 self.direction = "RIGHT"
#                 self.status = "move"
#                 self.updating = True
#
#         if self.jumping:
#             self.jump()
#
#         if self.status == "attack":
#             self.attack()
#         elif self.status == "defend":
#             self.defend()
#         elif self.status == "move":
#             self.move()
#         elif self.status == "stand":
#             self.stand()
#
#     def stand(self):
#         if self.updating:
#             self.updating = False
#             self.frame_point = 0
#             self.fps_count = 0
#
#         self.subrect.x = self.scale_width * self.stand_lst[self.frame_point][0][0]
#         self.subrect.y = self.scale_height * self.stand_lst[self.frame_point][0][1]
#
#         self.display_image = self.image.subsurface(self.subrect)
#
#         if self.fps_count < self.stand_lst[self.frame_point][1]:
#             self.fps_count += 1
#         else:
#             self.fps_count = 0
#             self.frame_point += 1
#
#             if self.frame_point > len(self.stand_lst) - 1:
#                 self.updating = True
#                 self.status = "stand"
#
#     def move(self):
#         if self.updating:
#             self.updating = False
#             self.frame_point = 0
#             self.fps_count = 0
#
#         self.subrect.x = self.scale_width * self.move_lst[self.frame_point][0][0]
#         self.subrect.y = self.scale_height * self.move_lst[self.frame_point][0][1]
#
#         if self.direction == "RIGHT":
#             self.rect.x += 1
#         else:
#             self.rect.x -= 1
#
#         self.display_image = self.image.subsurface(self.subrect)
#
#         if self.fps_count < self.move_lst[self.frame_point][1]:
#             self.fps_count += 1
#         else:
#             self.fps_count = 0
#             self.frame_point += 1
#
#             if self.frame_point > len(self.move_lst) - 1:
#                 self.updating = True
#                 self.status = "stand"
#
#     def attack(self):
#         if self.updating:
#             self.updating = False
#             self.frame_point = 0
#             self.fps_count = 0
#             if random.randint(0, 1) == 0:
#                 self.random_attack_lst = self.attack_lst_0
#             else:
#                 self.random_attack_lst = self.attack_lst_1
#
#         self.subrect.x = self.scale_width * self.random_attack_lst[self.frame_point][0][0]
#         self.subrect.y = self.scale_height * self.random_attack_lst[self.frame_point][0][1]
#
#         self.display_image = self.image.subsurface(self.subrect)
#
#         if self.fps_count < self.random_attack_lst[self.frame_point][1]:
#             self.fps_count += 1
#         else:
#             self.fps_count = 0
#             self.frame_point += 1
#             if self.direction == "RIGHT":
#                 self.rect.x += ACC*5
#             else:
#                 self.rect.x -= ACC*5
#
#             if self.frame_point > len(self.random_attack_lst) - 1:
#                 self.updating = True
#                 self.status = "stand"
#
#     def defend(self):
#         pass
#
#     def jump(self):
#         if self.updating:
#             self.vel.y = -12
#             self.updating = False
#             self.rect.y -= 1
#
#     def render(self):
#         if self.direction == "LEFT":
#             self.display_image = pygame.transform.flip(self.display_image, True, False)
#
#         print(self.rect.x, self.rect.y)
#         displaysurface.blit(self.display_image, self.rect)
#
#
# class Enemy(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Enemy, self).__init__()

if __name__ == "__main__":
    HEIGHT = 350
    WIDTH = 700
    FPS = 60
    FPS_CLOCK = pygame.time.Clock()
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    env = Env(displaysurface, 0.2, WIDTH, HEIGHT)
    p1 = Player(env, [pygame.image.load("image/player/davis_0.bmp").convert_alpha()], [(10, 7)])
    while True:
        displaysurface.fill((0, 0, 0), (0, 0, WIDTH, HEIGHT))
        env.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
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

