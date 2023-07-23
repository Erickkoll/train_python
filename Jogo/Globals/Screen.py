import pygame

screen = None
scene_done = None

def init():
    global screen
    global scene_done
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    scene_done = False
