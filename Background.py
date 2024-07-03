"""
Background class
    __init__
        cloudSurface: Surface, cloudRect: Rect, groundSurface: Surface, groundRect: Rect
    showBackground()
        blits cloud and ground
    thunder()
        plays thunder sound every 15-30 seconds (randomly generated)
    rainSound()
        plays rain sound on game start 
    music()
        plays cool jazz music when game is won 
"""
import pygame

from Character import Character


class Background:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.cloudImage = pygame.image.load("cloud.png").convert()
        self.cloudRect = self.cloudImage.get_rect(center=(500, 230))

        self.groundImage = pygame.image.load("grass.png").convert()
        self.groundRect = self.groundImage.get_rect(bottom=screen.get_height()+100)

        self.sunImage = pygame.image.load("sunny day.png").convert()
        self.sunImage = pygame.transform.scale(self.sunImage, (1000, 1000))
        self.sunRect = self.sunImage.get_rect()

        self.font = pygame.font.Font(None, 27)

        self.rainSounds = pygame.mixer.Sound("Rain Loop 1245.wav")
        self.thunderSound = pygame.mixer.Sound("Big Thunder Rumble.wav")
        self.jazz = pygame.mixer.Sound("jazz.mp3")

    def showBackground(self, frog: Character):
        if frog.score == 20:
            self.screen.blit(self.sunImage, self.sunRect)
        else:
            self.screen.blit(self.cloudImage, self.cloudRect)
            self.screen.blit(self.groundImage, self.groundRect)

    def showScore(self, frog: Character):
        scoreText = self.font.render("Score: " + str(frog.score), True, (255, 255, 255))
        self.screen.blit(scoreText, (0, 0))
        if frog.score == 20:
            winText = self.font.render("Wow! You win!", True, (255, 255, 255))
            self.screen.blit(winText, (420, 690))

    def playRainSound(self):
        self.rainSounds.set_volume(.1)
        self.rainSounds.play(loops=1000000)

    def playThunderSound(self):
        self.thunderSound.set_volume(.1)
        self.thunderSound.play()

    def playJazz(self):
        self.jazz.set_volume(.3)
        self.jazz.play(loops=1000000)