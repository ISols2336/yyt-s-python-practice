#一共有 4 个学生
#每个学生有 语文、数学、英语 3 门成绩
#把所有学生成绩存入二维列表 stu_scores
#最后：遍历整个二维列表，打印出每个学生的所有成绩



stu_scores = []
for _ in range(4) :
    
    item =[]
    
    for _ in range(3) :
        score = int(input('请输入成绩'))
        item.append(score)
    
    stu_scores.append(item)

print(stu_scores)
print('打印第几个学生成绩？')
stu = int(input('请输入'))
print(stu_scores[stu - 1])
