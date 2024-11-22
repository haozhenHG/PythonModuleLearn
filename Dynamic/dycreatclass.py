import inspect,os
import importlib
MyClass = type('MyClass', (), {'attribute': 10})

obj = MyClass()
print(obj.attribute)  # 输出: 10
# type(name, bases, dict) -> a new type

# 在这个示例中，使用type()函数动态地创建了一个名为MyClass的类，它具有一个名为attribute的属性，并赋予其初始值为10。


class Animal():
    name = "11"

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def breathe(self):
        return "我可以呼吸"


a = Animal('大象')
print(type(a))  # 返回类Animal的实例对象  (aka 'object') 或者 <class '__main__.Animal'>)
print(dir(a))
print('*'*100)
People = type("People", (Animal,), {'sex': 'M'})  # 我们定义了一个新类叫People，他继承于animal类，多了一个新的属性sex
'''
type(name, bases, dict, **kwds)
这个时候​type()​函数可以传入三个参数，
    第一个参数name是我们要创建的类的类名，
    第二个参数bases为这个类继承于谁（也就是谁是他的父类），如果为空的话则继承于object类，
    第三个参数dict是一个字典，包含类的属性和方法定义。
    注意，bases参数必须是一个元组，所以要使用元组的形式把参数传进去！
'''
human = People('男人')

print(type(human))  # 返回类People的实例对象 <class '__main__.People'>)
print(dir(human))
print(human.sex)
print('*' * 100)


