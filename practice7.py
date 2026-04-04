status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'               #和if,elif,else的作用一样，匹配成功后执行冒号后面的代码，如果没有匹配成功，就执行case _后的代码
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'

print('状态码描述:', description)



status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'        #也可以用|连接多个值，表示这些值都匹配，如果匹配成功，就执行冒号后面的代码
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'            #case_匹配任何值，如果前面的case都没有匹配成功，就执行这个case，并且case_并不会将match后变量的值赋值给_，如果这个值你不想使用，可以用_来表示
print('状态码描述:', description)



status_code = int(input('请输入状态响应码：'))
match status_code:
    case 400:
        print("请求错误")
    case 404:
        print("页面不存在")
    case 500:
        print("服务器挂了")
    case x:                         #case后面跟一个变量名，表示匹配任何值，并将该值赋给变量，如果前面的case都没有匹配成功，就执行这个case
        print(f"未知状态码：{x}")    #case x表示将match后变量的值赋值给x
                                    #如果想使用case后的值，可以在case后面跟一个变量名，这样就可以在case块中使用这个变量了，如果前面的case都没有匹配成功，就执行这个case，并且将match后变量的值赋给这个变量，这样就可以在case块中使用这个变量了
                                    #原神牛逼


x = float(input('x = '))            #嵌套结构，如果if语句的代码块中还有if语句，那么就形成了嵌套结构，嵌套结构可以有多层，但是不建议超过三层，否则代码的可读性就会变差，嵌套结构的代码块需要注意缩进，缩进错误会导致代码运行错误
if x > 1:
    y = 3 * x - 5                   #用elif可以简化代码
else:
    if x >= -1:
        y = x + 2           
    else:
        y = 5 * x + 3
print(f'{y = }')




#练习,如果输入的成绩在90分以上（含90分），则输出A；输入的成绩在80分到90分之间（不含90分），则输出B；输入的成绩在70分到80分之间（不含80分），则输出C；输入的成绩在60分到70分之间（不含70分），则输出D；输入的成绩在60分以下，则输出E
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



#练习，输入三条边的长度，如果能构成三角形就计算周长和面积；否则给出“不能构成三角形”的提示。

import math

a = float(input('请输入a边长:'))
b = float(input('请输入b边长:'))
c = float(input('请输入c边长:'))
if a+b>c and a+c>b and c+b>a :
    Perimeter = a + b + c
    p = Perimeter/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c)) 
    print(f'Perimeter={Perimeter:.1f}')
    print(f'area={area:.1f}')

else :
    print('不能构成三角形')