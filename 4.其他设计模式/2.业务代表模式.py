"""Business Delegate Pattern"""

"""
模式定义:
    业务代表模式（Business Delegate Pattern）用于对表示层和业务层解耦。
    它基本上是用来减少通信或对表示层代码中的业务层代码的远程查询功能。
    在业务层中我们有以下实体。
"""

"""
业务代表:
    客户端（Client）: 表示层代码可以是 JSP、servlet 或 UI java 代码。
    业务代表（Business Delegate） - 一个为客户端实体提供的入口类，它提供了对业务服务方法的访问。
    查询服务（LookUp Service） - 查找服务对象负责获取相关的业务实现，并提供业务对象对业务代表对象的访问。
    业务服务（Business Service） - 业务服务接口。实现了该业务服务的实体类，提供了实际的业务实现逻辑。
    
"""

"""
实现:
    
"""
import abc

class BusinessService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def doProcessing(self):pass

class EJBService(BusinessService):
    # 实体服务类
    def doProcessing(self):
        print("Processing task by invoking EJB Service")

class JMSService(BusinessService):
    # 实体服务类
    def doProcessing(self):
        print("Processing task by invoking JMS Service")

class BusinessLookUp():
    # 创建业务查询服务
    def getBusinessService(self, serviceType):
        if str(serviceType).__eq__("EJB"):
            return EJBService()
        else:
            return JMSService()

class BusinessDelegate():
    # 创建业务代表
    def setServiceType(self, serviceType):
        self.serviceType = serviceType


    def doTask(self):
        businessService = BusinessLookUp().getBusinessService(self.serviceType)
        businessService.doProcessing()

class Client():
    def __init__(self, businessService):
        self.businessService = businessService

    def doTask(self):
        self.businessService.doTask()

if __name__ == '__main__':

    # 1. 创建一个业务代表
    businessDelegate = BusinessDelegate()

    # 2. 根据客户选择服务类型
    businessDelegate.setServiceType("EJB")
    client = Client(businessDelegate)
    client.doTask()

    businessDelegate.setServiceType("JMS")
    client.doTask()