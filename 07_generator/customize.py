'''
自定义实现 loop 和 range
'''


def custom_loop(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            func(next(iterator))
        except StopIteration:
            break


list = [1, 2, 3, 4, 5, 6]
for item in list:
    print(item)
print("=" * 50)
custom_loop(list, print)  # 自定义实现 loop


print("=" * 50)


class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    # __next__方法是迭代器协议的核心部分，它在每次迭代时被调用，返回序列的下一个值。
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # 在没有后续元素时，应该触发StopIteration异常。
        else:
            value = self.current
            self.current += 1
            return value


for item in CustomRange(1, 5):
    print(item)
