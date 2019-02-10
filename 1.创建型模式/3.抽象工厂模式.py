"""Abstract Factory"""
"""
模式动机
    在工厂方法模式中具体工厂负责生产具体的产品
    每一个具体工厂对应一种具体产品
    一般情况下，一个具体工厂中只有一个工厂方法或者一组重载的工厂方法
    但是有时候我们需要一个工厂可以提供多个产品对象，而不是单一的产品对象。
    为了更清晰地理解抽象工厂模式，需要先引入两个概念：
        产品等级结构 ：
            产品等级结构即产品的继承结构，
            如一个抽象类是电视机，其子类有海尔电视机、海信电视机、TCL电视机，
            则抽象电视机与具体品牌的电视机之间构成了一个产品等级结构，
            抽象电视机是父类，而具体品牌的电视机是其子类。
        产品族 ：
            在抽象工厂模式中，产品族是指由同一个工厂生产的，位于不同产品等级结构中的一组产品，
            如海尔电器工厂生产的海尔电视机、海尔电冰箱
            海尔电视机位于电视机产品等级结构中，海尔电冰箱位于电冰箱产品等级结构中。
    当系统所提供的工厂所需生产的具体产品并不是一个简单的对象，而是多个位于不同产品等级结构中属于不同类型的具体产品时需要使用抽象工厂模式。
    抽象工厂模式是所有形式的工厂模式中最为抽象和最具一般性的一种形态。
    抽象工厂模式与工厂方法模式最大的区别在于，工厂方法模式针对的是一个产品等级结构，而抽象工厂模式则需要面对多个产品等级结构
    一个工厂等级结构可以负责多个不同产品等级结构中的产品对象的创建 。
    当一个工厂等级结构可以创建出分属于不同产品等级结构的一个产品族中的所有对象时，抽象工厂模式比工厂方法模式更为简单、有效率。
"""

"""
模式定义:
    抽象工厂模式: 提供一个创建一系列相关或相互依赖对象的接口,而无须指定它们具体的类
    抽象工厂模式又称为Kit模式，属于对象创建型模式。
"""

"""
模式结构:
    AbstractFactory：抽象工厂
    ConcreteFactory：具体工厂
    AbstractProduct：抽象产品
    Product：具体产品
    
电脑:CPU(inter amd) 内存(Kingston dell) 硬盘  显卡...
"""
import abc
class CPUAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface(self):
        pass


class FlashAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface(self):
        pass



class InterCPUFactory(CPUAbstractFactory):
    def interface(self):
        return "InterCPU接口"

class AMDCPUFactory(CPUAbstractFactory):
    def interface(self):
        return "AMDCPU接口"


class KingstonFlashFactory(FlashAbstractFactory):
    def interface(self):
        return "Kingston内存接口"
class DellFlashFactory(FlashAbstractFactory):
    def interface(self):
        return "Dell内存接口"


class ComputerAbstractProduct(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def open(self):
        pass

class XMProduct(ComputerAbstractProduct):
    def __init__(self, cpu, flash):
        self.cpu = cpu
        self.flash = flash

    def open(self):
        return "小米笔记本开机,配置cpu:{}, 内存:{}".format(self.cpu, self.flash)

class LenovoProduct(ComputerAbstractProduct):
    def __init__(self, cpu, flash):
        self.cpu = cpu
        self.flash = flash
    def open(self):
        return "联想笔记本开机,配置cpu:{}, 内存:{}".format(self.cpu, self.flash)

class ComputerAbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_product(self):
        pass

class XMComputerFactory(ComputerAbstractFactory):
    def create_product(self):
        cpu = InterCPUFactory()
        flash = DellFlashFactory()
        return XMProduct(cpu, flash)


class LenovoComputerFactory(ComputerAbstractFactory):
    def create_product(self):
        cpu = InterCPUFactory()
        flash = DellFlashFactory()
        return LenovoProduct(cpu, flash)



if __name__ == '__main__':

    xiaomi = XMComputerFactory().create_product()
    lenovo = LenovoComputerFactory().create_product()

    print(xiaomi.open())
    print(lenovo.open())

"""
优点:
    抽象工厂模式隔离了具体类的生成，使得客户并不需要知道什么被创建。
    由于这种隔离，更换一个具体工厂就变得相对容易。
    所有的具体工厂都实现了抽象工厂中定义的那些公共接口，因此只需改变具体工厂的实例，就可以在某种程度上改变整个软件系统的行为。
    应用抽象工厂模式可以实现高内聚低耦合的设计目的，因此抽象工厂模式得到了广泛的应用。
    当一个产品族中的多个对象被设计成一起工作时，它能够保证客户端始终只使用同一个产品族中的对象。
    需要根据当前环境来决定其行为的软件系统
    增加新的具体工厂和产品族很方便，无须修改已有系统，符合“开闭原则”。
    
    
缺点:
    在添加新的产品对象时，难以扩展抽象工厂来生产新种类的产品，这是因为在抽象工厂角色中规定了所有可能被创建的产品集合
    要支持新种类的产品就意味着要对该接口进行扩展，而这将涉及到对抽象工厂角色及其所有子类的修改，显然会带来较大的不便。
    开闭原则的倾斜性（增加新的工厂和产品族容易，增加新的产品等级结构麻烦）
"""

"""
适用环境:
    一个系统不应当依赖于产品类实例如何被创建、组合和表达的细节,这对于所有类型的工厂模式都是重要的。
    系统中有多于一个的产品族，而每次只使用其中某一产品族。
    属于同一个产品族的产品将在一起使用，这一约束必须在系统的设计中体现出来。
    系统提供一个产品类的库，所有的产品以同样的接口出现，从而使客户端不依赖于具体实现。
在很多软件系统中需要更换界面主题，要求界面中的按钮、文本框、背景色等一起发生改变时，可以使用抽象工厂模式进行设计。
"""

"""
“开闭原则”的倾斜性
    1. 增加产品族：对于增加新的产品族，工厂方法模式很好的支持了“开闭原则”，对于新增加的产品族，只需要对应增加一个新的具体工厂即可，对已有代码无须做任何修改。
"""