"""Model-View-Controller"""
"""
MVC 模式代表 Model-View-Controller（模型-视图-控制器） 模式。这种模式用于应用程序的分层开发。

Model（模型） - 模型代表一个存取数据的对象或 JAVA POJO。它也可以带有逻辑，在数据变化时更新控制器。
View（视图） - 视图代表模型包含的数据的可视化。
Controller（控制器） - 控制器作用于模型和视图上。它控制数据流向模型对象，并在数据变化时更新视图。它使视图与模型分离开。
"""

"""
1. 创建一个作为模型的 Student 对象
2. StudentView 是一个把学生详细信息输出到控制台的视图类
3. StudentController 是负责存储数据到 Student 对象中的控制器类，并相应地更新视图 StudentView
"""

from collections import Iterable

class retriveStudentFromDatabase():
    student_info = []

    def __init__(self):
        self.student_info = [Student("张三", 1), Student("李四", 2), Student("王五", 3)]

    def get_date(self):
        return self.student_info

class Student():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return "姓名:{}, ID:{}".format(self.name, self.id)

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


class StudentView():
    def printStudentDetails(self, name, id):
        print("姓名:{}, ID:{}".format(name, id))


class StudentController():

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def updateView(self):
        if isinstance(self.model, Iterable):
            for i in self.model:
                self.view.printStudentDetails(i.get_name(), i.get_id())
        else:
                self.view.printStudentDetails(self.model.get_name(), self.model.get_id())


if __name__ == '__main__':

    model  = retriveStudentFromDatabase().get_date()
    view  = StudentView()
    controller  = StudentController(model, view)
    controller.updateView()
