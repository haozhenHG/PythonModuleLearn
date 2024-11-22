class MyClass():
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "I am an instance attribute"
    def __getattr__(self, item):
        return '{} is not exist!'.format(item)
    def test(self):
        return 'this is a test method!'

# 创建 MyClass 的实例
obj = MyClass()

# # 访问实例属性
# print(obj.instance_attribute)  # 输出: I am an instance attribute
#
# # 访问类属性
# print(obj.class_attribute)    # 输出: I am a class attribute
#
# # 访问类方法
# print(obj.test())    # 输出: this is a test method!
#
#
# # 访问不存在的属性，将触发 __getattr__
# print(obj.non_existent)      # 输出: Attribute non_existent not found


print('MyClass.__dict__ : ',MyClass.__dict__)
print('obj.__dict__ : ',obj.__dict__)


# print('MyClass.dir : ',MyClass.__dict__())
print('obj.__dir__() : ',obj.__dir__())
print('dir(obj) : ',dir(obj) )
print(obj.__dir__() ==dir(obj) )

