#元素的遍历


languages = ['Python','C++','Java','Kotlin']
for element in range(len(languages)):
    print(element + 1,languages[element])   #len函数可以获取列表内元素的个数，range(len(languages))则构成了range(N),0--N-1的范围，作为列表元素的索引


#还可以对列表做循环
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