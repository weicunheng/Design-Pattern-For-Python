"""Command Pattern"""
"""
模式动机:
    在软件设计中，我们经常需要向某些对象发送请求
    但是并不知道请求的接收者是谁
    也不知道被请求的操作是哪个
    我们只需在程序运行时指定具体的请求接收者即可
    python manage.py runserver 0:8080
    此时，可以使用命令模式来进行设计，使得请求发送者与请求接收者消除彼此之间的耦合，让对象之间的调用关系更加灵活。
    命令模式可以对发送者和接收者完全解耦
    发送者与接收者之间没有直接引用关系,发送请求的对象只需要知道如何发送请求，而不必知道如何完成请求。这就是命令模式的模式动机。
    
"""

"""
模式定义:
    命令模式(Command Pattern)：将一个请求封装为一个对象,
    从而使我们可用不同的请求对客户进行参数化；对请求排队或者记录请求日志，以及支持可撤销的操作。
    命令模式是一种对象行为型模式，其别名为动作(Action)模式或事务(Transaction)模式。
"""

"""
模式结构
    Command: 抽象命令类
    ConcreteCommand: 具体命令类
    Invoker: 调用者
    Receiver: 接收者
    Client:客户类
"""

"""
命令模式（Command Pattern）是一种数据驱动的设计模式，它属于行为型模式。
请求以命令的形式包裹在对象中，并传给调用对象。调用对象寻找可以处理该命令的合适的对象，并把该命令传给相应的对象，该对象执行命令。
意图：
    将一个请求封装成一个对象，从而使您可以用不同的请求对客户进行参数化。
主要解决：
    在软件系统中，行为请求者与行为实现者通常是一种紧耦合的关系，但某些场合，
    比如需要对行为进行记录、撤销或重做、事务等处理时，这种无法抵御变化的紧耦合的设计就不太合适。
何时使用:
    在某些场合，比如要对行为进行"记录、撤销/重做、事务"等处理，这种无法抵御变化的紧耦合是不合适的。
    在这种情况下，如何将"行为请求者"与"行为实现者"解耦？将一组行为抽象为对象，可以实现二者之间的松耦合。
如何解决：
    通过调用者调用接受者执行命令，顺序：调用者→接受者→命令。
关键代码:
    1、received 真正的命令执行对象 
    2、Command 
    3、invoker 使用命令对象的入口
优点
    1、降低了系统耦合度。 
    2、新的命令可以很容易添加到系统中去。
缺点
    使用命令模式可能会导致某些系统有过多的具体命令类。
使用场景:
    认为是命令的地方都可以使用命令模式，比如： 1、GUI 中每一个按钮都是一条命令。 2、模拟 CMD。
     
"""

"""
1. 首先创建作为命令接口Order
2. 然后创建作为请求的Stock类
3. 实体命令类 BuyStock 和 SellStock，实现了 Order 接口，将执行实际的命令处理。
4. 创建作为调用对象的类 Broker，它接受订单并能下订单。
5. Broker 对象使用命令模式，基于命令的类型确定哪个对象执行哪个命令。
"""
import abc


class Order(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def excute(self):pass


class Stock(object):
    name = "ABC"
    quantity = 10

    def buy(self):
        print("Stock [ Name: "+ self.name +", Quantity: " + str(self.quantity) +" ] bought")

    def sell(self):
        print("Stock [ Name: " + self.name + ", Quantity: " + str(self.quantity) +"] sold")

class BuyStock(Order):


    def __init__(self, abcStock):
        self.abcStock = abcStock

    def excute(self):
        self.abcStock.buy()


class SellStock(Order):

    def __init__(self, abcStock):
        self.abcStock = abcStock

    def excute(self):
        self.abcStock.sell()


class Broker():
    orderList = []

    def takeOrder(self, order):
        self.orderList.append(order)

    def placeOrders(self):
        for i in self.orderList:
            i.excute()


if __name__ == '__main__':
    stock =  Stock()
    buyStockOrder = BuyStock(stock)
    sellStockOrder = SellStock(stock)
    broker = Broker()
    broker.takeOrder(buyStockOrder)
    broker.takeOrder(sellStockOrder)

    broker.placeOrders()

"""
优点:
    降低系统的耦合度。
    新的命令可以很容易地加入到系统中。
    可以比较容易地设计一个命令队列和宏命令（组合命令）。
    可以方便地实现对请求的Undo和Redo。

缺点
    使用命令模式可能会导致某些系统有过多的具体命令类。
    因为针对每一个命令都需要设计一个具体命令类，因此某些系统可能需要大量具体命令类，这将影响命令模式的使用。
"""

"""
模式应用

    很多系统都提供了宏命令功能，
    如UNIX平台下的Shell编程，可以将多条命令封装在一个命令对象中，
    只需要一条简单的命令即可执行一个命令序列，这也是命令模式的应用实例之一。
"""