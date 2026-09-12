#知识点：random 随机数；列表用 [] 定义，元素可重复、可不同类型
#将一颗色子掷6000次，统计每种点数出现的次数
import random

if01 = 0
if02 = 0
if03 = 0
if04 = 0
if05 = 0
if06 = 0

for _ in range(6000) :       #_ 表示这个循环变量用不到
    
    i = random.randint(1,6)  #randint(1,6) 生成 1 到 6 的随机整数（闭区间）
    
    if i == 1 :
        if01 += 1
    
    elif i == 2 :
        if02 += 1
    
    elif i == 3 :
        if03 += 1
    
    elif i == 4 :
        if04 += 1
    
    elif i == 5 :
        if05 += 1

    elif i == 6 :    
        if06 += 1


print(f'1出现了{if01}次')
print(f'2出现了{if02}次')
print(f'3出现了{if03}次')
print(f'4出现了{if04}次')
print(f'5出现了{if05}次')
print(f'6出现了{if06}次')


#列表：用 [] 字面量定义
items1 = [35, 12, 99, 68, 55, 35, 87]        #元素可以重复
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]         #元素可以是不同类型
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]

print(type(items1))   # <class 'list'>

print(list(range(1,11)))   #list() 把序列转成列表
print(list('hello'))       #字符串也可拆成 ['h','e','l','l','o']


print(items1 + items2)     #+ 拼接两个列表（返回新列表）

items3 += items2           #+= 原地扩展，等价 items3 = items3 + items2
print(items3)     #[100, 12.3, 'Python', True, 'Python', 'Java', 'Go', 'Kotlin']

# 蓝酱整理注释，代码一行没动
