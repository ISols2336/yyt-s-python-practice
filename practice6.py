BMI=(kg:=float(input('请输入体重'))/(meter:=float(input('请输入身高'))**2))
print(f'BMI={BMI:.2f}')
if 18.5>BMI:
    print('你的身材偏瘦')



elif 18.5<=BMI<24:
    print('你的身材很棒')      #关系运算会产生布尔值，如果if后面的布尔值为True，那么if语句下方，有四个空格缩进的print('你的身材很棒！')就会被执行





else:                         #if后条件不成立，就运行else
    print('你的身材不够标准')
