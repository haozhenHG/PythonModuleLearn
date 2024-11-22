class A(object):
    def __init__(self, value):
        self.value = value

    def __getattr__(self, item):
        print("into __getattr__")
        print('{} is not exist!!'.format(item))
        return "can not find"


a = A(10)
print(a.value)
print(a.name)

'''
__getattr__函数的作用： 如果属性查找（attribute lookup）在实例以及对应的类中（通过__dict__)失败， 那么会调用到类的__getattr__函数；
'''