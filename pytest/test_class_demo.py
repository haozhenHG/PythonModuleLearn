# 在类中对测试进行分组时需要注意的是，每个测试都有一个唯一的类实例。
# 让每个测试共享同一个类实例将非常不利于测试隔离，并且会促进不良的测试实践。
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1