#知识点：用 // 和 % 拆出个位/十位/百位；水仙花数 = 各位立方和
#找出100到999范围内的水仙花数
#水仙花数：各位数字的立方和等于它本身

for PPDI in range(100,1000) :
    third = PPDI % 10            #个位：除以 10 取余
    second = PPDI // 10 % 10     #十位：先整除 10，再取余
    first =  PPDI // 100         #百位：整除 100

    if first ** 3 + second ** 3 + third ** 3 == PPDI :
        print(PPDI)

# 蓝酱整理注释，代码一行没动
