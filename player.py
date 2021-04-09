import pygame, sys, time
import settings

# This class contains all the frog functions
class Frog(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.x = 0
        self.dead_state = 0
        self.sprites = []
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_moving = False

        self.check = self.angleprev = self.current_sprite = 0
        self.sprites.append(pygame.image.load("images/frog1.png"))
        self.sprites.append(pygame.image.load("images/frog2.png"))
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

    # Reset the positon of the frog
    def reset(self):
        #if self.x == 100:
        #    self.x = 0
        self.pos_x = 200
        self.pos_y = 449
        #self.x = self.x + 1

    # Hide the frog until the animation is done
    def hide(self):
        self.pos_x = 20000
        self.pos_y = 20000
        self.image = self.sprites[int(self.current_sprite)]
        self.rect = self.image.get_rect(center = self.image.get_rect(topleft = [self.pos_x,self.pos_y]).center)
        settings.screen.blit(self.image, self.rect)

    # Change the state of the frog when moving
    def move(self):
        self.is_moving = True

    # Attach the frog to an object, wood or turtle
    def attach(self, speed, type):
        if type == "wood":
            self.pos_x = self.pos_x + speed
        if type == "turtle":
            self.pos_x = self.pos_x - speed*2

    # Update the frog when moving, create the frog animation
    def update(self):
        if self.is_moving == True:
            if self.key == "UP":
                self.pos_y = self.pos_y - 33
                self.rotate_the_frog(1, 0, 4, 90, 3, -90, 2, 180)
            if self.key == "DOWN":
                self.pos_y = self.pos_y + 33
                self.rotate_the_frog(2, 180, 4, -90, 3, 90, "x", "x")
            if self.key == "LEFT":
                self.pos_x = self.pos_x - 33
                self.rotate_the_frog(3, 90, 2, -90, 4, 180, "x", "x")
            if self.key == "RIGHT":
                self.pos_x = self.pos_x + 33
                self.rotate_the_frog(4, -90, 2, 90, 3, -180, "x", "x")

            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_moving = False

        if self.dead_state == 0:
            self.image = self.sprites[int(self.current_sprite)]
            self.rect = self.image.get_rect(center = self.image.get_rect(topleft = [self.pos_x,self.pos_y]).center)
            settings.screen.blit(self.image, self.rect)
        else:
            self.reset()

    #Rotate the frog in the right way when moving, it depends on the previous move
    def rotate_the_frog(self, move_id, default_angle, id1, angle1, id2, angle2, id3, angle3):
        self.rect.topleft = [self.pos_x,self.pos_y]
        self.angle = default_angle

        if self.check is id1:
            self.angle = angle1
        if self.check is id2:
            self.angle = angle2
        if self.check is id3:
            self.angle = angle3

        if self.check is not move_id:
            self.rotate()
        self.check = move_id

        self.key = 0
        pygame.time.wait(10)

    def rotate(self):
        self.sprites[0] = pygame.transform.rotate(self.sprites[0], self.angle)
        self.sprites[1] = pygame.transform.rotate(self.sprites[1], self.angle)
        self.check = 0
