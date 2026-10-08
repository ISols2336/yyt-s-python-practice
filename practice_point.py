#知识点：类 class、魔法方法 __str__、组合（一个对象包含另一个对象）、类型注解
#Point（点）和 Circle（圆）

class Point:

    #构造函数：记录点的坐标 (x, y)
    def __init__(self,x:int,y:int):
        self.x,self.y = x,y      #一行给两个属性赋值

    #计算到另一个点的距离：两点距离公式 √((x2-x1)² + (y2-y1)²)
    def distance_to(self,other_point:Point):
        return ((other_point.x - self.x)**2 + (other_point.y - self.y)**2)**0.5
        #**0.5 就是开平方；other_point 是另一个 Point 对象

    #__str__ 是魔法方法：控制 print(对象) 时显示什么
    def __str__(self):
        return f'({self.x},{self.y})'


class Circle:

    #构造函数：圆心是一个 Point 对象（组合），半径是 r
    def __init__(self,center_point:Point,r:int):
        self.center = center_point   #center 里装的是 Point 对象，这就是"组合"
        self.r = r

    #判断一个点是否在圆内：到圆心的距离 <= 半径
    def is_point_in_circle(self,op_point:Point):
        if self.center.distance_to(op_point) <= self.r:
            return True

        else:
            return False
        #上面 if/else 可简化成一行：return self.center.distance_to(op_point) <= self.r

    #__str__ 里又调用了 self.center 的 __str__（嵌套调用，很妙）
    def __str__(self):
        return f'Circle(圆心{self.center},半径{self.r})'


# ---- 测试 Point ----
point1 = Point(1,4)
point2 = Point(5,1)

print(point1.distance_to(point2))   #5.0：距离 √((5-1)²+(1-4)²)=√25

p1 = Point(1,3)
p2 = Point(3,5)
print(f"点{p1} 到 点{p2} 的距离：{p1.distance_to(p2):.4f}") #≈2.8284
print(p1)   #(1,3)：__str__ 生效
print(p2)   #(3,5)


# ---- 测试 Circle（蓝酱补的）----
c = Circle(Point(0, 0), 5)
print(c)                                   #Circle(圆心(0,0),半径5)
print(c.is_point_in_circle(Point(3, 4)))   #True：距离 5，正好在圆上
print(c.is_point_in_circle(Point(6, 0)))   #False：距离 6，在圆外

# 蓝酱整理注释，并补了 Circle 的测试代码
