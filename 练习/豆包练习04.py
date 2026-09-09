#只用 while，不能 for、不能 range、不导入任何模块
#从 100 循环到 999
#拆分：百位、十位、个位
#计算：每位相加同时满足两个条件才打印：
#① 这个数 不是水仙花数
#② 各位立方和 > 500


nummer = 100
while nummer < 1000 :
    
    third = nummer % 10
    second = nummer // 10 % 10
    first =  nummer // 100

    if first ** 3 + second ** 3 + third ** 3 != nummer and \
    first ** 3 + second ** 3 + third ** 3 > 500:
       
        print(nummer)
    
    nummer += 1