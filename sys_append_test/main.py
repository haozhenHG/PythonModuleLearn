#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/11/26 20:51
# @File ：main.py
# @Author : 胜天半子
# IDE : PyCharm
# @CSDN : https://blog.csdn.net/HG0724?type=blog
# @GitHub : https://github.com/haozhenHG
# main.py
import sys
import os


# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
print('*'*100)
print('current_file_path:',os.path.abspath(__file__))

print('current_dir:',current_dir)
print('before_sys.path ',sys.path)

# 将  目录添加到 sys.path
sys.path.append(os.path.join("../learnTest"))
print('after_sys.path ',sys.path)
print('*'*100)
from module.module1 import greet as greet1
from module.module2 import greet as greet2

def main():
    print(greet1())
    print(greet2())

if __name__ == "__main__":
    main()
