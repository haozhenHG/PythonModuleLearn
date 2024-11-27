#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/11/27 20:57
# @File ：decorate.py
# @Author : 胜天半子
# IDE : PyCharm
# @CSDN : https://blog.csdn.net/HG0724?type=blog
# @GitHub : https://github.com/haozhenHG
import logging
import functools

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')

# 定义装饰器
def use_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.warning(f"{func.__name__} is running")
        result = func(*args, **kwargs)
        logging.warning(f"{func.__name__} has finished")
        return result
    return wrapper

# 应用装饰器到函数
@use_logging
def foo():
    print('i am foo')

@use_logging
def bar():
    print('i am bar')

@use_logging
def bar2():
    print('i am bar2')

if __name__ == "__main__":
    foo()
    bar()
    bar2()