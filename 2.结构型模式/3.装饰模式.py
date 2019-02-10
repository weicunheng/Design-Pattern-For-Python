"""装饰模式(Decorator Pattern)"""
"""
模式动机:
    一般有两种方式给一个类或对象增加行为：
        1. 继承机制
            通过继承一个现有类可以使得子类在拥有自身方法的同时还拥有父类的方法。
            但是这种方法是静态的，用户不能控制增加行为的方式和时机。
        2. 关联机制
            将一个类的对象嵌入另一个对象中
            由另一个对象来决定是否调用嵌入对象的行为以便扩展自己的行为，我们称这个嵌入的对象为装饰器(Decorator)
    装饰模式以对客户透明的方式动态地给一个对象附加上更多的责任
    客户端并不会觉得对象在装饰前和装饰后有什么不同。
    装饰模式可以在不需要创造更多子类的情况下，将对象的功能加以扩展。这就是装饰模式的模式动机。
"""

"""
模式定义:
    装饰模式(Decorator Pattern) ：动态地给一个对象增加一些额外的职责(Responsibility)
    就增加对象功能来说，装饰模式比生成子类实现更为灵活。
    其别名也可以称为包装器(Wrapper)，与适配器模式的别名相同，但它们适用于不同的场合。
    它是一种对象结构型模式。
    允许向一个现有的对象添加新的功能，同时又不改变其结构
"""

"""
模式结构:
        Component: 抽象构件
        ConcreteComponent: 具体构件
        Decorator: 抽象装饰类
        ConcreteDecorator: 具体装饰类
"""
import abc

class Shap(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

# 创建装饰类
class ShapeDecorator(Shap):
    def __init__(self, decoratedShape):
        self.decoratedShape = decoratedShape

    def draw(self):
        self.decoratedShape.draw()


class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decoratedShape):
        super().__init__(decoratedShape)

    def draw(self):
        self.decoratedShape.draw()
        self.setRedBorder(self.decoratedShape)

    def setRedBorder(self, decoratedShape):
        print("边框颜色:红色")

class Rectangle(Shap):
    def draw(self):
        print("长方形")

class Circle(Shap):

    def draw(self):
        print("圆")

if __name__ == '__main__':
    circle = Circle()
    redCircle = RedShapeDecorator(Circle())
    redRectangle = RedShapeDecorator(Rectangle())

    circle.draw() # 没有装饰，只能输出自己是圆
    print("\r\n")
    redCircle.draw() # 输出自己是圆，还能输出自己的边框颜色
    print("\r\n")
    redRectangle.draw() # 输出自己是长放心，还能输出自己的边框颜色
    print("\r\n")

"""
优点:
    装饰类和被装饰类可以独立发展，不会相互耦合，
    装饰模式是继承的一个替代模式，装饰模式可以动态扩展一个实现类的功能。
"""
"""
缺点:
    多层装饰比较复杂。
"""

"""
适用场景:
     1、扩展一个类的功能。 
     2、动态增加功能，动态撤销。

"""