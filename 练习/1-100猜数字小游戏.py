#猜数字游戏：程序随机生成 1 到 100 的数字，玩家输入猜测，
#提示"大了"或"小了"或"猜对了"；猜中时提示一共猜了多少次，游戏结束。


import random     #用 random.randrange 生成 1 到 100 的随机数

nummer = random.randrange(1,101)
times = 0

while True :

    nummer01 = int(input('请输入1到100的数字'))     #输入放在循环内，每次都会重新赋值
    times += 1                                     #放在循环外的话次数不会累加

    if nummer01 > 100 :
        print('请输入1到100的数字!')

    elif nummer01 < 1 :
        print('请输入1到100的数字!')     
        
    else :
        if nummer01 > nummer :
            print('大了')
        
        elif nummer01 < nummer :
            print('小了')
    
        else :
            print(f'正确！数字是{nummer}')
            print(f'你猜了{times}次')
            break

# deepseek 酱整理注释，代码一行没动
