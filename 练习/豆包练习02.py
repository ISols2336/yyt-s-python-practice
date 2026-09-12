#知识点：三角形判定、连等比较 a==b==c、elif 分支
#输入三条边长 a、b、c（已经能构成三角形的前提下），判断它是哪种三角形：
#三边都相等 → 输出：等边三角形
#有且只有两边相等 → 输出：等腰三角形
#三边都不相等 → 输出：普通三角形

a = float(input('请输入a边长:'))
b = float(input('请输入b边长:'))
c = float(input('请输入c边长:'))
if a+b>c and a+c>b and c+b>a :      #任意两边之和大于第三边，才能构成三角形
    if  a == b == c:                #连等：等价 a == b and b == c
        print('等边三角形')
    
    elif a == b != c or a == c != b or b == c != a:   #有且只有两边相等
        print('等腰三角形')
    
    elif a != b and a != c and b != c:
        print('普通三角形')

else :
    print('不能构成三角形')

# 蓝酱整理注释，代码一行没动
