import pytest

def f():
    raise ExceptionGroup(
        "Group message",
        [
            RuntimeError(),
        ],
    )


def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        f()
    assert excinfo.group_contains(RuntimeError)
    assert not excinfo.group_contains(TypeError)
    # group_contains 是 pytest 中的一个方法，它用于检查在 ExceptionGroup 中是否包含了指定类型的异常。