import pygame as py
from enum import Enum,unique
from math import sqrt
from random import randint
from qiqiaoban.angle import angle

class Color:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0,)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)


    def random_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class graph:
    color = Color()
    def __init__(self,size=()):
        self.draw(size)

        pass
    def running(self):
        running = True
        while running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    radius = randint(80, 120)
                    print(x, y, radius)
    def getDingdians(self):
        pass
    def draw(self,size=()):
        py.init()
        screen = py.display.set_mode(size)
        print(self.color.WHITE)

        py.display.set_caption('七巧板')
        screen.fill(self.color.WHITE)

        threeAngleDingdians=[]
        fourAngleDingdians=[]
        x=100
        y=100
        width=500

        threeAngleDingdians.append(((x,y),(x+width/2,y+width/2),(x,y+width)))
        threeAngleDingdians.append(((x,y),(x+width,y),(x+width/2,y+width/2)))
        threeAngleDingdians.append(((x,y+width),(x+width/2/2,y+width/2+width/2/2),(x+width/2,y+width)))
        threeAngleDingdians.append(((x+width/2,y+width),(x+width,y+width/2),(x+width,y+width)))
        threeAngleDingdians.append(((x+width/2,y+width/2),(x+width/2+width/2/2,y+width/2+width/2/2),(x+width/2+width/2/2,y+width/2/2)))
        fourAngleDingdians.append(((x+width/2,y+width/2),(x+width/2/2,y+width/2+width/2/2),(x+width/2,y+width),(x+width/2+width/2/2,y+width/2+width/2/2)))
        fourAngleDingdians.append(((x+width/2+width/2/2,y+width/2/2),(x+width/2+width/2/2,y+width/2+width/2/2),(x+width,y+width/2),(x+width,y)))
        angles = []
        for i in range(len(threeAngleDingdians)):
            angleSingle=angle(color=self.color.random_color(),dingdian=threeAngleDingdians[i])
            angles.append(angleSingle)
        for i in range(len(fourAngleDingdians)):
            angleSingle = angle(color=self.color.random_color(),dingdian=fourAngleDingdians[i])
            angles.append(angleSingle)
        for i in angles:
            i.draw(py=py,screen=screen)
        py.display.flip()
        self.running()

