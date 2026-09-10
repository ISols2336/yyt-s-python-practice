#原神牛逼

status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'      #case _：兜底，匹配任何值但不绑定变量

print('状态码描述:', description)



status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'        #用 | 连接多个值，任意一个匹配即可
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)



status_code = int(input('请输入状态响应码：'))
match status_code:
    case 400:
        print("请求错误")
    case 404:
        print("页面不存在")
    case 500:
        print("服务器挂了")
    case x:                         #case 加变量名：匹配任何值并绑定到 x，后面的 case 就轮不到了
        print(f"未知状态码：{x}")    #所以这里才能用 x


x = float(input('x = '))            #分段函数：x > 1 走第一段，其余按 x >= -1 再分
if x > 1:
    y = 3 * x - 5
else:                               #这里的嵌套 if 可以用 elif 简化
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(f'{y = }')




#练习,输入成绩，90分及以上A，80-90B，70-80C，60-70D，60以下E
score=int(input('请输入成绩：'))
if score>=90:
    print('A')

elif score>=80:
    print('B')

elif score>=70:
    print('C')

elif score>=60:
    print('D')

else:
    print('E')



#练习，输入三条边的长度，能构成三角形就计算周长和面积，否则提示“不能构成三角形”

import math

a = float(input('请输入a边长:'))
b = float(input('请输入b边长:'))
c = float(input('请输入c边长:'))
if a+b>c and a+c>b and c+b>a :
    Perimeter = a + b + c
    p = Perimeter/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))          #海伦公式：p 是半周长
    print(f'{Perimeter=:.1f}')            #{变量=:.1f}：打印变量名和值，保留一位小数
    print(f'{area=:.1f}')                      

else :
    print('不能构成三角形')

# deepseek 酱整理注释，代码一行没动
