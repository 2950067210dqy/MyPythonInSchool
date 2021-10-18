class player():
    # 手牌
    hand=[]
    def __init__(self):
        self.hand=[]
    # 得牌
    def getPoke(self,poke):
        self.hand.append(poke)
