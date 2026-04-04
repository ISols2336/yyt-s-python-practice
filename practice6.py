BMI=(kg:=float(input('请输入体重'))/(meter:=float(input('请输入身高'))**2))
print(f'BMI={BMI:.2f}')
if   BMI<18.5:
    print('你的身材偏瘦')

elif BMI<24:
    print('你的身材很棒')      #关系运算会产生布尔值，如果if后面的布尔值为True，那么if语句下方，有四个空格缩进的print('你的身材很棒！')就会被执行

elif BMI<27:
    print('您有些肥胖')        #如果上方的if不成立就会elif

elif BMI<30:
    print('您轻度肥胖')

elif BMI<35:
    print('您重度肥胖')

else:                         #if后条件不成立，就运行else
    print('666良子来了')
