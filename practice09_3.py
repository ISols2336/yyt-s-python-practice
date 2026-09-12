#知识点：遍历列表的两种写法；len() 取长度
languages = ['Python','C++','Java','Kotlin']
for element in range(len(languages)):
    print(element + 1,languages[element])   #len 取元素个数，range(N) 得到 0 到 N-1 的下标


#更直接的写法：直接遍历元素，不用下标
for language in languages :
    print(language)



#掷骰子的列表应用：用列表当下标计数器
import random

times = [0] * 6              #[0,0,0,0,0,0]，[x]*n 快速建重复列表
move = int(input('请输入投骰子次数'))
for _ in range(move) :       #_ 表示这个循环变量用不到
    face = random.randint(1,6)
    times[face-1] += 1       #点数 1 存到下标 0，点数 6 存到下标 5

for index in range(len(times)) :
    print(f'骰子点{index + 1}出现了{times[index]}次')

# 蓝酱整理注释，代码一行没动
