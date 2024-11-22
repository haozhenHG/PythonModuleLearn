class MyClass:
    def __init__(self):
        self.aaa = "This attribute exists"

    def __getattr__(self, item):
        # 当访问不存在的属性时，__getattr__ 被调用
        return f"'{item}' attribute is not found"

    @property
    def prer(self):
        return  'this is a test'

# 创建 MyClass 的实例
obj = MyClass()

# 访问存在的属性
print(obj.aaa)
print(obj.prer )
# 访问不存在的属性
print(obj.non_existing_attribute)  # 输出: 'non_existing_attribute' attribute is not found
print(obj.existing_attribute)  # 输出: This attribute exists