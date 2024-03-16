'''
Function parameter order rule: params, *args, default params, **kwargs

在 Python 中，函数参数的顺序规则是：位置参数（params）、可变位置参数（*args）、默认参数（default params）、可变关键字参数（**kwargs）。
这是 Python 函数定义中参数的标准顺序。

1. 位置参数（params）：这些是普通的参数，它们的位置在函数调用中是重要的。例如，在 def func(a, b): 中，a 和 b 就是位置参数。
2. 可变位置参数（*args）：这是一个特殊的参数，可以接收任意数量的位置参数。在函数内部，这些参数被存储在一个元组中。例如，在 def func(*args): 中，args 就是可变位置参数。
3. 默认参数（default params）：这些参数有一个默认值，如果在函数调用中没有提供这些参数的值，那么就会使用默认值。例如，在 def func(a=1): 中，a 就是一个默认参数。
4. 可变关键字参数（kwargs）**：这是一个特殊的参数，可以接收任意数量的关键字参数。
在函数内部，这些参数被存储在一个字典中。例如，在 def func(**kwargs): 中，kwargs 就是可变关键字参数。
'''

# 函数定义中的 *args， 表示接收任意数量的位置参数，并且在函数内部，这些参数被存储在一个元组中，这个元组的名称就是 args。


def super_func(*args, **kwargs):
    # args 表示元组，*args 表示元组解包，将元组中的元素解包出来
    print(f"args: {args} ")
    print("args after unpacking: ", *args)

    print(f"kwargs: {kwargs} ")
    for k in kwargs:
        print(k)

    return sum(args)


print(super_func(1, 2, 3, 4, 5, test=1, tes2=2))

kwargs = {
    "test": 1,
    "test2": 2
}
print(super_func(**kwargs))
