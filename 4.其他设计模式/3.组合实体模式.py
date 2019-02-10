"""Composite Entity Pattern"""
"""
组合实体模式（Composite Entity Pattern）用在 EJB 持久化机制中。
一个组合实体是一个 EJB 实体 bean，代表了对象的图解。
当更新一个组合实体时，内部依赖对象 beans 会自动更新，因为它们是由 EJB 实体 bean 管理的

    组合实体（Composite Entity） - 它是主要的实体 bean。它可以是粗粒的，或者可以包含一个粗粒度对象，用于持续生命周期。
    粗粒度对象（Coarse-Grained Object） - 该对象包含依赖对象。它有自己的生命周期，也能管理依赖对象的生命周期。
    依赖对象（Dependent Object） - 依赖对象是一个持续生命周期依赖于粗粒度对象的对象。
    策略（Strategies） - 策略表示如何实现组合实体

"""

"""
实现
    创建依赖对象。
    创建组合实体
    
"""
class DependentObject1():
    data = None

    def set_date(self, data):
        self.data = data

    def get_data(self):
        return self.data

class DependentObject2():
    data = None

    def set_date(self, data):
        self.data = data

    def get_data(self):
        return self.data

# 创建粗粒对象
class CoarseGrainedObject():
    do1 = DependentObject1()
    do2 = DependentObject2()

    def setData(self, data1, data2):
        self.do1.set_date(data1)
        self.do2.set_date(data2)

    def getData(self):
        return [self.do1.get_data(), self.do2.get_data()]

# 创建组合实体
class CompositeEntity():
    cgo = CoarseGrainedObject()
    def setData(self, data1, data2):
        self.cgo.setData(data1, data2)

    def get_data(self):
        return self.cgo.getData()

# 创建使用组合实体的客户端类。
class Client():
    compositeEntity = CompositeEntity()

    def printData(self):
        for i in range(len(self.compositeEntity.get_data())):
            print("Data:{}".format(self.compositeEntity.get_data()[i]))

    def set_data(self, data1, data2):
        self.compositeEntity.setData(data1, data2)

if __name__ == '__main__':

    client = Client()
    client.set_data(1,2)
    client.printData()
    client.set_data("Second Test", "Data1")
    client.printData()