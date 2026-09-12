#知识点：列表生成式，把 for、if、append 合并成一行
#[ 表达式  for 变量 in 可迭代对象  (if 条件) ]

#创建一个取值范围在1到99且能被3或者5整除的数字构成的列表
item = []
for i in range(1,100) :
    if i % 3 == 0 or i % 5 == 0 :
        item.append(i)

print(item)


#上面四行浓缩成一行：取值 i、遍历 range(1,100)、条件筛选
items = [i for i in range(1,100) if i % 3 == 0 or i % 5 == 0]
print(items)
print(item == items)   #True，两种写法结果一样


#有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]   #表达式是 num ** 2
print(nums2)


#嵌套列表

scores =[[11,22,33],[76,48,49],[24,42,98]]   #列表里放列表，就是二维
print(scores[0][2])  #33，两层下标：第 0 行第 2 列


#通过产生随机数的方式来生成5个学生3门课程的成绩并保存在列表中
import random
score1 = [[random.randint(0,100) for _ in range(3)] for _ in range (5)]
print(score1)
#两层生成式：外层 5 个学生，内层每人 3 门课

# 蓝酱整理注释，代码一行没动
