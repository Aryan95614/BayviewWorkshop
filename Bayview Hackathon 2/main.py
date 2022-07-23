import pygame, os
import sys

pygame.init()

SIZE = (800, 800)

class Window():

    def __init__(self):
        self.window = pygame.display.set_mode(SIZE)
        self.gameover = False
        self.keys = None
        self.backgroundImage = pygame.image.load(os.path.join("assets", "Background.jpg"))
        self.backX = -400
        self.backY = 0


    def update(self):
        self.window.blit(self.backgroundImage, (self.backX, self.backY))


    def game_loop(self):
        while not self.gameover:
            self.keys = pygame.key.get_pressed()
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover = True
                if self.keys[pygame.K_a]:
                    self.backX += 2
                if self.keys[pygame.K_d]:
                    self.backX -= 2
                if self.keys[pygame.K_w]:
                    self.backY -= 2
                if self.keys[pygame.K_s]:
                    self.backY += 2

            pygame.display.update()


window = Window()
window.game_loop()