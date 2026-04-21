#小一点”或“猜对了”，如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。


import random     #使用import random导入了 Python 标准库的random模块，该模块的randrange函数帮助我们生成了 1 到 100 范围的随机数

nummer = random.randrange(1,101)
times = 0

while True :

    nummer01 = int(input('请输入1到100的数字'))     #变量输入放在循环内，每次循环都会重新赋值，实现连续猜测
    times += 1                                     #放在循环外则变量值不变

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
