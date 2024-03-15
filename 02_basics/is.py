"""
    is 和 == 的区别
"""

'''
在 Python 中，== 是一个比较运算符，用于比较两个操作数的值是否相等。
如果两个操作数的值相等，那么 == 运算的结果就是 True，否则就是 False。
== 运算符不会进行隐式类型转换，也就是说，如果两个操作数的类型不同，
那么 == 运算的结果通常是 False。

然而，对于布尔值 True 和 False，在进行 == 比较时，
Python 会将它们视为数值 1 和 0。这是一个例外情况。
'''
print(False == 1)
print(True == 1.0)
print('1' == 1)
print(1.0 == 1)
print([] == 0)
print([] == [])
print('' == 0)


print(1 is 1)
print('a' is 'a')
print('Hello World!' is 'Hello World!')
print([] is [])
print(1.0 is 1.0)
