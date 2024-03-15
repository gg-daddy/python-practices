
for item in range(5):
    print(item)

# 这个比较特别， 上面 item 实在 for-loop 使用的变量。
# 但是在 for-loop 之外也可以使用， 保留了最后一次的值
print(item)


# 如何针对一个 list 进行求和
my_list = range(1, 11)
sumed_value = sum(my_list)
print(sumed_value)

sumed_value2 = 0
for item in my_list:
    sumed_value2 += item
print(sumed_value2)

# range ，可以快速生成一个 list
l = list(range(1, 11))
print(l)

# 可以指定步长和方向
l2 = list(range(10, 0, -1))
print(l2)

# 也可以使用 for-loop 来遍历一个 range object.
for _ in range(5):
    print(_)  # _ 也是一个合法的变量名， 只是表示这个变量通常不会被关心和使用。
    print('Hello World!')


my_list = [1, -2, 3, -4, 5, -6]

negative_indices = [i for i, item in enumerate(my_list) if item < 0]
print(negative_indices)  # 输出：[1, 3, 5]