
# list all logical operators
# > , < , >= , <= , == , !=
# and , or , not

print(not True)
# () 在这里只是改变了表达式的优先级，但由于 not 后面只有一个表达式 True，所以无论是否有括号，not 都会直接对 True 进行取反操作，结果都为 False。
print(not (True))

if 'a' > 'A':  # 比较的是 unicode 编码， 具体可以看 ord 的结果。
    print('a > A')
else:
    print('a < A')

print(ord('a'))
print(ord('A'))
