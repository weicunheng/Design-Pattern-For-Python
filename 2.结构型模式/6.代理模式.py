"""Proxy Pattern"""
"""
模式动机
    在代理模式（Proxy Pattern）中，一个类代表另一个类的功能。这种类型的设计模式属于结构型模式。
    在代理模式中，我们创建具有现有对象的对象，以便向外界提供功能接口。
    在某些情况下，一个客户不想或者不能直接引用一个对 象，此时可以通过一个称之为“代理”的第三者来实现 间接引用
    代理对象可以在客户端和目标对象之间起到 中介的作用
    并且可以通过代理对象去掉客户不能看到 的内容和服务或者添加客户需要的额外服务。 
    
    通过引入一个新的对象（如小图片和远程代理 对象）来实现对真实对象的操作或者将新的对 象作为真实对象的一个替身，
    这种实现机制即 为代理模式，通过引入代理对象来间接访问一 个对象，这就是代理模式的模式动机。
       
"""

"""
模式定义
    代理模式(Proxy Pattern) ：给某一个对象提供一个代 理，并由代理对象控制对原对象的引用。
    代理模式的英 文叫做Proxy或Surrogate，它是一种对象结构型模式。
"""

"""
模式结构
    Subject: 抽象主题角色
    Proxy: 代理主题角色
    RealSubject: 真实主题角色
"""

"""
意图：
    为其他对象提供一种代理以控制对这个对象的访问。
主要解决：
    在直接访问对象时带来的问题，比如说：要访问的对象在远程的机器上。
    在面向对象系统中，有些对象由于某些原因（比如对象创建开销很大，或者某些操作需要安全控制，或者需要进程外的访问）
    直接访问会给使用者或者系统结构带来很多麻烦，我们可以在访问此对象时加上一个对此对象的访问层。
何时使用：
    想在访问一个类时做一些控制。
如何解决：
    增加中间层。
关键代码：
    实现与被代理类组合。
应用实例：
    1、Windows 里面的快捷方式
    2、买火车票不一定在火车站买，也可以去代售点
    3、一张支票或银行存单是账户中资金的代理
    4、spring aop
优点： 
    1、职责清晰。 
    2、高扩展性。 
    3、智能化。
缺点： 1、由于在客户端和真实主题之间增加了代理对象，因此有些类型的代理模式可能会造成请求的处理速度变慢。 
        2、实现代理模式需要额外的工作，有些代理模式的实现非常复杂。
使用场景：按职责来划分，通常有以下使用场景： 
    1、远程代理。 
    2、虚拟代理。 
    3、Copy-on-Write 代理。 
    4、保护（Protect or Access）代理。 
    5、Cache代理。 
    6、防火墙（Firewall）代理。 
    7、同步化（Synchronization）代理。 
    8、智能引用（Smart Reference）代理。
"""

"""
和适配器、 装饰器的区别:
    1、和适配器模式的区别：适配器模式主要改变所考虑对象的接口，而代理模式不能改变所代理类的接口。 
    2、和装饰器模式的区别：装饰器模式为了增强功能，而代理模式是为了加以控制。
"""

"""
实现:
    建一个 Image 接口和实现了 Image 接口的实体类
    ProxyImage 是一个代理类，减少 RealImage 对象加载的内存占用
    ProxyPatternDemo，我们的演示类使用 ProxyImage 来获取要加载的 Image 对象，并按照需求进行显示
"""
import abc

class Image(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):pass

class RealImage(Image):

    def __init__(self, fileName):
        self.fileName = fileName
        self.loadFromDisk(fileName)

    def display(self):
        print("display...{}".format(self.fileName))

    def loadFromDisk(self, fileName):
        print("loading{}".format(fileName))

class ProxyImage(Image):

    realImage = None

    def __init__(self, fileName):
        self.fileName = fileName

    def display(self):
        if not self.realImage:
            self.realImage = RealImage(self.fileName)

        self.realImage.display()


if __name__ == '__main__':
    proxy_image = ProxyImage("test_10mb.jpg")

    # 图像将从磁盘加载
    proxy_image.display()

    # 图像不需要从磁盘加载
    proxy_image.display()


    """
    loadingtest_10mb.jpg
    display...test_10mb.jpg
    display...test_10mb.jpg
    """