import pygame, sys, time

def init():

    pygame.init()
    
    global screen_width
    screen_width  = 448

    global screen_height
    screen_height = 530

    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Frogger, v1.0 by_ Hugo Picquet")
