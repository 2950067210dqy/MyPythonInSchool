from zipai.player import player
import random
class poke():
    # 一副牌
    AllPokesPair=2
    AllPokes=54#54张牌
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]  # 牌面数字 1--13
    SUITS = ["梅花", "方钻", "红心", "黑桃"]  # 梅为梅花，方为方钻，红为红心，黑为黑桃
    Ghost=["大王","小王"]
    #当前牌堆
    pokes=[]
    def __init__(self):
        self.initPoke()
        self.washPoke()
        pass
    # 洗牌
    def washPoke(self):
        random.shuffle(self.pokes)
    # 生成标准牌堆
    def initPoke(self):
        for i in range(self.AllPokesPair):
            for j in self.SUITS:
                for k in self.RANKS:
                    self.pokes.append(str(j)+str(k))
            for l in self.Ghost:
                self.pokes.append(l)
    # 发牌
    def setPoke(self,players):
        for i in range(len(self.pokes)):
            if (i % 4 == 0):
                players[0].getPoke(self.pokes[i])
            if (i % 4 == 1):
                players[1].getPoke(self.pokes[i])
            if (i % 4 == 2):
                players[2].getPoke(self.pokes[i])
            if (i % 4 == 3):
                players[3].getPoke(self.pokes[i])

