#知识点：import 复用自己写的模块、类的方法调用、抽函数、资金流水（押金模型）
#21 点游戏：玩家和庄家比谁更接近 21 点、且不能超过（超过叫"爆牌"）

from practaice_Poker import Suite, Card, Poker, Player
import time, random

cast = 10000                                                    #玩家的总资金
dealer = [Player('莉莉丝'), Player('柊筱娅'), Player('叶瞬光')]    #庄家候选（每局随机挑一个）


def total_card(cards:Player.card):
    #算一手牌的点数：J/Q/K 算 10；A 先按 1 算，只在"升级成 11 也不会爆"时才加 10
    total = [i.num for i in cards]

    for i in range(len(total)):
        if total[i] > 10:                                       #11/12/13 就是 J/Q/K
            total[i] = 10

    total_sum = sum(total)

    if any(num == 1 for num in total):                          #手里有 A（A 的 num 是 1）

        if total_sum <= 11:                                     #A 当 11 也不会超过 21 → 升级
            total_sum += 10

    return total_sum


while cast > 0:                                                 #资金花光就结束

    poker = Poker()                                             #每局重新造一副牌（保证 52 张够发）
    player = Player(input('请输入玩家名字'))
    pull_cast = int(input('请输入下注金额'))
    dealer_1 = random.choice(dealer)

    cast -= pull_cast                                           #★ 先把押金交出去 —— "押金模型"的关键一步
    time.sleep(2)
    print(f'本次庄家为{dealer_1}')

    while True:                                                 #这层只为配合底部的 break，实际只跑一次

        dealer_1.card = []                                      #清空上一局的手牌
        player.card = []
        
        print(f'现在的资金{cast}')

        Poker.shuffle(poker)

        dealer_1.get_one(Poker.deal(poker))                     #先各发一张
        player.get_one(Poker.deal(poker))    
    
        print(f'庄家的手牌为{dealer_1.card}')
        time.sleep(1)
        print(f'玩家的手牌为{player.card}')

        y_or_n = input('是否继续摸牌？')

        while y_or_n == 'y':                                    #玩家回合：想摸就继续摸
    
            dealer_1.get_one(Poker.deal(poker))
            player.get_one(Poker.deal(poker))
    
            print(f'庄家的手牌为{dealer_1.card}')
            time.sleep(1)
            print(f'玩家的手牌为{player.card}')

            y_or_n = input('是否继续摸牌？')

        if total_card(player.card) <= 21:                       #★ 玩家没爆，庄家才需要摸牌
            while total_card(dealer_1.card) < 17:               #庄家规则：不满 17 点就继续摸
                dealer_1.get_one(Poker.deal(poker))
                time.sleep(1)
                print(f'庄家的手牌为{dealer_1.card}')


        # ===== 结算：爆牌最先判（自己爆了就是输，跟对方几点无关）=====
        if total_card(player.card) > 21:
            print(f'庄家{dealer_1}获胜')                         #玩家爆牌→输。押金开局已扣，这里不再动钱

        elif total_card(dealer_1.card) > 21:
            print(f'玩家{player}获胜')                           #庄家爆牌→玩家赢
            cast += pull_cast*2                                 #拿回押金 + 赢的一倍

        elif total_card(dealer_1.card) > total_card(player.card) and total_card(dealer_1.card) <= 21:
            print(f'庄家{dealer_1}获胜')                         #庄家大且没爆→玩家输

        elif total_card(dealer_1.card) < total_card(player.card) and total_card(player.card) <= 21:
            print(f'玩家{player}获胜')                           #玩家大且没爆→玩家赢
            cast += pull_cast*2

        else:
            print('平局')                                       #点数一样→退回押金
            cast += pull_cast
                
        break                                                   #这一局结束，回外层重新下注

# 蓝酱整理注释，代码一行没动
