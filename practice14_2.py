#知识点：import 的两种用法——from 模块 import 函数 / import 模块
from yytmodules import factorial_1   #从模块导入某个函数，直接用函数名

print(factorial_1(3))

import yytmodules                    #导入整个模块，用 模块名.函数名 调用

yytmodules.f_1()

# 蓝酱整理注释，代码一行没动
