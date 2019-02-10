"""Strategy Pattern"""
"""
模式动机:
    完成一项任务，往往可以有多种不同的方式，每一种方式称为一个策略
    我们可以根据环境或者条件的不同选择不同的策略来完成该项任务。
    在软件开发中也常常遇到类似的情况，实现某一个功能有多个途径，此时可以使用一种设计模式来使得系统可以灵活地选择解决途径，也能够方便地增加新的解决途径。
    在软件系统中，有许多算法可以实现某一功能，如查找、排序等，
    一种常用的方法是硬编码(Hard Coding)在一个类中，
    如需要提供多种查找算法，可以将这些算法写到一个类中，在该类中提供多个方法，每一个方法对应一个具体的查找算法；
    当然也可以将这些查找算法封装在一个统一的方法中，通过if…else…等条件判断语句来进行选择。
    这两种实现方法我们都可以称之为硬编码，如果需要增加一种新的查找算法，需要修改封装算法类的源代码；更换查找算法，也需要修改客户端调用代码。
    在这个算法类中封装了大量查找算法，该类代码将较复杂，维护较为困难。
    
    为了解决这些问题，可以定义一些独立的类来封装不同的算法，每一个类封装一个具体的算法，
    在这里，每一个封装算法的类我们都可以称之为策略(Strategy)
    为了保证这些策略的一致性，一般会用一个抽象的策略类来做算法的定义，而具体每种算法则对应于一个具体策略类。
"""

"""
模式定义:
    策略模式(Strategy Pattern)：定义一系列算法，将每一个算法封装起来，并让它们可以相互替换。
    策略模式让算法独立于使用它的客户而变化，也称为政策模式(Policy)。
    策略模式是一种对象行为型模式。
    创建各种策略的对象 和 一个行为随着策略对象改变而改变的 context 对象。策略对象改变 context 对象的执行算法。
"""
"""
模式结构
    Context: 环境类
    Strategy: 抽象策略类
    ConcreteStrategy: 具体策略类
"""
"""
意图：定义一系列的算法,把它们一个个封装起来, 并且使它们可相互替换。

主要解决：在有多种算法相似的情况下，使用 if...else 所带来的复杂和难以维护。

何时使用：一个系统有许多许多类，而区分它们的只是他们直接的行为。

如何解决：将这些算法封装成一个一个的类，任意地替换。

关键代码：实现同一个接口。

应用实例： 
    1、诸葛亮的锦囊妙计，每一个锦囊就是一个策略。 
    2、旅行的出游方式，选择骑自行车、坐汽车，每一种旅行方式都是一个策略。 
    3、JAVA AWT 中的 LayoutManager。

优点： 
    1、算法可以自由切换。
    2、避免使用多重条件判断。 
    3、扩展性良好。

缺点： 
    1、策略类会增多。 
    2、所有策略类都需要对外暴露。

使用场景： 
    1、如果在一个系统里面有许多类，它们之间的区别仅在于它们的行为，那么使用策略模式可以动态地让一个对象在许多行为中选择一种行为。
     2、一个系统需要动态地在几种算法中选择一种。 3、如果一个对象有很多的行为，如果不用恰当的模式，这些行为就只好使用多重的条件选择语句来实现。

注意事项：如果一个系统的策略多于四个，就需要考虑使用混合模式，解决策略类膨胀的问题。
"""
import abc

# 抽象策略类
class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def doOperation(self, num1, num2):
        pass

# 具体策略类
class OperationAdd(Strategy):

    def doOperation(self, num1, num2):
        return num1 + num2

class OperationSubstract(Strategy):

    def doOperation(self, num1, num2):
        return num1 - num2

class OperationMultiply(Strategy):

    def doOperation(self, num1, num2):
        return num1 * num2



# 使用某种策略
class Context(object):

    def __init__(self, strategy):
        self.strategy = strategy

    def executeStrategy(self, num1, num2):
        return self.strategy.doOperation(num1, num2)


if __name__ == '__main__':

    context = Context(OperationMultiply())
    print(context.executeStrategy(1, 2))

"""
和状态模式的区别:
    状态模式的类图和策略模式类似，并且都是能够动态改变对象的行为。
    但是状态模式是通过状态转移来改变 Context 所组合的 State 对象，
    而策略模式是通过 Context 本身的决策来改变组合的 Strategy 对象。
    所谓的状态转移，是指 Context 在运行过程中由于一些条件发生改变而使得 State 对象发生改变，注意必须要是在运行过程中。

    状态模式主要是用来解决状态转移的问题，当状态发生转移了，那么 Context 对象就会改变它的行为；
    而策略模式主要是用来封装一组可以互相替代的算法族，并且可以根据需要动态地去替换 Context 使用的算法。
"""