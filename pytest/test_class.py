class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
        #hasattr用于检查对象（object）是否具有名为 name 的属性。如果对象有这个属性，hasattr 函数返回 True；否则返回 False