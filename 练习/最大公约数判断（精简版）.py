#精简版
nummer00 = int(input('请输入第一个数：'))
nummer01 = int(input('请输入第二个数：'))

if nummer00 > nummer01 :
    min_num = nummer01

elif nummer01 > nummer00 :
    min_num = nummer00

else :
    min_num = nummer00

for i in range(min_num,0,-1) :
    if nummer01 % i == 0 and nummer00 % i == 0:
        print(f'{nummer00}和{nummer01}的最大公约数为{i}')
        break