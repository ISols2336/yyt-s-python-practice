#知识点：% 格式化占位符 %d %f %s，以及 f-string；华氏转摄氏 C = (F-32)/1.8
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%d华氏度 = %d摄氏度' % (f, c))          #%d 整数占位，float 会被截断


f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))      #%.1f 浮点占位，保留 1 位小数

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%s华氏度 = %s摄氏度' % (f, c))          #%s 字符串占位，万物都能转字符串



f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')    #f-string：{变量:格式}，比 % 更直观、更快


#下面这行会崩，故意留的：str 不能和 int/float 做减法
#TypeError: unsupported operand type(s) for -: 'str' and 'int'
f = str(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%s华氏度 = %s摄氏度' % (f, c))

# 蓝酱整理注释，代码一行没动
