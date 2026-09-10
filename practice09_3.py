#元素的遍历


languages = ['Python','C++','Java','Kotlin']
for element in range(len(languages)):
    print(element + 1,languages[element])   #len 取元素个数，range(N) 得到 0 到 N-1 的下标


#更直接的写法：直接遍历元素
for language in languages :
    print(language)



#掷骰子的列表应用
import random

times = [0] * 6              #[0,0,0,0,0,0]
move = int(input('请输入投骰子次数'))
for _ in range(move) :
    face = random.randint(1,6)
    times[face-1] += 1

for index in range(len(times)) :
    print(f'骰子点{index + 1}出现了{times[index]}次')

# deepseek 酱整理注释，代码一行没动
