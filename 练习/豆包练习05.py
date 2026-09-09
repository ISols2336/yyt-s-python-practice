#要求：
#定义一个列表 nums = [12, 5, 8, 19, 3, 25, 7]
#遍历这个列表，把大于 10的元素挑出来，放进新列表
#最后打印新列表


nums = [12,5,8,19,3,25,7]
nums10 = []
for times in range(len(nums)) :
    if nums[times] > 10 :
        nums10.append(nums[times])

print(nums10)


#把 小于 10 的元素挑出来，生成新列表，最后打印。
arr = [2, 7, 11, 4, 15, 8, 20]
itme = [i for i in arr if i < 10]
print(itme)