"""Observer Pattern"""

"""
模式动机
    当对象间存在一对多关系时，则使用观察者模式（Observer Pattern）。
    比如，当一个对象被修改时，则会自动通知它的依赖对象。观察者模式属于行为型模式。

    建立一种对象与对象之间的依赖关系，
    一个对象发生改变时将自动通知其他对象，
    其他对象将相应做出反应。
    发生改变的对象称为观察目标，而被通知的对象称为观察者，一个观察目标可以对应多个观察者
    而且这些观察者之间没有相互联系，可以根据需要增加和删除观察者，使得系统更易于扩展，这就是观察者模式的模式动机。
"""

"""
模式定义
    观察者模式(Observer Pattern)：
        定义对象间的一种一对多依赖关系，使得每当一个对象状态发生改变时，其相关依赖对象皆得到通知并被自动更新。
        观察者模式又叫做发布-订阅（Publish/Subscribe）模式、
        模型-视图（Model/View）模式、
        源-监听器（Source/Listener）模式
        从属者（Dependents）模式。
    观察者模式是一种对象行为型模式。
"""

"""
模式结构
    Subject: 目标
    ConcreteSubject: 具体目标
    Observer: 观察者
    ConcreteObserver: 具体观察者
"""

"""
意图：
    定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。
主要解决：
    一个对象状态改变给其他对象通知的问题，而且要考虑到易用和低耦合，保证高度的协作。
何时使用：
    一个对象（目标对象）的状态发生改变，所有的依赖对象（观察者对象）都将得到通知，进行广播通知。
如何解决：
    使用面向对象技术，可以将这种依赖关系弱化。
关键代码：在抽象类里有一个 ArrayList 存放观察者们。
应用实例： 
    1、拍卖的时候，拍卖师观察最高标价，然后通知给其他竞价者竞价。 
    2、西游记里面悟空请求菩萨降服红孩儿，菩萨洒了一地水招来一个老乌龟，这个乌龟就是观察者，他观察菩萨洒水这个动作。
优点： 
    1、观察者和被观察者是抽象耦合的。 
    2、建立一套触发机制。
缺点： 
    1、如果一个被观察者对象有很多的直接和间接的观察者的话，将所有的观察者都通知到会花费很多时间。
    2、如果在观察者和观察目标之间有循环依赖的话，观察目标会触发它们之间进行循环调用，可能导致系统崩溃。 
    3、观察者模式没有相应的机制让观察者知道所观察的目标对象是怎么发生变化的，而仅仅只是知道观察目标发生了变化。
使用场景：
    1. 一个抽象模型有两个方面，其中一个方面依赖于另一个方面。
    2. 将这些方面封装在独立的对象中使它们可以各自独立地改变和复用。
    3. 一个对象的改变将导致其他一个或多个对象也发生改变，而不知道具体有多少对象将发生改变，可以降低对象之间的耦合度。
    4. 一个对象必须通知其他对象，而并不知道这些对象是谁。
    5. 需要在系统中创建一个触发链，A对象的行为将影响B对象，B对象的行为将影响C对象……，可以使用观察者模式创建一种链式触发机制。
    
"""

"""
注意事项:
     1、JAVA 中已经有了对观察者模式的支持类。
     2、避免循环引用。 
     3、如果顺序执行，某一观察者错误会导致系统卡壳，一般采用异步方式。
"""

"""
实现:
    观察者模式使用三个类 Subject、Observer 和 Client
    Subject 对象带有绑定观察者到 Client 对象和从 Client 对象解绑观察者的方法。
    我们创建 Subject 类、Observer 抽象类和扩展了抽象类 Observer 的实体类。
    
"""
import abc

class Subject(object):
    observers = []
    state = 0

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
        self.notifyAllObservers()

    def attach(self, observer):
        self.observers.append(observer)

    def notifyAllObservers(self):
        for observer in self.observers:
            observer.update()

# 观察者
class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        pass

class BinaryObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print("BinaryObserver:{}".format(self.subject.getState()))

class OctalObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print("BinaryObserver:{}".format(self.subject.getState()))

class HexaObserver(Observer):

    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print("BinaryObserver:{}".format(self.subject.getState()))


if __name__ == '__main__':
    subject = Subject()  # 发布者


    # 观察者
    HexaObserver(subject)
    OctalObserver(subject)
    BinaryObserver(subject)

    print("subject state 1")
    subject.setState(1)

    print("subject state 2")
    subject.setState(2)


"""
模式分析
    观察者模式描述了如何建立对象与对象之间的依赖关系，如何构造满足这种需求的系统。
    这一模式中的关键对象是观察目标和观察者，一个目标可以有任意数目的与之相依赖的观察者，
    一旦目标的状态发生改变，所有的观察者都将得到通知。
    作为对这个通知的响应，每个观察者都将即时更新自己的状态，以与目标状态同步，这种交互也称为发布-订阅(publishsubscribe)。
    目标是通知的发布者，它发出通知时并不需要知道谁是它的观察者，可以有任意数目的观察者订阅它并接收通
"""

"""
优点:
    1. 观察者模式可以实现表示层和数据逻辑层的分离，并定义了稳定的消息更新传递机制，抽象了更新接口，使得可以有各种各样不同的表示层作为具体观察者角色。
    2. 观察者模式在观察目标和观察者之间建立一个抽象的耦合。
    3. 观察者模式支持广播通信。
    4. 观察者模式符合“开闭原则”的要求。
"""

"""
缺点:
    1. 如果一个观察目标对象有很多直接和间接的观察者的话，将所有的观察者都通知到会花费很多时间。
    2. 如果在观察者和观察目标之间有循环依赖的话，观察目标会触发它们之间进行循环调用，可能导致系统崩溃。
    3. 观察者模式没有相应的机制让观察者知道所观察的目标对象是怎么发生变化的，而仅仅只是知道观察目标发生了变化。
"""

"""
适用环境
    一个抽象模型有两个方面，其中一个方面依赖于另一个方面。将这些方面封装在独立的对象中使它们可以各自独立地改变和复用。
    一个对象的改变将导致其他一个或多个对象也发生改变，而不知道具体有多少对象将发生改变，可以降低对象之间的耦合度。
    一个对象必须通知其他对象，而并不知道这些对象是谁。
    需要在系统中创建一个触发链，A对象的行为将影响B对象，B对象的行为将影响C对象……，可以使用观察者模式创建一种链式触发机制。
"""

"""
模式应用
    观察者模式在软件开发中应用非常广泛，如某电子商务网站可以在执行发送操作后给用户多个发送商品打折信息，
    某团队战斗游戏中某队友牺牲将给所有成员提示等等，
    凡是涉及到一对一或者一对多的对象交互场景都可以使用观察者模式。
"""

"""
MVC模式
    MVC模式是一种架构模式，
    它包含三个角色：模型(Model)，视图(View)和控制器(Controller)。
    观察者模式可以用来实现MVC模式，
    观察者模式中的观察目标就是MVC模式中的模型(Model)，
    而观察者就是MVC中的视图(View)，
    控制器(Controller)充当两者之间的中介者(Mediator)。当模型层的数据发生改变时，视图层将自动改变其显示内容。
"""