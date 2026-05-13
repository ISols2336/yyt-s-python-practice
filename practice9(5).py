#列表的生成式
#[ 表达式  for 变量 in 可迭代对象 ]

#创建一个取值范围在1到99且能被3或者5整除的数字构成的列表
item = []
for i in range(1,100) :
    if i % 3 == 0 or i % 5 == 0 :
        item.append(i)

print(item)


items = [i for i in range(1,100) if i % 3 == 0 or i % 5 == 0] #相当于遍历，把符合条件的元素加入列表
print(items)   #第一个i，放入新列表的元素；for i in range(1,100)，做遍历；if i % 3 == 0 or i % 5 == 0，符合条件加入
#列表生成式 = 把 for 循环、if 判断、append 合并成一行
#写法固定：[取值 for 变量 in 列表 if 条件]（取值 = 变量）要用遍历到的元素（必须前后同一个变量）
print(item == items)   #True


#有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]   #表达式 num ** 2
print(nums2)


#嵌套列表

scores =[[11,22,33],[76,48,49],[24,42,98]]   #列表内可以加入列表元素作为列表元素
print(scores[0][2])  #33,可以用scores[N][N]访问列表内列表元素的元素


#通过产生随机数的方式来生成5个学生3门课程的成绩并保存在列表中
import random
score1 = [[random.randint(0,100) for _ in range(3)] for _ in range (5)]
print(score1)
#只需要循环次数，根本不用遍历的值