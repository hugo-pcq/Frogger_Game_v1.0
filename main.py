import pygame, sys, time

from player import *
from obstacles import *
from animations import *
from scoring import *

import settings
clock = pygame.time.Clock()

# Game, the main class
class Game:
    # We mostly define default objects or group of objects in this function
    def __init__(self):
        self.background_image = pygame.image.load("images/back.png")
        self.background_menu = pygame.image.load("images/backtxt.png")

        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites1 = pygame.sprite.Group()

        self.x_housepositiondefault = ["x_pos", 15, 111, 207, 303, 399]

        self.turtle1, self.turtle2, self.turtle3, self.turtle4 = Turtle(400, 116, 0.4, 1, 94), Turtle(100, 116, 0.4, 1, 94), Turtle(400, 215, 0.2, 2, 139),  Turtle(100, 215, 0.2, 2, 139)
        self.moving_sprites.add(self.turtle1), self.moving_sprites.add(self.turtle2), self.moving_sprites.add(self.turtle3), self.moving_sprites.add(self.turtle4)

        self.wood1, self.wood2, self.wood3, self.wood4, self.wood5, self.wood6, self.wood7 = Wood(100, 83, 0.8, 1, 95), Wood(350, 83, 0.8, 1, 95), Wood(0, 149, 1, 2, 139), Wood(280, 149, 1, 2, 139), Wood(-50, 182, 0.5, 3, 70), Wood(150, 182, 0.5, 3, 70), Wood(350, 182, 0.5, 3, 70)
        self.objects = [self.wood1, self.wood2, self.wood3, self.wood4, self.wood5,self.wood6, self.wood7, self.turtle1, self.turtle2, self.turtle3, self.turtle4]

        self.car1, self.car2, self.car3, self.car4, self.car5, self.car6, self.car7, self.car8, self.car8, self.car9, self.car10, self.car11, self.car12  = Car(100, 413, 0.8, 1, 36), Car(250, 413, 0.8, 1, 36), Car(400, 413, 0.8, 1, 36), Car(0, 380, 1, 2, 47), Car(200, 380, 1, 2, 47), Car(600, 380, 1, 2, 47), Car(0, 347, 1, 4, 37), Car(200, 347, 1, 4, 37), Car(600, 347, 1, 4, 37),  Car(400, 314, 0.6, 5, 36), Car(50, 314, 0.6, 5, 36), Car(450, 281, 0.7, 3, 81),Car(200, 281, 0.7, 3,81)
        self.objectscar = [self.car1, self.car2, self.car3, self.car4, self.car5, self.car6, self.car7, self.car8, self.car9, self.car10, self.car11, self.car12]
        ##########################################################################################################################

        self.health1,self.health2 = Health(10, 484), Health(30, 484)
        self.moving_sprites.add(self.health1)
        self.moving_sprites.add(self.health2)

        self.init()

    # These variables are defined separately, this function is called in the __init__ method but
    # these specific variables are re-initiated when the game is over and when the game restart
    def init(self):
        self.attach = []

        self.time = Time()
        self.score = Score()

        self.vel, self.pos_x, self.pos_y = 23, 200, 449
        self.count = self.counthouse = self.counthouse_previous = 0

        self.frog = Frog(self.pos_x, self.pos_y)
        self.moving_sprites.add(self.frog)

        self.x_housepositionupdated = ["x_pos", 0, 0, 0, 0, 0]

        self.counthealth = self.ishome = 0
        self.show_image = self.run = False
        self.running = True


    # Small function that clear the screen and draw the backround
    def draw_background(self):
        settings.screen.fill((0, 0, 0))
        settings.screen.blit(self.background_image, (0, 32))
        self.draw()

    # The execute function is divided in 2 parts
    def execute(self):
        self.font = pygame.font.Font(None, 28)

        self.black = pygame.image.load("images/black.png")
        self.imagehealth = pygame.image.load("images/life.png")

        self.text = self.font.render("PRESS SPACE KEY TO START", True, (200, 200, 200))
        self.img = self.font.render("SCORE", True, (200, 200, 200))
        self.img1 = self.font.render("0", True, (200, 200, 200))
        self.img2 = self.font.render("LEVEL", True, (200, 200, 200))
        self.img3 = self.font.render("1", True, (200, 200, 200))
        self.imgtime = self.font.render("TIME", True, (200, 200, 200))
        self.imggameover = self.font.render("GAME OVER", True, (200, 200, 200))
        settings.screen.blit(self.imggameover, (140, 300))

        # This is the main loop of the program
        # if self.running is set to false, the game stops
        while self.running:
            # First Part: Playing Mode
            if self.run == True:
                self.draw_background()

                for event in pygame.event.get():
                    self.event( event )

                self.draw()
                self.time.update()
                self.score.update()
                pygame.display.flip()
                clock.tick(60)

            #Second Part: Menu Mode, wait for the user to press ESCAPE and start a game
            elif self.run == False:
                keys = pygame.key.get_pressed()

                settings.screen.fill((0, 0, 0))
                settings.screen.blit(self.background_menu, (0, 32))
                settings.screen.blit(self.img, (10, 10))
                settings.screen.blit(self.img1, (100, 10))
                settings.screen.blit(self.img2, (340, 10))
                settings.screen.blit(self.img3, (420, 10))
                settings.screen.blit(self.imgtime, (380, 504))

                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        self.running = False
                    if keys[pygame.K_SPACE]:
                        self.run = True

                if self.show_image:
                    pygame.time.wait(50)
                    settings.screen.blit(self.text, (77, 310))
                    self.show_image = False
                else:
                    pygame.time.wait(100)
                    settings.screen.blit(self.black, (77, 310))
                    self.show_image = True

                pygame.display.flip()
                clock.tick(60)

        self.cleanup()

    # This function listens for the keystrokes, and manage according actions, such as moving the frog or starting a new game
    def event(self, event):
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            self.running = False

        if keys[pygame.K_SPACE]:
            self.run = True

        # This variable, self.frog.dead_state, is used to delay the apparation of the frog after an animaiton
        if (self.frog.dead_state == 0) and (keys[pygame.K_UP]) and self.frog.pos_y>0:
            self.event_actions("UP")
        if (self.frog.dead_state == 0) and (keys[pygame.K_DOWN]) and self.frog.pos_y<449-self.vel:
            self.event_actions("DOWN")
        if (self.frog.dead_state == 0) and (keys[pygame.K_LEFT]) and self.frog.pos_x>0:
            self.event_actions("LEFT")
        if (self.frog.dead_state == 0) and (keys[pygame.K_RIGHT]) and self.frog.pos_x<449-self.vel:
            self.event_actions("RIGHT")

    # Part of the previous function, the frog is drawn according to the KEY(RIGHT,DOWN...)
    def event_actions(self, key):
        self.frog.key = key
        self.frog.move()
        self.frog.update()

    # These functions are calling the rest of the code
    def draw(self):
        self.draw_wood_and_turtles()
        self.draw_cars_or_crash_animation()
        self.draw_house_or_water_animation()
        self.update_time_health_and_levels()


    # Here we draw the objects wood and turtles and check if the frog intersects with one of this object
    def draw_wood_and_turtles(self):
        x = 10 # Number of objects
        #Iterate through the list of objects
        while x >= 0: #As soon as x = 0, the loop stops
            self.objects[x].update()
            # To check if the frog intersects with an object, we append 1 to a list if frog intersects with an object, 0 if not
            if self.frog.rect[0] >= self.objects[x].x_pos and self.frog.rect[0] <= self.objects[x].x_pos+self.objects[x].pxsize and self.frog.rect[1]-3 == self.objects[x].y_pos:
                if self.objects[x].type == "wood":
                    # Here we attach the frog to the object with self.frog.attach
                    self.frog.attach(self.objects[x].speed, "wood")
                elif self.objects[x].type == "turtle":
                    self.frog.attach(self.objects[x].speed, "turtle")
                self.attach.append("1")
            else:
                self.attach.append("0")
            x = x - 1

    # Here we draw the objects cars, and check if the frog intersects with a car
    def draw_cars_or_crash_animation(self):
        x = 11 #Number of objects, here objects
        #Iterate through the list of objects
        # dead = 0
        while x >= 0: #As soon as x = 0, the loop stops
            self.objectscar[x].update()
            # if the frog intersects with a car, we draw the animation and create a delay in the apparation of the new frog
            if self.frog.rect[0] >= self.objectscar[x].x_pos and self.frog.rect[0] <= self.objectscar[x].x_pos+self.objectscar[x].pxsize and self.frog.rect[1]-3 == self.objectscar[x].y_pos:
                self.explosion = Dead(self.frog.rect[0], self.frog.rect[1])
                self.moving_sprites1.add(self.explosion)
                self.counthealth += 1
                self.frog.dead_state = 1
                self.frog.hide()
            x = x - 1
        # This is how the delay is added
        if (self.frog.dead_state != 0) and (self.frog.dead_state < 90): self.frog.dead_state += 1
        elif self.frog.dead_state >= 90:
            self.frog.reset()
            self.frog.dead_state = 0

    # In this function we check if the frog is in an upper slot, if there is not a frog already, in this case we draw a house
    # We also check when the frog is in the river part, the frog has to be on an object, otherwise it means the frog is in the water
    def draw_house_or_water_animation(self):
        if self.frog.rect[1] <83 and self.pos_y != 449:#178 + 32

            self.ishome = 0
            # Check Slot 1
            if self.frog.rect[0] > 5 and self.frog.rect[0] < 45 and self.x_housepositionupdated[1] == 0:
                self.x_housepositionupdated[1] = self.x_housepositiondefault[1]
                self.house1 = House(self.x_housepositiondefault[1], 50)
                self.moving_sprites.add(self.house1)
                self.score.add(100)
                self.counthouse += 1
                self.ishome = 1
            # Check Slot 2
            elif self.frog.rect[0] > 95 and self.frog.rect[0] < 140 and self.x_housepositionupdated[2] == 0:
                self.x_housepositionupdated[2] = self.x_housepositiondefault[2]
                self.house2 = House(self.x_housepositiondefault[2], 50)
                self.moving_sprites.add(self.house2)
                self.score.add(100)
                self.counthouse += 1
                self.ishome = 1
            # Check Slot 3
            elif self.frog.rect[0] > 190 and self.frog.rect[0] < 235 and self.x_housepositionupdated[3] == 0:
                self.x_housepositionupdated[3] = self.x_housepositiondefault[3]
                self.house3 = House(self.x_housepositiondefault[3], 50)
                self.moving_sprites.add(self.house3)
                self.score.add(100)
                self.counthouse += 1
                self.ishome = 1
            # Check Slot 4
            elif self.frog.rect[0] > 290 and self.frog.rect[0] < 335 and self.x_housepositionupdated[4] == 0:
                self.x_housepositionupdated[4] = self.x_housepositiondefault[4]
                self.house4 = House(self.x_housepositiondefault[4], 50)
                self.moving_sprites.add(self.house4)
                self.score.add(100)
                self.counthouse += 1
                self.ishome = 1
            # Check Slot 5
            elif self.frog.rect[0] > 390 and self.frog.rect[0] < 435 and self.x_housepositionupdated[5] == 0:
                self.x_housepositionupdated[5] = self.x_housepositiondefault[5]
                self.house5 = House(self.x_housepositiondefault[5], 50)
                self.moving_sprites.add(self.house5)
                self.score.add(100)
                self.counthouse += 1
                self.ishome = 1

            # if the frog is in the slot section but haven't been in one of the 5 conditions before
            if self.ishome == 0:
                # It means the frog dies because it hits the wall or went in an already used spot
                self.dead = Dead(self.frog.rect[0], self.frog.rect[1])
                self.moving_sprites1.add(self.dead)
                self.counthealth += 1
                self.frog.reset()

        # Here we check if the frog is on a wood or a turtle
        elif self.frog.rect[1] < 243:
            count = 0
            for z in self.attach:
                if z == "0":
                    count += 1
                    # if there is only 0 in attach list, it means the frog is in the water
                    if count == len(self.objects) and self.frog.rect[1] is not 0:
                        self.explosion = Explosion(self.frog.rect[0], self.frog.rect[1])
                        self.moving_sprites1.add(self.explosion)
                        self.counthealth += 1
                        self.frog.dead_state = 1
                        self.frog.hide()

            count = 1
            if (self.frog.dead_state != 0) and (self.frog.dead_state < 90): self.frog.dead_state += 1
            elif self.frog.dead_state >= 90:
                self.frog.reset()
                self.frog.dead_state = 0

    # In this function we check the number of lives remaning for the frog
    def update_time_health_and_levels(self):
        # if the time is over and the frog hasn't been into a new slot, you lose a live
        if self.counthouse == self.counthouse_previous:
            if self.time.timeisover == 1:
                self.time.timeisover = 0
                self.counthealth += 1

            # if the frog has lost a live
            if self.counthealth == 1 and self.count == 0:
                self.count = 1
                self.moving_sprites.remove(self.health2)
                self.time.pos_x = 330
                self.frog.reset()
            # if the frog has lost two lives
            elif self.counthealth == 2 and self.count == 1:
                self.count = 2
                self.moving_sprites.remove(self.health1)
                self.time.pos_x = 330
            # if the frog has lost three lives
            elif self.counthealth == 3  and self.count == 2 and self.frog.dead_state == 0:
                self.count = 3
                self.game_over()

        # if the frog has been into a valid slot
        if self.counthouse > self.counthouse_previous:
            self.time.pos_x = 330
            self.frog.reset()

        # if the 5 slots are filled with frogs
        if self.counthouse == 5:
            self.score.add(1000)
            self.score.level_up()
            self.counthouse = self.counthouse_previous = 0
            self.x_housepositionupdated = ["x_pos", 0, 0, 0, 0, 0]
            self.moving_sprites.remove(self.house1, self.house2, self.house3, self.house4, self.house5)

        self.counthouse_previous = self.counthouse

        self.pos_y = self.frog.rect[1]
        self.attach = []
        self.moving_sprites.update()
        self.moving_sprites1.update()

    # This function is called when the player has no more lives
    def game_over(self):

        count = 0
        data = [0, 1, 2, 3, 4, 5]
        self.moving_sprites.remove(self.frog)
        for x in self.x_housepositionupdated:

            if x == "x_pos" or x == 0:
                pass
            else:
                if data[count] == 1:
                    self.moving_sprites.remove(self.house1)
                if data[count] == 2:
                    self.moving_sprites.remove(self.house2)
                if data[count] == 3:
                    self.moving_sprites.remove(self.house3)
                if data[count] == 4:
                    self.moving_sprites.remove(self.house4)
                if data[count] == 5:
                    self.moving_sprites.remove(self.house5)
            count = count + 1

        self.init()
        self.moving_sprites.add(self.health1)
        self.moving_sprites.add(self.health2)

        settings.screen.fill((0, 0, 0))
        self.font = pygame.font.Font(None, 38)
        settings.screen.blit(self.background_menu, (0, 32))
        settings.screen.blit(self.img, (10, 10))
        settings.screen.blit(self.img1, (100, 10))
        settings.screen.blit(self.img2, (340, 10))
        settings.screen.blit(self.img3, (420, 10))
        settings.screen.blit(self.imgtime, (380, 504))

        self.imggameover = self.font.render("GAME OVER", True, (200, 200, 200))
        settings.screen.blit(self.imggameover, (140, 300))

        self.deadfrog = self.image = pygame.image.load("images/deadfrog.png")
        settings.screen.blit(self.deadfrog, (185, 345))

        pygame.display.flip()
        pygame.time.wait(3000)

    def cleanup(self):
        pygame.quit()
        quit()

# Here the main logic is called, when we launch the program this is the first action performed
if __name__ == "__main__":
    settings.init()
    FroggerGame = Game()
    FroggerGame.execute()
