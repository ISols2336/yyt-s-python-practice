#找出100到999范围内的水仙花数
#水仙花数：各位数字的立方和等于它本身

for PPDI in range(100,1000) :
    third = PPDI % 10            #个位
    second = PPDI // 10 % 10     #十位
    first =  PPDI // 100         #百位

    if first ** 3 + second ** 3 + third ** 3 == PPDI :
        print(PPDI)

# deepseek 酱整理注释，代码一行没动
