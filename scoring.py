import pygame, sys, time
import settings


#This class displays the health remaining
class Health(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.image = pygame.image.load("images/life.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.draw()

    def draw(self):
        settings.screen.blit(self.image, (self.x_pos, self.y_pos))

#This class diplays and manage the score and the levels
class Score:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 28)
        self.level = 1
        self.score = 0

    def update(self):
        self.img = self.font.render("SCORE", True, (200, 200, 200))
        self.img1 = self.font.render(str(self.score), True, (200, 200, 200))

        self.img2 = self.font.render("LEVEL", True, (200, 200, 200))
        self.img3 = self.font.render(str(self.level), True, (200, 200, 200))
        self.drawbar()

    def add(self, score):
        self.score += score

    def level_up(self):
        self.level += 1

    def drawbar(self):
        settings.screen.blit(self.img, (10, 10))
        settings.screen.blit(self.img1, (100, 10))
        settings.screen.blit(self.img2, (340, 10))
        settings.screen.blit(self.img3, (420, 10))


#This class draws and manage the time elements
class Time:
    def __init__(self):
        self.start_ticks=pygame.time.get_ticks()
        self.font = pygame.font.SysFont(None, 28)
        self.timeisover = 0
        self.pos_x = 330

    def update(self):
        self.seconds=(pygame.time.get_ticks()-self.start_ticks)/1000
        self.img = self.font.render("TIME", True, (200, 200, 200))
        self.drawbar()

    def drawbar(self):
        self.pos_x -= 0.3
        if self.pos_x < 0:
            self.timeisover = 1
            self.pos_x = 330
        pygame.draw.rect(settings.screen, (200, 200, 200), pygame.Rect(0, 502, self.pos_x, 20))
        settings.screen.blit(self.img, (380, 504))
