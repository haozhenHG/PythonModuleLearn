class Person:
    ter = 'name'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# 创建 Person 类的实例
a = Person("Alice", 30)

# 使用 dir() 函数打印实例 a 的属性和方法
print('dir(a):',dir(a))
print('dir(Person)):',dir(Person))
print(set(dir(a))-set(dir(Person)))