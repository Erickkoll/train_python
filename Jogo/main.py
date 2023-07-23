import pygame
from pygame.constants import *

from Globals import Screen
from Constructors.Printable import Printable
from Constructors.KeyBoardHandler import KeyBoardHandler
from Constructors.CollisionObject import CollisionObject
Screen.init()
screen = Screen.screen
from Objects.Player1 import Player1
from Objects.Player2 import Player2

obj_list = list()
obj_list.append(Player1(100,100))
obj_list.append(Player2(200,200))

clock = pygame.time.Clock()

while not Screen.scene_done:
    clock.tick(10)
    screen.fill((0,0,0))


    for event in pygame.event.get():
        if event.type == QUIT:
            Screen.scene_done = True
        if event.type == pygame.KEYDOWN:
            for obj in obj_list:
                if isinstance(obj, KeyBoardHandler):
                    obj.keyboard_handler(event)
   
    for obj in obj_list:
        for obj2 in obj_list:
            if obj != obj2:
                if isinstance(obj,CollisionObject) and isinstance(obj2,CollisionObject):
                    for pos1 in obj.getPos():
                        for pos2 in  obj2.getPos():
                            if pos1 == pos2:
                                obj.onCollision(obj2)
            else:
                list_repeat = []
                for pos1 in obj.getPos():
                    if pos1 in list_repeat:
                        obj.onCollision(obj)
                        break
                    list_repeat.append(pos1)
    for obj in obj_list:
        if isinstance(obj, Printable):
            obj.print()
            
    pygame.display.update()
    
pygame.quit()
