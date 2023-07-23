from enum import Enum

import pygame
from Constructors.Printable import Printable
from Constructors.KeyBoardHandler import KeyBoardHandler
from Objects.Player1 import Player1, Direction
from Globals import Screen
    
class Player2(Player1):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.snake_skin = pygame.Surface((10,10))
        self.snake_skin.fill((255,211,58))

    def keyboard_handler(self, keyboard_event):
        if keyboard_event.key == pygame.K_UP:
            if self.movement != Direction.DOWN:
                self.movement = Direction.UP
        if keyboard_event.key == pygame.K_DOWN:
            if self.movement != Direction.DOWN:
                self.movement = Direction.DOWN
        if keyboard_event.key == pygame.K_LEFT:
            if self.movement != Direction.DOWN:
                self.movement = Direction.LEFT
        if keyboard_event.key == pygame.K_RIGHT:
            if self.movement != Direction.DOWN:
                self.movement = Direction.RIGHT

