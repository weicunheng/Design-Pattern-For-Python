"""桥接模式(Bridge Pattern)"""
"""
模式动机:
    设想如果要绘制矩形、圆形、椭圆、正方形，我们至少需要4个形状类，但是如果绘制的图形需要具有不同的颜色，如红色、绿色、蓝色等，此时至少有如下两种设计方案：
        第一种设计方案是为每一种形状都提供一套各种颜色的版本。
        第二种设计方案是根据实际需要对形状和颜色进行组合
    对于有两个变化维度（即两个变化的原因）的系统，采用方案二来进行设计系统中类的个数更少，且系统扩展更为方便。
    设计方案二即是桥接模式的应用。
    桥接模式将继承关系转换为关联关系，从而降低了类与类之间的耦合，减少了代码编写量。
"""

"""
模式定义:
    桥接模式(Bridge Pattern)：将抽象部分与它的实现部分分离，使它们都可以独立地变化。
    它是一种对象结构型模式，又称为柄体(Handle and Body)模式或接口(Interface)模式。
"""

"""
模式结构:
    Abstraction：抽象类
    RefinedAbstraction：扩充抽象类
    Implementor：实现类接口
    ConcreteImplementor：具体实现类
"""
# Shape 类来画出不同颜色的圆

import abc

"""
1. 创建桥接抽象接口
2. 创建实现DrawAPI 接口的实体桥接实现类
3. 使用 DrawAPI 接口创建抽象类 Shape。
4. 创建实现了 Shape 接口的实体类。
5. 使用 Shape 和 DrawAPI 类画出不同颜色的圆。
6. 执行程序，输出结果
"""

class DrawAPI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw_circle(self, radius, x, y):
        pass

class RedCircle(DrawAPI):
    def draw_circle(self, radius, x, y):
        print("半径为:{}的红圆".format(radius))

class GreenCircle(DrawAPI):
    def draw_circle(self, radius, x, y):
        print("半径为:{}的绿圆".format(radius))

class Shape(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape):

    def __init__(self, x, y, radius, draw_api):

        self.x = x
        self.y = y
        self.radius = radius
        self.draw_api = draw_api
        super().__init__()
        

    def draw(self):
        self.draw_api.draw_circle(self.radius, self.x, self.y)

if __name__ == '__main__':
    redCircle = Circle(1,1,5,RedCircle())
    greenCircle = Circle(2,2,6,GreenCircle())

    redCircle.draw()
    greenCircle.draw()