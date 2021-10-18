class angle:
    def __init__(self,color,dingdian):
        self.dingdian=dingdian
        self.color = color

    def draw(self,py,screen):
        py.draw.polygon(screen,self.color,self.dingdian,0)
        pass
