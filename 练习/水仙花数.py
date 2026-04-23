#找出100到999范围内的水仙花数

for PPDI in range(100,1000) :
    third = PPDI % 10
    second = PPDI // 10 % 10
    first =  PPDI // 100

    if first ** 3 + second ** 3 + third ** 3 == PPDI :
        print(PPDI)