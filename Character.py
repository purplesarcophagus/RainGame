"""
Character class
    __init__
        char: Surface, charRect: Rect, charOpenMouth: Surface, charOpenMouthRect: Rect, score: int, speed[]: [int, int],
        mouthOpen: bool, successSound
    showCharacter(screen: Surface)
        blits character to screen
    movement(direction: str)
        allows character to move left and right with L or R arrow keys or A and D keys
        flips image of character to face correct direction
    openMouth(open: bool)
        opens character's mouth when space bar is pressed
    playSuccessSound()
        plays success sound when correct rain is caught
    catchRain(Raindrop) -> bool
        adds to score when a non-blue raindrop is caught with open mouth
"""
import pygame.image

from Raindrop import Raindrop


class Character:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.frogImage = "frog.png"
        self.frogOpenImage = "frogOpen.png"

        self.mouthOpen = False

        self.frog = pygame.image.load(self.frogImage)
        self.frogRect = self.frog.get_rect(topleft=(0, 910))

        self.score = 0

        self.speed = [0, 0]
        self.directions = {"left": False, "right": False}

        self.croak = pygame.mixer.Sound("croak.mp3")

    def showCharacter(self):
        self.screen.blit(self.frog, self.frogRect)

    def startMovement(self, direction: str):
        match direction:
            case "left":
                self.directions["left"] = True
            case "right":
                self.directions["right"] = True

    def stopMovement(self):
        self.directions["left"], self.directions["right"] = False, False

    def movement(self):
        if self.directions["left"]:
            self.speed[0] = -5
        elif self.directions["right"]:
            self.speed[0] = 5
        else:
            self.speed[0] = 0

        if self.frogRect.left <= 0:
            self.directions["left"] = False
        elif self.frogRect.right >= self.screen.get_width():
            self.directions["right"] = False

        self.frogRect = self.frogRect.move(self.speed)
        self.screen.fill((0, 0, 0))

    def openMouth(self):
        if self.mouthOpen:
            self.frog = pygame.image.load("frog.png")
            self.mouthOpen = False
        else:
            self.frog = pygame.image.load("frogOpen.png")
            self.mouthOpen = True

    def closeMouth(self):
        self.frog = pygame.image.load("frog.png")
        self.mouthOpen = False

    def catchRain(self, drop: Raindrop):
        if self.frogRect.colliderect(drop.rainRect) and self.mouthOpen:
            self.score += 1
            self.croak.play()
            return True
