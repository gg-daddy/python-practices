# iteratable
# generator
# generator 是一种特殊的迭代器
import inspect
import time

for i in range(5):
    print(i)

# (<class 'range'>, <class 'object'>)
print(inspect.getmro(range))


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        print(f'Running {func.__name__}')
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'It took {t2-t1} s')
        return result
    return wrapper


count = 1000000000
l = list(range(count))


@performance
def use_range():
    '''
    range()函数是一个内置函数，用于生成一个不可变的数字序列。
    由于range()返回的是一个“惰性”序列，
    也就是说，它只在需要时才会生成下一个数字，
    所以它在处理大规模数据时，比直接创建一个包含所有数字的列表更加高效。    
    '''
    for item in range(count):
        item * 5


@performance
def not_use_range():
    for item in l:
        item * 5


'''
即使把 list 创建放到外面，也不如 range 快。 

Running use_range
It took 28.063737154006958 s
Running not_use_range
It took 80.19144177436829 s
'''
use_range()
not_use_range()
