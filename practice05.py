#知识点：math 模块、圆周率 math.pi、** 幂运算、{变量=} 调试写法
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)    #%.2f：保留两位小数
print('面积: %.2f' % area)



import math         #导入 math 模块，才能用 math.pi 这个常量

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2     #** 是幂运算：radius 的 2 次方
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')



import math

radius = float(input('请输入圆的半径: '))  # 输入: 5.5
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56；{变量=} 会打印"变量名=值"，调试神器
print(f'{area = :.2f}')       # 输出：area = 95.03


year = int(input('请输入年份: '))
#闰年规则：能被 4 整除且不能被 100 整除，或能被 400 整除（注意 and 优先级高于 or）
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')

# 蓝酱整理注释，代码一行没动
