f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%d华氏度 = %d摄氏度' % (f, c))          #%d 占位，按整数输出（截断小数）


f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))      #%.1f 占位，保留 1 位小数

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%s华氏度 = %s摄氏度' % (f, c))          #%s 占位，按字符串输出



f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')    #f-string：{变量:格式}


#下面这行会崩，是故意留的：str 不能和 int 做减法
#TypeError: unsupported operand type(s) for -: 'str' and 'int'
f = str(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%s华氏度 = %s摄氏度' % (f, c))

# deepseek 酱整理注释，代码一行没动
