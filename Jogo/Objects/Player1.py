from enum import Enum

import pygame
from Constructors.Printable import Printable
from Constructors.KeyBoardHandler import KeyBoardHandler
from Constructors.CollisionObject import CollisionObject
from Globals import Screen

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    
class Player1(Printable, KeyBoardHandler, CollisionObject):
    def __init__(self, x, y):
        super().__init__()
        self.snake_pos = [(x,y)]
        self.snake_skin = pygame.Surface((10,10))
        self.snake_skin.fill((51,119,170))
        self.movement = Direction.UP

    def print(self):
        if self.movement == Direction.UP:
            self.snake_pos.append((self.snake_pos[-1][0],self.snake_pos[-1][1] - 10))
        if self.movement == Direction.DOWN:
            self.snake_pos.append((self.snake_pos[-1][0],self.snake_pos[-1][1] + 10))
        if self.movement == Direction.LEFT:
            self.snake_pos.append((self.snake_pos[-1][0]  - 10,self.snake_pos[-1][1]))
        if self.movement == Direction.RIGHT:
            self.snake_pos.append((self.snake_pos[-1][0]  + 10,self.snake_pos[-1][1]))

        for body_pos in self.snake_pos:
            Screen.screen.blit(self.snake_skin, body_pos)

    def keyboard_handler(self, keyboard_event):
        if keyboard_event.key == pygame.K_w:
            if self.movement != Direction.DOWN:
                self.movement = Direction.UP
        if keyboard_event.key == pygame.K_s:
            if self.movement != Direction.UP:
                self.movement = Direction.DOWN
        if keyboard_event.key == pygame.K_a:
            if self.movement != Direction.RIGHT:
                self.movement = Direction.LEFT
        if keyboard_event.key == pygame.K_d:
            if self.movement != Direction.LEFT:
                self.movement = Direction.RIGHT

    def getPos(self):
        return self.snake_pos

    def onCollision(self, otherObject):
        if isinstance(otherObject, Player1):
            if self == otherObject:
                print(self.__class__.__name__ + " perdeu")
            else:
                print(otherObject.__class__.__name__+" perdeu")
        Screen.scene_done = True
