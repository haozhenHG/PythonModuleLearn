import time
import  os ,argparse,sys

# __file__ 是一个特殊变量，它在类和函数定义时自动被设置为当前文件的路径
print('test:',os.path.abspath(__file__) )   # 打印当前文件的绝对路径
print('test:',os.path.abspath(__file__).index("learnTest") )
print('test:',os.path.abspath(__file__)[:os.path.abspath(__file__).index("learnTest")])  # __file__ 是一个特殊变量，它在类和函数定义时自动被设置为当前文件的路径
print('os.sep:',os.path.abspath(__file__).split(os.sep),' /// ',os.sep )

print(*[f"{path}\n" for path in sys.path], end='\n')
print('*'*40)
print('test:',sys.path.append(os.path.abspath(__file__)[:os.path.abspath(__file__).index("learnTest")]) ) # __file__ 是一个特殊变量，它在类和函数定义时自动被设置为当前文件的路径
print(*[f"{path}\n" for path in sys.path], end='\n')

print('*'*40)
class MyClass:

    @property # 用于将一个方法转换为属性访问器  这意味着你可以像访问属性一样访问这个方法，而不需要使用括号。
    def current_format_time(self):
        return time.strftime('%Y-%m-%d-%X',time.localtime(time.time())).replace(';','-')

# 创建 MyClass 的实例
my = MyClass()
# 访问 current_format_time 属性
print(my.current_format_time.replace(':',''))
print('*'*40)

import os

# 合并路径组件
path = os.path.join('my', 'folder', 'subfolder', 'file.txt')
print(path)

# print('sys:',sys.path.append(os.path.abspath(__file__)))
print('*'*40)
# 连接字符串列表
elements = ['2024', '01', '22']
result = ":".join(elements)
print(result)  # 输出: 2024:01:22