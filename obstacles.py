import pygame, sys, time
import settings

class Turtle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, speed, size, pxsize):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.pxsize = pxsize
        self.size = size
        self.type = "turtle"

        self.sprites = []

        self.current_sprite = 0

        if self.size == 1:
            self.sprites.append(pygame.image.load("images/twoturtles1.png"))
            self.sprites.append(pygame.image.load("images/twoturtles2.png"))
            self.sprites.append(pygame.image.load("images/twoturtles3.png"))
        if self.size == 2:
            self.sprites.append(pygame.image.load("images/threeturtles1.png"))
            self.sprites.append(pygame.image.load("images/threeturtles2.png"))
            self.sprites.append(pygame.image.load("images/threeturtles3.png"))

        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()


    def update(self):
        self.x_pos -= self.speed
        if self.x_pos < -150:
            self.x_pos = 500
        self.current_sprite += 0.05

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

        self.rect = self.image.get_rect(center = self.image.get_rect(topleft = [self.x_pos,self.y_pos]).center)
        settings.screen.blit(self.image, self.rect)



class Car(pygame.sprite.Sprite):
    def __init__(self,  x_pos, y_pos, speed, size, pxsize):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.pxsize = pxsize
        self.size = size

        if self.size == 1:
            self.image = pygame.image.load("images/car1.png")
        if self.size == 2:
            self.image = pygame.image.load("images/car2.png")
        if self.size == 3:
            self.image = pygame.image.load("images/car3.png")
        if self.size == 4:
            self.image = pygame.image.load("images/car4.png")
        if self.size == 5:
            self.image = pygame.image.load("images/car5.png")

        self.rect = self.image.get_rect()


    def update(self):
        if self.x_pos > 450:
            self.x_pos = -150

        if self.x_pos < -150:
            self.x_pos = 450

        if self.size == 1:
            self.x_pos -= self.speed
        if self.size == 2:
            self.x_pos += self.speed
        if self.size == 3:
            self.x_pos -= self.speed
        if self.size == 4:
            self.x_pos -= self.speed
        if self.size == 5:
            self.x_pos += self.speed


        self.draw(self.x_pos, self.y_pos, self.image)


    def draw(self, x, y, image):
        settings.screen.blit(image, (x, y))


class Wood(pygame.sprite.Sprite):
    def __init__(self,  x_pos, y_pos, speed, size, pxsize):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.pxsize = pxsize
        self.size = size
        self.type = "wood"

        if self.size == 1:
            self.woodpic = pygame.image.load("images/wood1.png")
        if self.size == 2:
            self.woodpic = pygame.image.load("images/wood2.png")
        if self.size == 3:
            self.woodpic = pygame.image.load("images/wood3.png")

        self.rect = self.woodpic.get_rect()


    def update(self):
        if self.x_pos > 450:
            self.x_pos = -150
        self.x_pos += self.speed

        self.draw(self.x_pos, self.y_pos, self.woodpic)


    def draw(self, x, y, image):
        settings.screen.blit(image, (x, y))


class House(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.image = pygame.image.load("images/house.png")

        self.rect = self.image.get_rect()

    def update(self):
        self.draw()

    def draw(self):
        settings.screen.blit(self.image, (self.x_pos, self.y_pos))
