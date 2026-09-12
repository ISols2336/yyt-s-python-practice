#知识点：二维列表（列表套列表）的构建和访问
#一共有 4 个学生
#每个学生有 语文、数学、英语 3 门成绩
#把所有学生成绩存入二维列表 stu_scores
#最后：遍历整个二维列表，打印出每个学生的所有成绩



stu_scores = []
for _ in range(4) :       #外层：4 个学生
    
    item =[]              #每个学生的成绩列表
    
    for _ in range(3) :   #内层：每人 3 门
        score = int(input('请输入成绩'))
        item.append(score)
    
    stu_scores.append(item)   #把每个学生的列表装进大列表，形成二维

print(stu_scores)
print('打印第几个学生成绩？')
stu = int(input('请输入'))
print(stu_scores[stu - 1])    #stu-1：因为下标从 0 开始，第 1 个是下标 0

# 蓝酱整理注释，代码一行没动
