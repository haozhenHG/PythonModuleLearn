class Person :
    species = "Homo sapiens"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性
    def test(self):
        return 'test'

# 创建 Person 类的实例
john = Person("John", 30)

# 打印实例的 __dict__
print(john.__dict__)

# 输出: {'name': 'John', 'age': 30}

# 打印类的 __dict__
print(Person.__dict__)

# 输出结果将类似于：
# {
#     '__module__': '__main__',  # 类定义所在的模块
#     '__doc__': None,           # 类的文档字符串
#     '__init__': <function Person.__init__ at 0x...>,  # 类的方法
#     'species': 'Homo sapiens',  # 类属性
#     '__dict__': <attribute '__dict__' of 'Person' objects>,  # 类的 __dict__ 属性描述符
#     '__weakref__': <attribute '__weakref__' of 'Person' objects>,  # 用于弱引用
#     '__name__': 'Person',      # 类名
#     '__qualname__': 'Person',  # 限定类名（如果类在嵌套作用域中定义，则包含外层作用域名称）
#     '__annotations__': {},     # 类和方法的注解
#     # 其他内置属性...
# }

# ------------------------------\
# {
# '__module__': '__main__',
# 'species': 'Homo sapiens',
# '__init__': <function Person.__init__ at 0x0000013A1636DF70>,
# 'test': <function Person.test at 0x0000013A1638B040>,
# '__dict__': <attribute '__dict__' of 'Person' objects>,
# '__weakref__': <attribute '__weakref__' of 'Person' objects>,
# '__doc__': None
# }
