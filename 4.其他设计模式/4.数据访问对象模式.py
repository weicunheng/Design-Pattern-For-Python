"""Data Access Object Pattern"""
"""
数据访问对象模式（Data Access Object Pattern）或 DAO 模式用于把低级的数据访问 API 或操作从高级的业务服务中分离出来。
    数据访问对象接口（Data Access Object Interface） - 该接口定义了在一个模型对象上   要执行的标准操作。
    数据访问对象实体类（Data Access Object concrete class） - 该类实现了上述的接口。该类负责   从数据源获取数据，数据源可以是数据库，也可以是 xml，或者是其他的存储机制。
    模型对象/数值对象（Model Object/Value Object） - 该对象是简单的 POJO，包含了 get/set 方法来存储通过使用 DAO 类检索到的数据。
"""

"""
实现
    1. 创建一个作为模型对象或数值对象的Student对象
    2. StudentDao 是数据访问对象接口
    3. StudentDaoImpl 是实现了数据访问对象接口的实体类
"""
import abc
# 创建数据对象
class Student():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name
    def get_id(self):
        return self.id

# 创建数据访问对象接口。
class StudentDao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getAllStudents(self):
        pass

    @abc.abstractmethod
    def getStudent(self, id):
        pass

    @abc.abstractmethod
    def updateStudent(self, student):
        pass

    @abc.abstractmethod
    def deleteStudent(self, id):
        pass

class StudentDaoImpl(StudentDao):
    def getAllStudents(self):
        pass

    def getStudent(self, id):
        pass

    def updateStudent(self, student):
        pass

    def deleteStudent(self, id):
        pass
