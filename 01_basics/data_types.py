
# 基础数据类型， build-in data types
int
float
bool
str
list
tuple
set
dict

# 自定义数据类型，使用 Class 扩展

# 第三方包中提供的数据类型，比如 NumPy 中的 ndarray

# nothing.
None

# list all built-in data types in python
import pprint
pprint.pprint(dir(__builtins__))


import sys

# 创建一个 int 和 float
int_value = 1
float_value = 1.0

# 获取它们的大小
int_size = sys.getsizeof(int_value)
float_size = sys.getsizeof(float_value)

print(f"Size of int: {int_size} bytes")
print(f"Size of float: {float_size} bytes")


