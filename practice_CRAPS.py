#CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
#该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
#简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
#玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
#玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；
#如果玩家摇出了第一次摇的点数，玩家胜；
#其他点数玩家继续摇骰子，直到分出胜负。
#为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注
#每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励
#如果庄家获胜，玩家就会输掉自己下注的金额。
#游戏结束的条件是玩家破产（输光所有的赌注）。

import random
cash = 1000
first = None

while cash > 0 :
    print(f'你还有{cash}元')

    while True:
        
        bet =int(input('请下注\n'))
        
        if bet <= cash:
            first = random.randint(1,6) + random.randint(1,6)
            print(f'结果是{first}')

            if first == 11 or first == 7 :
                print('玩家获胜')
                cash += bet
                break
            
            elif first == 2 or first == 3 or first == 12 :
                print('庄家获胜')
                cash -= bet
                break

            else :
                print(f'你的目标点是{first}')
                break

        else :
            print('❌下注金额不能超过现有余额')


    if first in [2, 3, 7, 11, 12]:
        continue
    
    else :

        while cash > 0 :
            
            second = random.randint(1,6) + random.randint(1,6)
            print(f'结果是{second}')
            if second == 7 :
                    print('庄家获胜')
                    cash -= bet
                    break
            
            elif second == first :
                print('玩家获胜')
                cash += bet
                break
if cash == 0 :
    print('你没钱了，游戏结束')