"""Builder Pattern"""
"""
无论是在现实世界中还是在软件系统中，都存在一些复杂的对象
它们拥有多个组成部分，如汽车，它包括车轮、方向盘、发送机等各种部件。
而对于大多数用户而言，无须知道这些部件的装配细节，也几乎不会使用单独某个部件，而是使用一辆完整的汽车
可以通过建造者模式对其进行设计与描述，
建造者模式可以将部件和其组装过程分开，一步一步创建一个复杂的对象。
用户只需要指定复杂对象的类型就可以得到该对象，而无须知道其内部的具体构造细节。
"""

"""
在软件开发中，也存在大量类似汽车一样的复杂对象，
它们拥有一系列成员属性，这些成员属性中有些是引用类型的成员对象。
而且在这些复杂对象中，还可能存在一些限制条件，如某些属性没有赋值则复杂对象不能作为一个完整的产品使用；
有些属性的赋值必须按照某个顺序，一个属性没有赋值之前，另一个属性可能无法赋值等。
"""

"""
复杂对象相当于一辆有待建造的汽车，而对象的属性相当于汽车的部件，建造产品的过程就相当于组合部件的过程。
由于组合部件的过程很复杂，因此，这些部件的组合过程往往被“外部化”到一个称作建造者的对象里，建造者返还给客户端的是一个已经建造完毕的完整产品对象，
而用户无须关心该对象所包含的属性以及它们的组装方式，这就是建造者模式的模式动机。

对象: 一辆汽车
对象的属性: 汽车的部件
建造产品: 组合部件
"""

"""
模式定义
    造者模式(Builder Pattern)：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
    建造者模式是一步一步创建一个复杂的对象，
    它允许用户只通过指定复杂对象的类型和内容就可以构建它们，
    用户不需要知道内部的具体构建细节。建造者模式属于对象创建型模式。根据中文翻译的不同，建造者模式又可以称为生成器模式。
"""
"""
模式结构
   Builder: 抽象的建造者
   ConcreateBuilder: 具体建造者
   Director: 指挥者
   Product: 产品角色    
1. 实例化一个具体的汽车建造者
2. 实例化一个指挥官
3. 指挥官指定一个建造者
4. 建造者建造产品
5. 产品使用
"""

"""
模式分析:
    1. 抽象建造者类中定义了产品的创建方法和返回方法;
    2. 建造者模式的结构中还引入了一个指挥者类Director
        2.1 一方面它隔离了客户与生产过程；
        2.2 另一方面它负责控制产品的生成过程
    3. 指挥者针对抽象建造者编程
    4. 客户端只需要知道具体建造者的类型，即可通过指挥者类调用建造者的相关方法，返回一个完整的产品对象
    5. 在客户端代码中，无须关心产品对象的具体组装过程，只需确定具体建造者的类型即可
    6. 建造者模式将复杂对象的构建与对象的表现分离开来，这样使得同样的构建过程可以创建出不同的表现。
"""
import abc

class Packing(metaclass=abc.ABCMeta):
    """
    包装: 纸袋包装 / 瓶子包装
    """
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "{}类型的包装".format(self.type)

class Wrapper(Packing):
    def __init__(self):
        super().__init__('wrapper')
class Bottle(Packing):
    def __init__(self):
        super().__init__('bottle')

class Item(metaclass=abc.ABCMeta):
    """
    表示食物条目:汉堡 / 冷饮等
    """
    def __init__(self, name, packing, price):
        self.name = name
        self.packing = packing
        self.price = price

    def __str__(self):
        print("{}价格:{}".format(self.name, self.price))

class Burger(Item):
    def __init__(self, name, packing, price):
        super().__init__(name, packing, price)

    def __str__(self):
        print("{}价格:{}".format(self.name, self.price))
class ColdDrink(Item):
    def __init__(self, name, packing, price):
        super().__init__(name, packing, price)

    def __str__(self):
        print("{}价格:{}".format(self.name, self.price))

class VegBurger(Burger):
    price = 10
    name = "蔬菜汉堡包"
    packing = Wrapper()
    def __init__(self,):
        super().__init__(self.name, self.packing, self.price)

class ChickenBurger (Burger):
    price = 20
    name = "鸡腿汉堡包"
    packing = Wrapper()
    def __init__(self,):
        super().__init__(self.name, self.packing, self.price)

class Coke(ColdDrink):
    price = 2
    name = "可口可乐"
    packing = Bottle()
    def __init__(self,):
        super().__init__(self.name, self.packing, self.price)
class Pepsi(ColdDrink):
    price = 2
    name = "百事可乐"
    packing = Bottle()
    def __init__(self,):
        super().__init__(self.name, self.packing, self.price)



class Meal(metaclass=abc.ABCMeta):

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_cost(self):
        cost = 0
        for item in self.items:
            cost += item.price
        return cost

    def show_item(self):
        for item in self.items:
            print("名称:{}, 包装:{}, 价格:{}".format(item.name, item.packing, item.price))

class MealBuilder():
    """
    实际的builder类负责创建Meal对象
    """
    def prepareVegMeal(self):
        meal = Meal()
        meal.add_item(VegBurger())
        meal.add_item(Coke())
        return meal


    def prepareNonVegMeal(self):
        meal = Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())
        return meal

class BuilderPatternDemo():
    @classmethod
    def main(cls):
        mealBuilder = MealBuilder()
        vegMeal = mealBuilder.prepareVegMeal()
        print("蔬菜汉堡套餐:")
        vegMeal.show_item()
        print("总消费为:{}".format(vegMeal.get_cost()))

        mealBuilder1 = MealBuilder()
        nonVegMeal = mealBuilder1.prepareNonVegMeal()
        print("\n\n鸡肉汉堡套餐:")
        nonVegMeal.show_item()
        print("总消费为:{}".format(nonVegMeal.get_cost()))



if __name__ == '__main__':
    BuilderPatternDemo().main()

"""
实例:
    KFC套餐
    建造者模式可以用于描述KFC如何创建套餐：
        1. 套餐是一个复杂对象，它一般包含主食（如汉堡、鸡肉卷等）和饮料（如果汁、 可乐等）等组成部分
        2. 不同的套餐有不同的组成部分
        3. 而KFC的服务员可以根据顾客的要求，一步一步装配这些组成部分，构造一份完整的套餐，然后返回给顾客。
    建造者模式举例：去肯德基点餐，我们可以认为点餐就属于一个建造订单的过程。
    我们点餐的顺序是无关的，点什么东西也是没有要求的，可以单点，也可以点套餐，也可以套餐加单点，但是最后一定要点确认来完成订单。
"""

"""
优点:
    1. 在建造者模式中， 客户端不必知道产品内部组成的细节
    2. 将产品本身与产品的创建过程解耦
    3. 使得相同的创建过程可以创建不同的产品对象。
    4. 每一个具体建造者都相对独立，而与其他的具体建造者无关
    5. 因此可以很方便地替换具体建造者或增加新的具体建造者， 用户使用不同的具体建造者即可得到不同的产品对象 。
    6. 可以更加精细地控制产品的创建过程 (将复杂产品的创建步骤分解在不同的方法中，使得创建过程更加清晰，也更方便使用程序来控制创建过程。)
    7. 增加新的具体建造者无须修改原有类库的代码，指挥者类针对抽象建造者类编程，系统扩展方便，符合“开闭原则”。
"""
"""
缺点:
    1. 建造者模式所创建的产品一般具有较多的共同点，其组成部分相似，如果产品之间的差异性很大，则不适合使用建造者模式，因此其使用范围受到一定的限制。
    2. 如果产品的内部变化复杂，可能会导致需要定义很多具体建造者类来实现这种变化，导致系统变得很庞大。
"""

"""
在以下情况下可以使用建造者模式：
    需要生成的产品对象有复杂的内部结构，这些产品对象通常包含多个成员属性。
    需要生成的产品对象的属性相互依赖，需要指定其生成顺序。
    对象的创建过程独立于创建该对象的类。在建造者模式中引入了指挥者类，将创建过程封装在指挥者类中，而不在建造者类中。
    隔离复杂对象的创建和使用，并使得相同的创建过程可以创建不同的产品。
"""
"""
模式应用:
    在很多游戏软件中，
    地图包括天空、地面、背景等组成部分，
    人物角色包括人体、服装、装备等组成部分，
    可以使用建造者模式对其进行设计，通过不同的具体建造者创建不同类型的地图或人物。
"""

"""
模式扩展:
    建造者模式的简化:

    省略抽象建造者角色：如果系统中只需要一个具体建造者的话，可以省略掉抽象建造者。
    省略指挥者角色：在具体建造者只有一个的情况下，如果抽象建造者角色已经被省略掉，那么还可以省略指挥者角色，让
    Builder角色扮演指挥者与建造者双重角色。

建造者模式与抽象工厂模式的比较:

    与抽象工厂模式相比， 建造者模式返回一个组装好的完整产品 ，而 抽象工厂模式返回一系列相关的产品，这些产品位于不同的产品等级结构，构成了一个产品族。
    在抽象工厂模式中，客户端实例化工厂类，然后调用工厂方法获取所需产品对象，而在建造者模式中，客户端可以不直接调用建造者的相关方法，而是通过指挥者类来指导如何生成对象，包括对象的组装过程和建造步骤，它侧重于一步步构造一个复杂对象，返回一个完整的对象。
    如果将抽象工厂模式看成 汽车配件生产工厂 ，生产一个产品族的产品，那么建造者模式就是一个 汽车组装工厂 ，通过对部件的组装可以返回一辆完整的汽车。
"""

"""
建造者模式将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。建造者模式是一步一步创建一个复杂的对象，它允许用户只通过指定复杂对象的类型和内容就可以构建它们，用户不需要知道内部的具体构建细节。建造者模式属于对象创建型模式。
建造者模式包含如下四个角色：抽象建造者为创建一个产品对象的各个部件指定抽象接口；具体建造者实现了抽象建造者接口，实现各个部件的构造和装配方法，定义并明确它所创建的复杂对象，也可以提供一个方法返回创建好的复杂产品对象；产品角色是被构建的复杂对象，包含多个组成部件；指挥者负责安排复杂对象的建造次序，指挥者与抽象建造者之间存在关联关系，可以在其construct()建造方法中调用建造者对象的部件构造与装配方法，完成复杂对象的建造
在建造者模式的结构中引入了一个指挥者类，该类的作用主要有两个：一方面它隔离了客户与生产过程；另一方面它负责控制产品的生成过程。指挥者针对抽象建造者编程，客户端只需要知道具体建造者的类型，即可通过指挥者类调用建造者的相关方法，返回一个完整的产品对象。
建造者模式的主要优点在于客户端不必知道产品内部组成的细节，将产品本身与产品的创建过程解耦，使得相同的创建过程可以创建不同的产品对象，每一个具体建造者都相对独立，而与其他的具体建造者无关，因此可以很方便地替换具体建造者或增加新的具体建造者，符合“开闭原则”，还可以更加精细地控制产品的创建过程；其主要缺点在于由于建造者模式所创建的产品一般具有较多的共同点，其组成部分相似，因此其使用范围受到一定的限制，如果产品的内部变化复杂，可能会导致需要定义很多具体建造者类来实现这种变化，导致系统变得很庞大。
建造者模式适用情况包括：需要生成的产品对象有复杂的内部结构，这些产品对象通常包含多个成员属性；需要生成的产品对象的属性相互依赖，需要指定其生成顺序；对象的创建过程独立于创建该对象的类；隔离复杂对象的创建和使用，并使得相同的创建过程可以创建不同类型的产品。
"""