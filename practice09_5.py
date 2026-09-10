#列表的生成式
#[ 表达式  for 变量 in 可迭代对象 ]

#创建一个取值范围在1到99且能被3或者5整除的数字构成的列表
item = []
for i in range(1,100) :
    if i % 3 == 0 or i % 5 == 0 :
        item.append(i)

print(item)


items = [i for i in range(1,100) if i % 3 == 0 or i % 5 == 0] #取值 i、遍历 range(1,100)、条件筛选
print(items)
print(item == items)   #True


#有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]   #表达式是 num ** 2
print(nums2)


#嵌套列表

scores =[[11,22,33],[76,48,49],[24,42,98]]   #列表里放列表
print(scores[0][2])  #33，两层下标


#通过产生随机数的方式来生成5个学生3门课程的成绩并保存在列表中
import random
score1 = [[random.randint(0,100) for _ in range(3)] for _ in range (5)]
print(score1)
#两层生成式：外层 5 个学生，内层每人 3 门课

# deepseek 酱整理注释，代码一行没动
