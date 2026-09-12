#知识点：if/elif/else 多分支；海象运算符 :=；BMI = 体重 / 身高²
#:= 在表达式里先赋值再参与计算；** 是平方
BMI=(kg:=float(input('请输入体重'))/(meter:=float(input('请输入身高'))**2))
print(f'BMI={BMI:.2f}')
if   BMI<18.5:
    print('你的身材偏瘦')

elif BMI<24:
    print('你的身材很棒')

elif BMI<27:
    print('您有些肥胖')        #elif：上面条件不成立时才判断，等价于 else + if

elif BMI<30:
    print('您轻度肥胖')

elif BMI<35:
    print('您重度肥胖')

else:                         #以上都不成立时兜底
    print('666良子来了')

# 蓝酱整理注释，代码一行没动
