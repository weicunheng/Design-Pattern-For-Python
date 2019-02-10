"""Flyweight Pattern"""
"""
模式动机:
    面向对象技术可以很好地解决一些灵活性或可扩展性问题，但在很多情况下需要在系统中增加类和对象的个数。
    当对象数量太多时，将导致运行代价过高，带来性能下降等问题。
    享元模式正是为解决这一类问题而诞生的。享元模式通过共享技术实现相同或相似对象的重用。
    在享元模式中可以共享的相同内容称为内部状态(IntrinsicState)
    而那些需要外部环境来设置的不能共享的内容称为外部状态(Extrinsic State)
    由于区分了内部状态和外部状态，因此可以通过设置不同的外部状态使得相同的对象可以具有一些不同的特征,而相同的内部状态是可以共享的。
    在享元模式中通常会出现工厂模式
    需要创建一个享元工厂来负责维护一个享元池(Flyweight Pool)用于存储具有相同内部状态的享元对象。
    
"""

"""
模式定义:
    享元模式(Flyweight Pattern)：运用共享技术有效地支持大量细粒度对象的复用。
    系统只使用少量的对象，而这些对象都很相似，状态变化很小，可以实现对象的多次复用。
    由于享元模式要求能够共享的对象必须是细粒度对象，因此它又称为轻量级模式，它是一种对象结构型模式。
"""

"""
模式结构:
    Flyweight: 抽象享元类
    ConcreteFlyweight: 具体享元类
    UnsharedConcreteFlyweight: 非共享具体享元类
    FlyweightFactory: 享元工厂类
"""

"""
主要解决
    在有大量对象时，有可能会造成内存溢出，
    我们把其中共同的部分抽象出来，如果有相同的业务请求，直接返回在内存中已有的对象，避免重新创建。
何时使用
    1、系统中有大量对象。
    2、这些对象消耗大量内存。
    3、这些对象的状态大部分可以外部化。
    4、这些对象可以按照内蕴状态分为很多组，当把外蕴对象从对象中剔除出来时，每一组对象都可以用一个对象来代替。
    5、系统不依赖于这些对象身份，这些对象是不可分辨的。
如何解决
    用唯一标识码判断，如果在内存中有，则返回这个唯一标识码所标识的对象。
    用 HashMap 存储这些对象。
应用实例
    1、JAVA 中的 String，如果有则返回，如果没有则创建一个字符串保存在字符串缓存池里面。
    2、数据库的数据池。
    3、游戏角色
优点
    大大减少对象的创建，降低系统的内存，使效率提高。
缺点
    提高了系统的复杂度，需要分离出外部状态和内部状态
    而且外部状态具有固有化的性质，不应该随着内部状态的变化而变化，否则会造成系统的混乱。
使用场景
    1、系统有大量相似对象。
    2、需要缓冲池的场景。
注意事项
    1、注意划分外部状态和内部状态，否则可能会引起线程安全问题。
    2、这些类必须有一个工厂对象加以控制。
"""

"""

"""
import abc
import random

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape):

    def __init__(self,color):

        self.color = color

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_radius(self, radius):
        self.radius = radius

    def draw(self):
        print("{}颜色的圆: x:{}, y:{}, radius:{}".format(self.color, self.x, self.y, self.radius))



class ShapeFactory():
    """
    {
        "color":
    }
    """
    circle_color = dict()
    @classmethod
    def get_circle(cls, color):
        if color in cls.circle_color:
            return cls.circle_color[color]
        else:
            cls.circle_color[color] = Circle(color)
            return cls.circle_color[color]

if __name__ == '__main__':

    color = ["Red", "Green", "Blue", "White", "Black"]
    circle_id = dict()
    for i in range(20):
        circle = ShapeFactory.get_circle(color[random.randint(0,4)])
        circle.set_x(random.randint(0,10))
        circle.set_y(random.randint(0,10))
        circle.set_radius(100)
        circle.draw()
        id_str = id(circle)
        if id_str in circle_id:
            circle_id[id_str] += 1
        else:
            circle_id[id_str] = 1

    print(circle_id)  # {2678877878368: 5, 2678877880048: 3, 2678877879768: 5, 2678877880160: 2, 2678877880216: 5}




