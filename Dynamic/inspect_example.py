# -*- coding: utf-8 -*-
import inspect

def example_function(name,age):
    '''
    :param name: input a name str
    :param age: input a age int
    :return:
    '''
    print("Hello, World!")

'''
# 获取函数的源代码
source_code = inspect.getsource(example_function)

print(source_code)



# 获取函数的文档字符串
doc_string = inspect.getdoc(example_function)
print(doc_string)  # 输出: 这是一个示例函数。
print('*'*100)
class ExampleClass:
    def __init__(self):
        self.name='test'
        self.age=3
    def test(self):
        pass

# 获取类的成员
members = inspect.getmembers(ExampleClass)
for name, member in members:
    print(f"{name}: {member}")


def ex_function(a, b, *args, c, d=None):
    pass

# 获取函数的参数签名
signature = inspect.signature(ex_function)
print(signature)

# 获取函数定义的文件名
file_name = inspect.getfile(ex_function)
print(file_name)

# 获取函数所属的模块
module = inspect.getmodule(ex_function)
print(module)
'''
import inspect

class MyClass:
    def method1(self):
        pass

    def method2(self):
        pass

    @property
    def prop(self):
        pass

# 定义一个 predicate 函数，只返回方法
def is_method(member):
    # member 是一个元组，第一个元素是名称，第二个元素是值
    return inspect.isfunction(member) or inspect.ismethod(member)

# 使用 getmembers 获取 MyClass 的所有成员，并使用 predicate 过滤
members = inspect.getmembers(MyClass, predicate=is_method)

# 打印结果
for name, member in members:
    print(f"{name}: {member}")