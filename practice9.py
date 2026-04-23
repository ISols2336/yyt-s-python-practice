#将一颗色子掷6000次，统计每种点数出现的次数

import random

if01 = 0
if02 = 0
if03 = 0
if04 = 0
if05 = 0
if06 = 0

for _ in range(6000) :
    
    i = random.randint(1,6)
    
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



items1 = [35, 12, 99, 68, 55, 35, 87]        #列表中可以有相同元素，35
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]         #也可以有不同类型元素
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]

print(type(items1))   # <class 'list'>，列表变量类型为list，是一种容器型的数据类型