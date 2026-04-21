#输入两个大于 0 的正整数，求两个数的最大公约数。

nummer00 = int(input('请输入第一个数字'))
nummer01 = int(input('请输入第二个数字'))


if nummer00 > nummer01 :
    for i in range(nummer01,0,-1) :
        if nummer01 % i == 0 and nummer00 % i == 0:
            print(f'{nummer00}和{nummer01}的最大公约数为{i}')
            break

elif nummer01 > nummer00 :
    for i in range(nummer00,0,-1) :
        if nummer01 % i == 0 and nummer00 % i == 0:
            print(f'{nummer00}和{nummer01}的最大公约数为{i}')
            break
else :
    print(f'{nummer00}和{nummer01}的最大公约数为{nummer00}')