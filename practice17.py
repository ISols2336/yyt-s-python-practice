#面对对象编程入门

class Coder:

    def __init__(self,name,hoay):
        self.name = name
        self.hoay = hoay


    def study(self,lg):
        print(f'{self.name}正在学{lg}')

    def play(self):
        print(f'{self.name}正在玩CS')

    def age(self):
        print(f'{self.name}已经{self.hoay}岁了')

cod_1 = Coder('yyt',19)
cod_2 = Coder('zjr',19)

coders = [cod_1,cod_2]
print([x for x in coders])
print(hex(id(cod_1)))

#类.方法  调用方法

Coder.study(cod_1,'python')

#对象.方法   调用方法

cod_2.play()
cod_2.study('C++')

#类.方法调用一定带上对象
Coder.play(cod_2)

#对象.方法不需要带上对象
cod_1.age()

