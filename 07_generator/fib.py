# 使用 generator 编写 fibonacci 数列
from time import time


def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a+b


n = 2000000

t1 = time()
for item in fib(n):
    item * 2
t2 = time()
print(f'It took {t2-t1} s')


def fib2(n):
    a = 0
    b = 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a+b
    return result


t1 = time()
for item in fib2(n):
    item * 2
t2 = time()
print(f'It took {t2-t1} s')
