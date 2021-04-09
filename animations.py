import pygame, sys, time
import settings

# This class draws the animation when the frog is in the water
class Explosion(pygame.sprite.Sprite):
    def __init__(self, xplosion, yplosion):
        pygame.sprite.Sprite.__init__(self)
        self.xplosion = xplosion
        self.yplosion = yplosion

        self.sprites = []
        self.sprites.append(pygame.image.load("images/water1.png"))
        self.sprites.append(pygame.image.load("images/water2.png"))
        self.sprites.append(pygame.image.load("images/water3.png"))

        self.count = self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

    def update(self):
        self.count += 0.04
        self.current_sprite += 0.04

        if self.count <= 3:
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]

            self.rect = self.image.get_rect(center = self.image.get_rect(topleft = [self.xplosion,self.yplosion]).center)
            settings.screen.blit(self.image, self.rect)

# This class draws the animation when the frog hits a car
class Dead(pygame.sprite.Sprite):
    def __init__(self, xplosion, yplosion):
        pygame.sprite.Sprite.__init__(self)
        self.xplosion = xplosion
        self.yplosion = yplosion

        self.sprites = []
        self.sprites.append(pygame.image.load("images/dead1.png"))
        self.sprites.append(pygame.image.load("images/dead2.png"))
        self.sprites.append(pygame.image.load("images/dead3.png"))
        self.sprites.append(pygame.image.load("images/dead4.png"))

        self.count = self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

    def update(self):
        self.count += 0.06
        self.current_sprite += 0.06

        if self.count <= 4:
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]

            self.rect = self.image.get_rect(center = self.image.get_rect(topleft = [self.xplosion,self.yplosion]).center)
            settings.screen.blit(self.image, self.rect)

        # return 1 if self.count != 4 else 0
