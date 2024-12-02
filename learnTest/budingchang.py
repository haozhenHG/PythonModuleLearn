# coding=utf-8

# 第一个是元组形式，第二个是字典形式
def sun(aa,*args,**kwargs):
    print(aa)
    print(kwargs)
    print(args)


sun(1, 55258, x=25412, y=5123512)

print('*'*100)
# coding=utf-8

# 使用不定长参数传固定值,注意，b、c可省略，a不可省略
def fuzhi(a, *b, **c):
    print(a)
    print(b)
    print(c)


fuzhi(3)

# coding=utf-8

# 用不定长参数实行累加
print('*'*100)
def sum(*nums):
    """
    求多个数之和
    :param list_one: 接收数字的不定长参数，会把参数组装成一个(tuple)元祖，赋值给不定长参数
    :return: 返回所有数字之和
    """
    result = 0
    for num in nums:
        if isinstance(num, (int, float)):
            result = result + num

    return result


sum()

print(sum(1, 2, 3))
print('*'*100)

# 当我们将普通参数写在不定长参数写在后面时
# coding=utf-8

def JayChou(a, *b, c):
    print(a)
    print(b)
    print(c)


JayChou(1, 555, 5768, 55451,c=5)

print('*'*100)

# coding=utf-8

# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
def void_tuple(a, *tuplela):
    print(a)
    for b in tuplela:
        print(b)
    return


print(void_tuple(3))
print('*'*100)
print(dir(__builtins__))
print('*'*100)
def not_with_param(dot):
    print(*dot)

not_with_param([4,15,7,9,'y'])