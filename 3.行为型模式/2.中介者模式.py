"""Mediator Pattern"""
"""
模式动机
    降低多个对象和类之间的通信复杂性
    这种模式提供了一个中介类，该类通常处理不同类之间的通信，并支持松耦合，使代码易于维护。
    中介者模式属于行为型模式。
    在用户与用户直接聊天的设计方案中，用户对象之间存在很强的关联性，将导致系统出现如下问题：
    1. 系统结构复杂：
        对象之间存在大量的相互关联和调用，
        若有一个对象发生变化，则需要跟踪和该对象关联的其他所有对象，并进行适当处理。
    2. 对象可重用性差：
        由于一个对象和其他对象具有很强的关联，若没有其他对象的支持，
        一个对象很难被另一个系统或模块重用，这些对象表现出来更像一个不可分割的整体，职责较为混乱。
    3. 系统扩展性低：
        增加一个新的对象需要在原有相关对象上增加引用，
        增加新的引用关系也需要调整原有对象，系统耦合度很高，对象操作很不灵活，扩展性差。

    4. 在面向对象的软件设计与开发过程中，根据“单一职责原则”，我们应该尽量将对象细化，使其只负责或呈现单一的职责。
    5. 对于一个模块，可能由很多对象构成，而且这些对象之间可能存在相互的引用
        为了减少对象两两之间复杂的引用关系，使之成为一个松耦合的系统，我们需要使用中介者模式
"""

"""
模式定义
    中介者模式(Mediator Pattern)定义：
        用一个中介对象来封装一系列的对象交互，
        中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。
        中介者模式又称为调停者模式，它是一种对象行为型模式。
"""

"""
模式结构
    Mediator: 抽象中介者
    ConcreteMediator: 具体中介者
    Colleague: 抽象同事类
    ConcreteColleague: 具体同事类
"""

"""
意图：
    用一个中介对象来封装一系列的对象交互，
    中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。
主要解决：
    对象与对象之间存在大量的关联关系，这样势必会导致系统的结构变得很复杂，
    同时若一个对象发生改变，我们也需要跟踪与之相关联的对象，同时做出相应的处理。
何时使用：
    多个类相互耦合，形成了网状结构。
如何解决：将上述网状结构分离为星型结构。
关键代码：对象 Colleague 之间的通信封装到一个类中单独处理。
应用实例： 
    1、中国加入 WTO 之前是各个国家相互贸易，结构复杂，现在是各个国家通过 WTO 来互相贸易。
     2、机场调度系统。 
     3、MVC 框架，其中C（控制器）就是 M（模型）和 V（视图）的中介者。
优点： 
    1、降低了类的复杂度，将一对多转化成了一对一。 
    2、各个类之间的解耦。 
    3、符合迪米特原则。
缺点：中介者会庞大，变得复杂难以维护。
使用场景： 
    1、系统中对象之间存在比较复杂的引用关系，导致它们之间的依赖关系结构混乱而且难以复用该对象。 
    2、想通过一个中间类来封装多个类中的行为，而又不想生成太多的子类。

"""

"""
实例：
    我们通过聊天室实例来演示中介者模式
    实例中，多个用户可以向聊天室发送消息，聊天室向所有的用户显示消息。
    ChatRoom 和 User
    User 对象使用 ChatRoom 方法来分享他们的消息。
"""
from datetime import datetime
class ChatRoom():
    @classmethod
    def showMessage(self, user, message):
        print("{}\tuser:{}:{}".format(datetime.now(), user.getName(), message))
class User():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def sendMessage(self, message):
        ChatRoom.showMessage(self, message)


if __name__ == '__main__':
    robert = User("Robert")
    john = User("John")
    robert.sendMessage("Hi! John!")
    john.sendMessage("Hello! Robert!")

"""
    在现实生活中，有很多中介者模式的身影，
    例如QQ游戏平台，聊天室、QQ群、短信平台和房产中介。不论是QQ游戏还是QQ群，它们都是充当一个中间平台
    QQ用户可以登录这个中间平台与其他QQ用户进行交流
    如果没有这些中间平台，我们如果想与朋友进行聊天的话，可能就需要当面才可以了
    电话、短信也同样是一个中间平台，有了这个中间平台，每个用户都不要直接依赖与其他用户，只需要依赖这个中间平台就可以了，一切操作都由中间平台去分发。
    
    中介者模式，定义了一个中介对象来封装一系列对象之间的交互关系。
    中介者使各个对象之间不需要显式地相互引用，从而使耦合性降低，而且可以独立地改变它们之间的交互行为。
"""