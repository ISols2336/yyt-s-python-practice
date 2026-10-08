#知识点：Enum 枚举、魔法方法 __repr__ 与 __lt__、@property、类的组合
#扑克牌练习：造一副牌 → 洗牌 → 发牌 → 整理手牌

from enum import Enum


class Suite(Enum):
    #花色：用枚举定义，HEART=0、SPADE=1、CLUB=2、DIAMOND=3
    HEART, SPADE, CLUB, DIAMOND = range(4)


for i in Suite:
    print(f'{i}:{i.value}')      #打印每个花色和它的编号


class Card:
    #一张牌：由"花色 + 点数"组成

    def __init__(self,suite,num):
        self.suite = suite       #花色（Suite 枚举）
        self.num = num           #点数（1~13）

    def __repr__(self):
        #控制 print(牌) 显示成什么，比如 ♠5
        suites = '♥♠♣♦'
        nums = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        return f'{suites[self.suite.value]}{nums[self.num]}'

    def __lt__(self, other_card):
        #定义"比大小"规则——有了它，牌才能被 sort() 排序
        #同花色就比点数；不同花色就比花色的编号
        if self.suite == other_card.suite:
            return self.num < other_card.num
        return self.suite.value < other_card.suite.value


card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
card3 = Card(Suite.CLUB, 8)
print(card1)  # ♠5 
print(card2)  # ♥K
print(card3)  # ♣8

import random


class Poker:
    #一副牌：52 张牌 + 记录发到哪一张了

    def __init__(self):
        #双重列表生成式：4 个花色 × 13 个点数 = 52 张
        self.cards = [Card(suite, num)
                       for suite in Suite
                       for num in range(1, 14)]

        self.current = 0          #下一张要发的位置

    def shuffle(self):
        #洗牌：发牌位置归零 + 打乱顺序
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        #发一张：取出当前位置的牌，然后位置往后挪一格
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def next(self):
        #还有牌没发完吗（@property 让它能当属性用：poker.next）
        return self.current < len(self.cards)


poker = Poker()
print(poker.cards)  # 洗牌前的牌
poker.shuffle()
print(poker.cards)  # 洗牌后的牌



class Player:
    #玩家：一个名字 + 一手牌

    def __init__(self,name):
        self.name = name
        self.card = []            #这个玩家的手牌（是个列表）

    def get_one(self,poker):
        #收下发的牌（参数其实是一张牌，传进来的就是 poker.deal() 的结果）
        self.card.append(poker)

    def arrange(self):
        #整理手牌：排序，靠的是 Card 里定义的 __lt__ 规则
        self.card.sort()



poker = Poker()
poker.shuffle()
Players = [Player('yyt'), Player('tkl'), Player('zjr'), Player('zlx')]

#发牌：13 轮，每轮给 4 个人各发一张（13 × 4 = 52，刚好发完）
for _ in range(13):
    for player in Players:
        player.get_one(poker.deal())

#每个人整理手牌并打印
for player in Players:
    player.arrange()
    print(f'名字:{player.name},手牌:{player.card}')

# 蓝酱整理注释，代码一行没动
