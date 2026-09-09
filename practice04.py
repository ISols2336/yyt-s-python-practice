f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%d华氏度 = %d摄氏度' % (f, c))          #%d占位符，用int类型替换掉%后的占位符


f = float(input('请输入华氏温度: '))              
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))      #%f占位符，用浮点类型替换掉%后的占位符

f = float(input('请输入华氏温度: '))  
c = (f - 32) / 1.8
print('%s华氏度 = %s摄氏度' % (f, c))          #%s占位符，用str类型替换掉%后的占位符



f = float(input('请输入华氏温度: '))       #符串前面的f表示这个字符串是需要格式化处理的，其中的{f:.1f}和{c:.1f}可以先看成是{f}和{c}
c = (f - 32) / 1.8 
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')    #输出时用变量f和变量c替换掉占位符


f = str(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%s华氏度 = %s摄氏度' % (f, c))   #TypeError: unsupported operand type(s) for -: 'str' and 'int'
                                       #不支持str字符串和int做减法




