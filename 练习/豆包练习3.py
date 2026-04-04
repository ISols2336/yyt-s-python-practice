#从键盘输入三个数 a b c 代表三条边长。要求：
#先判断能不能构成三角形
#如果能，再判断是不是直角三角形
#输出结果：
#不能构成三角形
#是普通三角形
#是直角三角形


a = float(input('请输入a边长:'))
b = float(input('请输入b边长:'))
c = float(input('请输入c边长:'))

if a + b > c and a + c > b and c + b > a :

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
        print('三角形类型：直角三角形')
    
    else :
        print('三角形类型：普通三角形')

else :
    print('无法构成三角形')