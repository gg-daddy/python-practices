

from functools import reduce

# below codes demonstrate how to use map() function


def square(x):
    return x ** 2


squares = map(square, [1, 4, 5, 6, 12])
# map() 函数不会立即执行计算，而是返回一个特殊的 map 对象，这个对象会在你需要结果时（例如在迭代或转换为列表时）才进行计算。
# 这就是为什么当你试图打印 squares 时，你看到的是一个 map 对象，而不是结果列表。
print(squares)  # <map object at 0x10141caf0>

# 是的，map 对象是一个迭代器，迭代器只能遍历一次。一旦所有数据都被遍历和消耗掉，迭代器就会被耗尽，不能再次使用。
# 在你的代码中，你首先创建了一个 map 对象 squares，然后尝试将其转换为元组。这个过程会遍历 squares 中的所有元素，所以之后 squares 就被耗尽了。
# 如果你想再次使用相同的 map 对象，你需要重新创建它。
print(tuple(squares))

print(list(map(square, [1, 4, 5, 6, 12])))
print(set(map(square, [1, 4, 5, 6, 12])))


def is_even(x):
    return x % 2 == 0


# below code demonstrate how to use filter
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = filter(is_even, some_list)
print(list(f))
print(some_list)

# below code demonstrate how to use zip
some_list1 = [1, 2]  # zip 函数会在最短的可迭代对象耗尽时停止。
some_list2 = {"a", "b", "c", "d"}  # set 可以和 zip 用，但是没有顺序， 每次运行，可能结果不一样。
some_list3 = ("apple", "banana", "cherry")

zipped_list = list(zip(some_list1, some_list2, some_list3))
print(zipped_list)


def accumulator(acc, item):
    return acc + item


reduce_result = reduce(accumulator, list(range(1, 101)))
print(reduce_result)
