#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/11/24 20:31
# @File ：max.py
# @Author : 胜天半子
# IDE : PyCharm
# @CSDN : https://blog.csdn.net/HG0724?type=blog
# @GitHub : https://github.com/haozhenHG
# 比较集合中的最小元素
min_set = min([{1}, {2}, {3}], key=lambda x: min(x))

# 比较集合中的最大元素
max_set = max([{1}, {2}, {3}], key=lambda x: max(x))
print(min_set)
print(max_set)

print(max([{2}, {1}, {3}]))