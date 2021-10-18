import pygame
from New202109.NetworkGame.GameClass.Map.Map import Map
class Flash:
    screen=None
    img=None
    def __init__(self,width=600,height=400):
        self.done=False
        pygame.init()
        self.draw(width,height)
    def draw(self,width,height):
        self.screen=pygame.display.set_mode((width,height))
        self.img=pygame.image.load(r"1.png")
        self.loop()

    def loop(self):
        while not self.done:
            self.screen.blit(self.img,(0,0))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

