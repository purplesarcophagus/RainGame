"""
Rain Game
    user moves a character along the bottom of the screen trying to catch raindrops that are not blue
"""
import pygame
from Background import Background
from Character import Character
from Raindrop import Raindrop

if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()

    pygame.display.set_caption("Catch 20 raindrops to win!")

    screenWidth, screenHeight = 1000, 1000
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    background = Background(screen)
    background.playRainSound()
    background.playJazz()

    frog = Character(screen)

    rainList = []

    THUNDER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(THUNDER_EVENT, 30000)

    CLOSE_MOUTH_EVENT = pygame.USEREVENT + 2
    pygame.time.set_timer(CLOSE_MOUTH_EVENT, 5000)

    RAINDROP_EVENT = pygame.USEREVENT + 3
    pygame.time.set_timer(RAINDROP_EVENT, 500)

    running = True
    while running:
        if frog.score == 20:
            background.rainSounds.stop()
            background.thunderSound.stop()
            rainList = []
        for event in pygame.event.get():
            if event.type == RAINDROP_EVENT:
                rainList.append(Raindrop(screen))
            if event.type == THUNDER_EVENT:
                background.playThunderSound()
            if event.type == CLOSE_MOUTH_EVENT:
                frog.closeMouth()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                match event.key:
                    case pygame.K_ESCAPE:
                        running = False
                    case pygame.K_a:
                        frog.startMovement("left")
                    case pygame.K_d:
                        frog.startMovement("right")
                    case pygame.K_SPACE:
                        frog.openMouth()
                        if frog.score == 20:
                            frog.croak.play()
            if event.type == pygame.KEYUP:
                frog.stopMovement()

        frog.movement()
        background.showBackground(frog)
        frog.showCharacter()
        background.showScore(frog)

        for drop in rainList:
            if drop.rainRect.bottom >= 940 or frog.catchRain(drop):
                rainList.remove(drop)
            else:
                drop.makeRain()

        pygame.display.flip()

        clock.tick(60)
