import pygame, sys
from settings import *
from level import Level


class Background:
    def __init__(self, sprite):
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.posX = 0
        self.posY = 0

    def draw(self, surface):
        for x in range(-self.rect.width, WIDHT+self.rect.width, self.rect.width):
            for y in range(-self.rect.height, HEIGHT+self.rect.height, self.rect.height):
                surface.blit(self.sprite, (x + self.posX, y + self.posY))

    def move(self, x, y):
        self.posX += x
        self.posY += y
        if self.posX >= self.rect.width or self.posX <= -self.rect.width:
            self.posX %= self.rect.width
        if self.posY >= self.rect.height or self.posY <= -self.rect.height:
            self.posY %= self.rect.height
