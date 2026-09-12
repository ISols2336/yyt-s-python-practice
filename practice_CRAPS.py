#知识点：random 掷骰子、while 循环嵌套、break/continue 控制游戏流程
#CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种桌上赌博游戏，用两粒骰子。
#简化规则：
#  第一次摇出 7 或 11 点，玩家胜；
#  第一次摇出 2、3 或 12 点，庄家胜；
#  其他点数记为目标点，继续摇：摇出 7 点庄家胜，摇回目标点玩家胜，否则一直摇到分出胜负。
#玩家初始 1000 元，每局先下注，赢了赢得下注额，输了输掉下注额，破产为止。

import random
cash = 1000
first = None

while cash > 0 :        #外层循环：只要还有钱就一直玩
    print(f'你还有{cash}元')

    while True:         #内层循环：直到下注金额合法才跳出
        
        bet =int(input('请下注\n'))
        
        if bet <= cash:
            first = random.randint(1,6) + random.randint(1,6)   #两粒骰子相加
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
        continue        #这几个点数已经分出胜负，回到开头开下一局
    
    else :

        while cash > 0 :        #目标点阶段：继续摇
            
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

# 蓝酱整理注释，代码一行没动
