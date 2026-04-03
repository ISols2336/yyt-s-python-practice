radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)    #%f后f占位符，%后表示占位符替换为perimrter的值，.2表示保留小数点后两位，f表示这是一个浮点数
print('面积: %.2f' % area)



import math         #import math表示导入math模块，导入该模块以后，才能用math.pi得到圆周率的值

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}')       #字符串前的f表示后面要格式化字符串内的f字符，替换为变量值，：.2表示保留变量值小数点后两位，这是一个浮点数
print(f'面积: {area:.2f}')            #f+{变量}是一个语法



import math

radius = float(input('请输入圆的半径: '))  # 输入: 5.5
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
print(f'{area = :.2f}')       # 输出：area = 95.03          #f+{变量名=值}将输出 变量名=值，方便，等价于print(f'perimeter={perimeter:.2f}')


year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0     #能被4整除，不能被100整除，或者能被400整除
print(f'{is_leap = }')