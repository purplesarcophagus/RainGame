"""
Raindrop Class
    __init__
        rainSurface: Surface, rainRect: Rect, rainColor: (int, int, int), rainSpeed[]: [int, int]
    makeRain()
        randomly spawns rain drops either (0, 0, 255) or (0-255, 0-255, 0)
        makes rain fall
    showRain()
        blits raindrops
"""
import pygame
import random


class Raindrop:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.randxPosition = random.randint(150, 800)
        self.rainRect = pygame.Rect(self.randxPosition, 400, 3, 5)
        self.rainSurface = pygame.Surface((self.rainRect.w, self.rainRect.h))

        self.blue = (0, 150, 150)
        self.rainSurface.fill(self.blue)

        self.rainSpeed = [0, 5]

    def makeRain(self):
        self.rainRect = self.rainRect.move(self.rainSpeed)
        self.screen.blit(self.rainSurface, self.rainRect)

