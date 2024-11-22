# content of test_sysexit.py
import pytest

def f():
    raise SystemExit(1)

# 以 test_ 开头的函数会被自动识别为测试用例
def test_mytest():
    with pytest.raises(SystemExit):# 使用 raises 辅助函数断言某些代码引发异常：
        f()